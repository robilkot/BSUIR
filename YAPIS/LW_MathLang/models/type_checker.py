from models.error_formatter import ErrorFormatter
from models.errors import SemanticError
from models.types import Type


class TypeChecker:
    @staticmethod
    def is_templated_argument(type: Type | None) -> bool:
        return not type in [Type.float(), Type.int(), Type.bool()]

    @staticmethod
    def is_numeric_type(type: Type | None) -> bool:
        return type in [Type.float(), Type.int()]

    @staticmethod
    def is_boolean_type(type: Type | None) -> bool:
        return type in [Type.bool()]

    @staticmethod
    def can_cast(from_type: Type, to_type: Type) -> bool:
        if from_type is None or to_type is None:
            return False

        can_cast = {
            Type.bool(): [],
            Type.string: [],
            Type.void: [],
            Type.int(): [Type.float()],
            Type.float(): [Type.int()],
        }

        if from_type == to_type:
            return True

        return to_type in can_cast.get(from_type, [])

    @staticmethod
    def get_binary_operation_type(left_type: Type, right_type: Type, operator: str) -> Type:
        """Определяет тип результата бинарной операции"""
        numeric_ops = ['+', '-', '*', '/', '%', '^']
        comparison_ops = ['==', '!=', '<', '>', '<=', '>=']
        logical_ops = ['and', 'or']

        # Assuming binary operations only allowed on same types
        # todo does not seem valid
        if TypeChecker.is_templated_argument(left_type) and not TypeChecker.is_templated_argument(right_type):
            return right_type

        if TypeChecker.is_templated_argument(right_type) and not TypeChecker.is_templated_argument(left_type):
            return left_type

        if operator in numeric_ops:
            if TypeChecker.is_templated_argument(left_type) and left_type == right_type:
                return left_type

            if not (TypeChecker.is_numeric_type(left_type) and left_type == right_type):
                raise SemanticError(ErrorFormatter.binary_operator_only_valid_on_types(operator, "одинаковым числовым типам", left_type, right_type))
            return left_type

        elif operator in comparison_ops:
            if left_type != right_type:
                raise SemanticError(ErrorFormatter.binary_operator_only_valid_on_types(operator, "одинаковым числовым типам", left_type, right_type))
            return Type.bool()

        elif operator in logical_ops:
            if not (TypeChecker.is_boolean_type(left_type) and TypeChecker.is_boolean_type(right_type)):
                raise SemanticError(ErrorFormatter.binary_operator_only_valid_on_types(operator, "булевым типам", left_type, right_type))
            return Type.bool()

        raise ValueError(f"Неизвестный оператор: {operator}")
