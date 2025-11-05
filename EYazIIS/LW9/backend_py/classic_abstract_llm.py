import json

from backend_py.abstract import AbstractGenerator
from backend_py.classic_abstract import ClassicAbstract, ScoredSentence
from backend_py.llm import LLM


class LLMClassicAbstractGenerator(AbstractGenerator, LLM):
    def _create_keyword_prompt(self, text: str, top_n: int) -> str:
        return f"""
            Проанализируй следующий текст и сформируй строго {top_n} предложений, описывающих суть текста.
            Предложений должно быть ровно {top_n}. Реферат должен быть на таком же языке, что и сам текст.
            
            Текст для анализа:
            {text}

            Верни ответ в формате JSON:
            {{
                "sentences": ["предложение 1", "предложение 2"]
            }}

            Только JSON и без дополнительного текста.
            """

    def _parse_llm_response(self, response: str) -> ClassicAbstract:
        abstract = ClassicAbstract()

        try:
            json_start = response.find('{')
            json_end = response.rfind('}') + 1
            if json_start != -1 and json_end != 0:
                json_str = response[json_start:json_end]
                json_str = json_str.encode('utf-8')
                data = json.loads(json_str)['sentences']

                for sent in data:
                    abstract.sentences.append(ScoredSentence(original_text=sent))

        except (json.JSONDecodeError, KeyError) as e:
            raise Exception(f"Ошибка при парсинге ответа от LLM: {e}\nОтвет: {response}")

        return abstract

    def generate(self, text: str, top_n: int = 10) -> ClassicAbstract:
        if not text.strip():
            raise ValueError("Текст не может быть пустым")

        prompt = self._create_keyword_prompt(text, top_n)

        llm_response = self._call_ollama(prompt)

        abstract = self._parse_llm_response(llm_response)

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

    generator = LLMClassicAbstractGenerator()
    abstract = generator.generate(sample_text, top_n=10)
    abstract.print()