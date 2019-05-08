
grammar CustomScript;
/*
 * Parser Rules
 */

script              : scriptelement+ functionstatement* EOF ;

scriptelement       : (forstatement|ifstatement|line);

line                : (op|var|functioncall) NEWLINE;

op                  : command addon*;

addon               : (redirect command?);

redirect            : (customin | out | to);

var                 : (STRINGVAR|NUMBERVAR) WHITESPACE (IDENTIFIER|arg) WHITESPACE? '=' WHITESPACE? (NUMBER|TEXT|operation) (WHITESPACE)*?;

command             : TEXT (WHITESPACE (IDENTIFIER|arg) WHITESPACE?|WHITESPACE)? ;

customin            : IN WHITESPACE ;

out                 : OUT WHITESPACE ;

to                  : TO WHITESPACE ;

ifstatement         : IF WHITESPACE? '(' conditional ')' WHITESPACE? '{' NEWLINE line* '}' NEWLINE;

forstatement        : FOR WHITESPACE? '(' var ';' conditional ';' operation ')' WHITESPACE? '{' NEWLINE line* '}' NEWLINE;

functionstatement   : FUN WHITESPACE IDENTIFIER WHITESPACE '{' NEWLINE line*  '}' NEWLINE;

functioncall        : IDENTIFIER '(' functioninput? ')';

functioninput       : functioninputpart ((',' WHITESPACE? functioninputpart)*)?;
functioninputpart   : (IDENTIFIER|NUMBER|TEXT|arg);

operation           : operator WHITESPACE? OPERAND WHITESPACE? operator;

operator            : (NUMBER|IDENTIFIER|arg);

conditional         : conditionpart WHITESPACE? CONDITION WHITESPACE? conditionpart;

conditionpart       : (NUMBER|TEXT|IDENTIFIER|arg);

arg                 : (ARG1|ARG2|ARG3|ARG4|ARG5|ARG6|ARG7|ARG8|ARG9|LARG1|LARG2|LARG3|LARG4|LARG5|LARG6|LARG7|LARG8|LARG9);



/*
 * Lexer Rules
 */

fragment A          : ('A'|'a');
fragment B          : ('B'|'b');
fragment C          : ('C'|'c');
fragment D          : ('D'|'d');
fragment E          : ('E'|'e');
fragment F          : ('F'|'f');
fragment G          : ('G'|'g');
fragment H          : ('H'|'h');
fragment I          : ('I'|'i');
fragment J          : ('J'|'j');
fragment K          : ('K'|'k');
fragment L          : ('L'|'l');
fragment M          : ('M'|'m');
fragment N          : ('N'|'n');
fragment O          : ('O'|'o');
fragment P          : ('P'|'p');
fragment Q          : ('Q'|'q');
fragment R          : ('R'|'r');
fragment S          : ('S'|'s');
fragment T          : ('T'|'t');
fragment U          : ('U'|'u');
fragment V          : ('V'|'v');
fragment W          : ('W'|'w');
fragment X          : ('X'|'x');
fragment Y          : ('Y'|'y');
fragment Z          : ('Z'|'z');

fragment DIGIT      : [0-9];

fragment LOWERCASE  : [a-z];
fragment UPPERCASE  : [A-Z];

IN                  : I N ;
OUT                 : O U T ;
TO                  : T O ;
IF                  : I F;
FOR                 : F O R;
FUN                 : F U N;

ARG1                : A R G '1';
ARG2                : A R G '2';
ARG3                : A R G '3';
ARG4                : A R G '4';
ARG5                : A R G '5';
ARG6                : A R G '6';
ARG7                : A R G '7';
ARG8                : A R G '8';
ARG9                : A R G '9';

LARG1               : L A R G '1';
LARG2               : L A R G '2';
LARG3               : L A R G '3';
LARG4               : L A R G '4';
LARG5               : L A R G '5';
LARG6               : L A R G '6';
LARG7               : L A R G '7';
LARG8               : L A R G '8';
LARG9               : L A R G '9';

STRINGVAR           : S T R ;
NUMBERVAR           : N U M ;

NUMBER              : ('-')?(DIGIT*'.'?DIGIT+|DIGIT+) ;

IDENTIFIER          : (LOWERCASE|UPPERCASE|'_')(LOWERCASE|UPPERCASE|'_'|DIGIT)*;

BACKSLASH           :'\\';

SINGLEQUOTE         : '\\\'';

DOUBLEQUOTE         : '\\"';

CONDITION           : ('=='|'!='|'<'|'>'|'<='|'>=');

OPERAND             : ('+'|'-'|'*'|'/');

TEXT                : '"'(LOWERCASE|UPPERCASE|WHITESPACE|DOUBLEQUOTE|SINGLEQUOTE|BACKSLASH|'.')+'"';

WHITESPACE          : (' ' | '\t')+;

NEWLINE             : ('\r'? '\n' | '\r')+;
