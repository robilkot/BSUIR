import json

from backend_py.abstract import AbstractGenerator
from backend_py.keyword_abstract import KeywordAbstract
from backend_py.llm import LLM


class LLMKeywordAbstractGenerator(AbstractGenerator, LLM):
    def _create_keyword_prompt(self, text: str, top_n: int) -> str:
        return f"""
            Проанализируй следующий текст и выдели {top_n} самых важных ключевых слов и словосочетаний.
            Для каждого ключевого слова приведи 1-2 примера употребления из текста.
            
            Текст для анализа:
            {text}
            
            Верни ответ в формате JSON:
            {{
                "keywords": [
                    {{
                        "keyword": "ключевое слово или словосочетание",
                        "frequency": число_вхождений,
                        "phrases": ["пример фразы 1", "пример фразы 2"]
                    }}
                ]
            }}
            
            Только JSON, без дополнительного текста.
            """

    def _parse_llm_response(self, response: str, top_n: int) -> KeywordAbstract:
        abstract = KeywordAbstract()

        try:
            # Пытаемся найти JSON в ответе
            json_start = response.find('{')
            json_end = response.rfind('}') + 1
            if json_start != -1 and json_end != 0:
                json_str = response[json_start:json_end]
                data = json.loads(json_str)

                keywords_data = data.get("keywords", [])
                for kw_data in keywords_data[:top_n]:
                    keyword = kw_data.get("keyword", "").strip()
                    frequency = kw_data.get("frequency", 1)
                    phrases = kw_data.get("phrases", [])

                    if keyword:
                        # Добавляем ключевое слово
                        node = abstract.add_keyword(keyword)
                        node.frequency = frequency

                        # Добавляем примеры фраз
                        for phrase in phrases:
                            if phrase.strip():
                                node.add_phrase(phrase.strip())

        except (json.JSONDecodeError, KeyError) as e:
            raise Exception(f"Ошибка при парсинге ответа от LLM: {e}\nОтвет: {response}")

        return abstract

    def generate(self, text: str, top_n: int = 20) -> KeywordAbstract:
        if not text.strip():
            raise ValueError("Текст не может быть пустым")

        prompt = self._create_keyword_prompt(text, top_n)

        llm_response = self._call_ollama(prompt)

        abstract = self._parse_llm_response(llm_response, top_n)

        return abstract


if __name__ == "__main__":
    sample_text = """
    Искусственный интеллект (ИИ) - это область компьютерных наук, занимающаяся созданием 
    машин, способных выполнять задачи, требующие человеческого интеллекта. Машинное обучение 
    является подразделом искусственного интеллекта, которое фокусируется на разработке 
    алгоритмов, позволяющих компьютерам обучаться на основе данных. Глубокое обучение - это 
    вид машинного обучения, использующий нейронные сети с множеством слоев. 
    Современные системы искусственного интеллекта находят применение в различных областях, 
    включая обработку естественного языка, компьютерное зрение и автономные транспортные средства.
    """

    generator = LLMKeywordAbstractGenerator()
    abstract = generator.generate(sample_text, top_n=10)
    abstract.print()