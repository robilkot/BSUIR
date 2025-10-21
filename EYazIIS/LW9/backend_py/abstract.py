from abc import ABC


class Abstract(ABC):
    pass


class AbstractGenerator(ABC):
    def generate(self, text: str) -> Abstract:
        pass
