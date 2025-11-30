from models.types import Type


class ErrorFormatter:
    @staticmethod
    def cant_assign_from_to(from_type: Type, to_type: Type):
        return f'Нельзя присвоить значение типа {from_type} переменной типа {to_type}'

    @staticmethod
    def unmatched_number_of_expressions_or_not_single_expression():
        return 'Количество выражений должно совпадать с количеством переменных или быть равным 1'

    @staticmethod
    def redefined_symbol(symbol_id: str):
        return f"Символ {symbol_id} уже определен в этой области видимости"

    @staticmethod
    def undefined_symbol(symbol_id: str):
        return f'Символ {symbol_id} не определен'

    @staticmethod
    def undefined_global_symbol(symbol_id: str):
        return f'Символ {symbol_id} не определен в глобальной области видимости'

    @staticmethod
    def undefined_subprogram(subprogram_id: str):
        return f'Подпрограмма {subprogram_id} не определена'

    @staticmethod
    def uninitialized_global_symbol(symbol_id: str):
        return f'Глобальная переменная {symbol_id} вне подпрограммы не инициализирована'

    @staticmethod
    def no_overload_found(sub_name: str, sub_parameters: list[Type]):
        params_string = ', '.join([param.name for param in sub_parameters if param is not None])
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
    def flow_control_operator_outside_of_loop():
        return "Операторы continue и break могут использоваться только внутри циклов"

    @staticmethod
    def unmatched_condition_type(actual_type: Type):
        return f"Ожидался булев тип в условии. Получен {actual_type}"

    @staticmethod
    def invalid_cast(from_type: Type, to_type: Type):
        return f"Невозможно преобразовать {from_type} в {to_type}"
