from dataclasses import dataclass
from typing import Callable

from generated.grammar.MathLangParser import MathLangParser
from models.error_formatter import ErrorFormatter
from models.errors import SemanticError
from models.types import Type


class Symbol:
    def __init__(self, name, type: Type, is_global: bool = False):
        self.name = name
        self.type: Type = type
        self.is_global = is_global

    def __str__(self):
        return f"{'global ' if self.is_global else ''}{self.type.name} {self.name}"

    def __repr__(self):
        return self.__str__()

    def __key(self):
        return self.is_global, self.name, self.type

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        if isinstance(other, Symbol):
            return self.__key() == other.__key()
        return NotImplemented


# todo check for global symbols definition on call
# todo check for identical subprograms with different teamplte arg names
class SubprogramSymbol(Symbol):
    def __init__(self, name, parameters: list[Symbol], return_type: Type, template_args: list[Type] | None):
        super().__init__(name, return_type)
        self.parameters: list[Symbol] = parameters
        self.template_args: list[Type] | None = template_args
        self.local_scope = SymbolTable()

    def __str__(self):
        if self.template_args is None or len(self.template_args) == 0:
            return f"sub {self.name}({self.__params_str()}) -> {self.type}"
        else:
            return f"sub {self.name}<{self.__template_args_str()}>({self.__params_str()}) -> {self.type}"

    def __repr__(self):
        return self.__str__()

    def __params_str(self):
        return ", ".join([symbol.type.name for symbol in self.parameters])

    def __template_args_str(self):
        if self.template_args is None:
            return ""

        return ", ".join([type.name for type in self.template_args])

    def __key(self):
        return self.name, self.type, self.__params_str(), self.__template_args_str()

    def __hash__(self):
        return hash(self.__key())


class SymbolTable:
    def __init__(self, parent=None):
        self.symbols = set()
        self.symbols_dict: dict[str, list[Symbol]] = {}

        self.parent = parent
        self.children = []

    def __str__(self):
        return self.symbols.__str__()

    def __repr__(self):
        return self.__str__()

    def remove_symbol(self, symbol: Symbol):
        self.symbols.remove(symbol)

        existing_symbols = self.symbols_dict.get(symbol.name, [])
        existing_symbols.remove(symbol)
        self.symbols_dict[symbol.name] = existing_symbols

    def add_symbol(self, symbol: Symbol, exist_ok: bool = False):
        if symbol in self.symbols:
            if exist_ok:
                return
            else:
                raise SemanticError(ErrorFormatter.redefined_symbol(symbol))

        if self.parent is not None:
            if self.parent.has_defined(symbol):
                msg = f"'Warning: {symbol}' уже объявлен в верхней области видимости"
                print(msg) # Своего рода warning

        self.symbols.add(symbol)
        existing_symbols = self.symbols_dict.get(symbol.name, [])
        existing_symbols.append(symbol)
        self.symbols_dict[symbol.name] = existing_symbols

    def has_defined(self, symbol: Symbol) -> bool:
        return self.lookup(symbol.name) is not None

    def lookup(self, name: str) -> None | list[Symbol]:
        if name in self.symbols_dict:
            return self.symbols_dict[name]
        if self.parent:
            return self.parent.lookup(name)
        return None

    def create_child_scope(self) -> "SymbolTable":
        child = SymbolTable(self)
        self.children.append(child)
        return child
