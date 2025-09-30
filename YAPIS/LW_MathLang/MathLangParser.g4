parser grammar ExprParser;
options { tokenVocab=ExprLexer; }

program
    : statement* EOF ;

statement 
    : control_flow_operator | block | declaration | subprogram | branching | loop | assignment | call ;
    
subprogram 
    : SUB ID '(' declaration_list? ')' block ;
branching 
    : IF '(' expression ')' block (ELSE block)? ;

declaration 
    : declaration_list;
assignment 
    : (declaration_list | id_list) assignment_operator expression_list ;
call 
    : ID '(' expression_list? ')' ;
    
loop
    : for_loop | while_loop | until_loop ;
for_loop 
    : FOR '(' assignment ';' expression ';' statement ')' block;
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
    | expression binary_operator expression
    | unary_operator expression
    | ('(' expression ')') ;
    
cast_expression
    : type_specifier '(' expression ')' ;
    
assignment_operator : simple_assignment_operator ;

simple_assignment_operator : EQ ;

binary_operator 
    : PLUS 
    | MINUS 
    | ASTERISK 
    | SLASH
    | CARET
    | (EQ EQ)
    | OR
    | AND 
    | NOT 
    | GT
    | LS 
    | (GT EQ)
    | (LS EQ) ;
 
unary_operator
    : MINUS ;
    
control_flow_operator
    : RETURN
    | BREAK
    | CONTINUE ;
    
literal 
    : INT 
    | FLOAT 
    | BOOL
    | STRING ;

declaration_list 
    : scope_modifier? type_specifier variable_declaration (',' scope_modifier? type_specifier?  variable_declaration)*
    ;

variable_declaration 
    : ID (simple_assignment_operator expression)?
    ;

type_specifier 
    : FLOAT_T | INT_T | BOOL_T;

scope_modifier 
    : GLOBAL ;
