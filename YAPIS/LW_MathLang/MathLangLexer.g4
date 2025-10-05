lexer grammar MathLangLexer;

AND : 'and' ;
OR : 'or' ;
NOT : 'not' ;

EQ : '=' ;
GT : '>' ;
LS : '<' ;

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