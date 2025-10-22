from backend_py.classic_abstract import ClassicAbstractGenerator
from backend_py.keyword_en import ENKeywordAbstractGenerator
from backend_py.keyword_ru import RUKeywordAbstractGenerator

if __name__ == '__main__':
    sample_text = """
    Лазер — это устройство, создающее узкий пучок интенсивного света. 
    Лазеры находят применение в самых разных областях: от медицины до телекоммуникаций. 
    Принцип работы лазера основан на явлении вынужденного излучения. 
    Существуют различные типы лазеров, например, газовые лазеры, твердотельные лазеры и полупроводниковые лазеры. 
    Красный лазер часто используется в указателях, в то время как синий лазер обладает большей энергией и применяется в Blu-ray технологиях. 
    Мощность лазерного луча можно регулировать в зависимости от задачи. 
    Устройство лазера включает в себя активную среду, источник накачки и оптический резонатор.
    """

    print("Реферат в виде структуры ключевых слов:")
    print("=" * 50)

    keyword_generator = RUKeywordAbstractGenerator()
    # keyword_generator = ENKeywordAbstractGenerator()

    keyword_structure = keyword_generator.generate(sample_text, top_n=5)
    keyword_structure.print()

    classic_abstract = ClassicAbstractGenerator(language='russian').generate(sample_text, num_sentences=5)
    classic_abstract.print()
