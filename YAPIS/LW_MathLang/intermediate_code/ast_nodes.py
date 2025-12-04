from dataclasses import dataclass, Field
from typing import List, Optional


@dataclass
class ProgramNode:
    subprograms: List['SubprogramNode']
    statements: List['StatementNode']


@dataclass
class SubprogramNode:
    name: str
    ret_type: str
    params: list[str]
    param_types: list[str]
    body: 'BlockNode'


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
class VarDecl(StatementNode):
    type: str
    name: str
    init: Optional['Expr']

@dataclass
class Return(StatementNode):
    pass

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
    step: Optional['Expr']
    body: BlockNode


@dataclass
class Expr(StatementNode):
    type: str


@dataclass
class IntLiteral(Expr):
    value: int

@dataclass
class FloatLiteral(Expr):
    value: float

@dataclass
class StringLiteral(Expr):
    value: str

@dataclass
class BoolLiteral(Expr):
    value: bool


@dataclass
class VarRef(Expr):
    name: str

@dataclass
class AssignNode(Expr):
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
    target_type: str
    expr: Expr