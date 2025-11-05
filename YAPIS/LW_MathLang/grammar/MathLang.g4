grammar MathLang;

program
    : subprogram*
      statement*
      EOF
    ;

statement
    : control_flow_operator | block | branching | loop | assignment | call ;

subprogram
    : SUB ID '(' declaration_list? ')' block ;
branching
    : IF '(' expression ')' block (ELSE block)? ;

assignment
    : (declaration_list | id_list) assignment_operator expression_list ;

declaration_list
    : scope_modifier? type_specifier variable_declaration (',' type_specifier  variable_declaration)*
    ;

variable_declaration
    : ID (simple_assignment_operator expression)?
    ;

call
    : ID '(' expression_list? ')' ;

loop
    : for_loop | while_loop | until_loop ;
for_loop
    : FOR '(' assignment? ';' expression? ';' statement? ')' block;
while_loop
    : WHILE '(' expression ')' block;
until_loop
    : UNTIL '(' expression ')' block;

block
    : '{' statement* '}' ;


id_list : (ID ',')* ID ;

expression_list : (expression ',')* expression ;
expression
    : ID
    | literal
    | call
    | cast_expression
    | '(' expression ')'
    | NOT expression
    | MINUS expression
    | expression CARET expression
    | expression ASTERISK expression
    | expression SLASH expression
    | expression PLUS expression
    | expression MINUS expression
    | expression AND expression
    | expression OR expression
    | expression EQ EQ expression
    | expression NEQ expression
    | expression GT expression
    | expression LT expression
    | expression GE expression
    | expression LE expression
    ;


cast_expression
    : type_specifier '(' expression ')' ;

assignment_operator : simple_assignment_operator ;

simple_assignment_operator : EQ ;

control_flow_operator
    : RETURN
    | BREAK
    | CONTINUE ;

literal
    : INT
    | FLOAT
    | BOOL
    | STRING ;

type_specifier
    : FLOAT_T | INT_T | BOOL_T;

scope_modifier
    : GLOBAL ;

AND : 'and' ;
OR : 'or' ;
NOT : 'not' ;

EQ : '=' ;
NEQ : '!=' ;
GT : '>' ;
LT : '<' ;
GE : '>=' ;
LE : '<=' ;

COMMA : ',' ;
SEMI : ';' ;
COLON : ':' ;
LPAREN : '(' ;
RPAREN : ')' ;
LCURLY : '{' ;
RCURLY : '}' ;
SLASH : '/' ;
PLUS : '+' ;
MINUS : '-' ;
ASTERISK : '*' ;
CARET : '^' ;
GLOBAL : 'global' ;

FOR : 'for' ;
WHILE : 'while' ;
UNTIL : 'until' ;
BREAK : 'break' ;
CONTINUE : 'continue' ;
RETURN : 'return' ;
IF : 'if' ;
ELSE : 'else' ;

SUB : 'sub' ;
DSLASH : SLASH SLASH ;
FLOAT_T : 'float' ;
INT_T : 'int' ;
BOOL_T : 'bool' ;

INT : '-'?[0-9]+ ;
FLOAT : INT '.' INT? | INT 'e' INT ;
BOOL : 'true' | 'false' ;
STRING  : '"' (~'"')* '"' ;

ID: [a-zA-Z_][a-zA-Z_0-9]* ;
LINE_COMMENT : '//' ~[\r\n]* -> channel(HIDDEN);
WS: [ \t\f\r\n]+ -> skip ;