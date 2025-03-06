from corpus_entry import CorpusEntry
import json

class CorpusManager:
    def __init__(self):
        self.entries = {}  # Хранение записей корпуса по id

    def add_entry(self, entry_id, text, bibliographic=None, typological=None):
        if entry_id in self.entries:
            raise ValueError(f"Запись с id {entry_id} уже существует.")
        self.entries[entry_id] = CorpusEntry(entry_id, text, bibliographic, typological)

    def edit_entry(self, entry_id, new_text):
        if entry_id not in self.entries:
            raise ValueError(f"Запись с id {entry_id} не найдена.")
        entry = self.entries[entry_id]
        entry.text = new_text
        entry.tokens = entry.analyze_text(new_text)

    def delete_entry(self, entry_id):
        if entry_id in self.entries:
            del self.entries[entry_id]

    def search_tokens(self, condition_func):
        results = []
        for entry in self.entries.values():
            for token in entry.tokens:
                if condition_func(token):
                    results.append((entry.id, token))
        return results

    def compute_frequency(self):
        freq_feats = {}
        for entry in self.entries.values():
            for token in entry.tokens:
                if token.pos == "PUNCT":
                    continue
                freq_feats.setdefault("pos", {})
                freq_feats["pos"][token.pos] = freq_feats["pos"].get(token.pos, 0) + 1
                for key, val in token.feats.items():
                    freq_feats.setdefault(key, {})
                    freq_feats[key][val] = freq_feats[key].get(val, 0) + 1
        return freq_feats

    def get_wordforms_info(self):
        wordforms_freq = {}
        for entry in self.entries.values():
            for token in entry.tokens:
                if token.pos == "PUNCT":
                    continue
                wordforms_freq[token.text] = wordforms_freq.get(token.text, 0) + 1
        result = {}

        for entry in self.entries.values():
            for token in entry.tokens:
                if token.pos == "PUNCT":
                    continue
                result[token.text] = {
                    "freq": wordforms_freq[token.text],
                    "lemma": token.lemma,
                    "morph": token.feats,
                }
        return result

    def get_concordance(self, target_text, window=3):
        """
        Поиск конкорданса с учётом текста и леммы (регистронезависимо).
        """
        target_lower = target_text.lower()
        concordance_list = []
        for entry in self.entries.values():
            for i, token in enumerate(entry.tokens):
                if token.text.lower() == target_lower or token.lemma.lower() == target_lower:
                    left_context = [t.text for t in entry.tokens[max(0, i-window):i]]
                    right_context = [t.text for t in entry.tokens[i+1:i+1+window]]
                    concordance_list.append({
                        "entry_id": entry.id,
                        "target_index": i,
                        "left_context": left_context,
                        "target": token.text,
                        "right_context": right_context
                    })
        return concordance_list

    def save_corpus(self, filepath):
        data = {}
        for entry_id, entry in self.entries.items():
            data[entry_id] = {
                "text": entry.text,
                "bibliographic": entry.bibliographic,
                "typological": entry.typological,
                "tokens": [
                    {
                        "text": token.text,
                        "lemma": token.lemma,
                        "pos": token.pos,
                        "feats": token.feats,
                        "index": token.index
                    }
                    for token in entry.tokens
                ]
            }
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load_corpus(self, filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        self.entries = {}
        for entry_id, entry_data in data.items():
            self.entries[entry_id] = CorpusEntry(
                entry_id,
                entry_data["text"],
                entry_data.get("bibliographic"),
                entry_data.get("typological")
            )
