from dataclasses import dataclass
from typing import List, Optional

from models.types import Type


@dataclass
class ProgramNode:
    subprograms: List['SubprogramNode']
    statements: List['StatementNode']


@dataclass
class StatementNode:
    pass

# Flow control statement
@dataclass
class ReturnNode(StatementNode):
    pass

@dataclass
class BreakNode(StatementNode):
    pass

@dataclass
class ContinueNode(StatementNode):
    pass



@dataclass
class GlobalVarDeclaration(StatementNode):
    type: Type
    name: str

@dataclass
class BlockNode(StatementNode):
    body: List['StatementNode']

@dataclass
class IfStmt(StatementNode):
    cond: 'Expr'
    then_body: BlockNode
    else_body: Optional[BlockNode]


@dataclass
class WhileStmt(StatementNode):
    cond: 'Expr'
    body: BlockNode

@dataclass
class UntilStmt(StatementNode):
    cond: 'Expr'
    body: BlockNode

@dataclass
class ForStmt(StatementNode):
    init: Optional[StatementNode]
    cond: Optional['Expr']
    step: Optional[StatementNode]
    body: BlockNode


@dataclass
class Expr(StatementNode):
    type: Type

@dataclass
class SubprogramNode(Expr):
    name: str
    param_names: list[str]
    param_types: list[Type]
    body: 'BlockNode'

    def __hash__(self) -> int:
        return hash((self.name, ','.join(self.param_names), ','.join([str(typ) for typ in self.param_types])))


@dataclass
class IntLiteral(Expr):
    value: int

    def __init__(self, value: int):
        self.type = Type.int()
        self.value = value

@dataclass
class FloatLiteral(Expr):
    value: float

    def __init__(self, value: float):
        self.type = Type.float()
        self.value = value

@dataclass
class StringLiteral(Expr):
    value: str

    def __init__(self, value: str):
        self.type = Type.string()
        self.value = value

@dataclass
class BoolLiteral(Expr):
    value: bool

    def __init__(self, value: bool):
        self.type = Type.bool()
        self.value = value


@dataclass
class VarRef(Expr):
    name: str

@dataclass
class AssignNode(StatementNode):
    name: str
    value: Expr


@dataclass
class BinaryOp(Expr):
    op: str
    left: Expr
    right: Expr

@dataclass
class UnaryOp(Expr):
    op: str
    expr: Expr


@dataclass
class SubprogramCall(Expr):
    name: str
    args: List[Expr]

@dataclass
class CastExpr(Expr):
    expr: Expr