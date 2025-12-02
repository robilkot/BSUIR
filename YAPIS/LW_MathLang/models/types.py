from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Type:
    name: str

    @staticmethod
    def int():
        return Type('int')

    @staticmethod
    def float():
        return Type('float')

    @staticmethod
    def bool():
        return Type('bool')

    @staticmethod
    def string():
        return Type('string')

    @staticmethod
    def void():
        return Type('void')

    @staticmethod
    def create(typename: str):
        if isinstance(typename, Type):
            raise ValueError(f'typename уже типа ({typename.name})')

        if typename == "float":
            return Type.float()
        elif typename == "int":
            return Type.int()
        elif typename == "bool":
            return Type.bool()
        elif typename == "string":
            return Type.string()
        elif typename == "void":
            return Type.void()
        else:
            return Type(typename)
        
        
    def to_wat(self):
        if self == Type.int():
            return "i32"
        elif self == Type.float():
            return "f32"
        elif self == Type.bool():
            return "i32"
        elif self == Type.string():
            return "i32"
        elif self == Type.void():
            return ""
        else:
            return "i32"
        

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Type):
            return False
        return self.name == other.name

    def __lt__(self, other: Any) -> bool:
        if not isinstance(other, Type):
            return NotImplemented
        return self.name < other.name
