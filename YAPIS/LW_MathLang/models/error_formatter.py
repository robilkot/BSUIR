from models.types import Type


class ErrorFormatter:
    @staticmethod
    def cant_assign_from_to(from_type: Type, to_type: Type):
        return f'Нельзя присвоить значение типа {from_type} переменной типа {to_type}'

    @staticmethod
    def unmatched_variables_and_expressions():
        return 'Количество переменных и выражений в присваивании не совпадает'

    @staticmethod
    def unmatched_number_of_expressions_or_not_single_expression():
        return 'Количество выражений должно совпадать с количеством переменных или быть равным 1'

    @staticmethod
    def undefined_symbol(id: str):
        return f'Символ {id} не определен'

    @staticmethod
    def undefined_subprogram(id: str):
        return f'Подпрограмма {id} не определена'

    @staticmethod
    def no_overload_found(sub_name: str, sub_parameters: list[Type]):
        params_string = ', '.join([type.name for type in sub_parameters if type is not None])
        return f"Не найдено перегрузки {sub_name} с параметрами {params_string}"

    @staticmethod
    def binary_operator_only_valid_on_types(operator: str, type_description: str, left_type: Type, right_type: Type):
        return f"Оператор '{operator}' применим только к {type_description}. Получены типы {left_type}, {right_type}"

    @staticmethod
    def unary_operator_only_valid_on_types(operator: str, type_description: str, actual_type: Type):
        return f"Оператор '{operator}' применим только к {type_description}. Получен тип {actual_type}"

    @staticmethod
    def return_outside_of_subprogram():
        return "Оператор return может использоваться только внутри подпрограмм"

    @staticmethod
    def unmatched_condition_type(actual_type: Type):
        return f"Ожидался булев тип в условии. Получен {actual_type}"

    @staticmethod
    def invalid_cast(from_type: Type, to_type: Type):
        return f"Невозможно преобразовать {from_type} в {to_type}"
