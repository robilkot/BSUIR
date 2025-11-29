from dataclasses import dataclass


@dataclass
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

    def __str__(self):
        return self.name


    def __hash__(self):
        return hash(self.name)


