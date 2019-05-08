# Read Me - Domain Specific Language
## Introduction

The goal of this project was to use a combination of ANTLR and Python to develop a transpiler that would take a Domain Specific Language(DSL) and translate it into Windows Batch script. Windows Batch script can be rather cumbersome to work with and has a very awkward syntax that sets itself apart from more modern languages and scripting options. Additionally, many simple operations, such as AND/OR boolean operations or general user input, require sophisticated workarounds in order to be utilized. This DSL has the potential to automatically implement these workarounds while providing a much simpler syntax. Additionally, this DSL could also simplify some of the more tedious or foreign elements of the Windows Batch Script with much more familiar syntax.

## Grammar Definition
The grammar is rather simple and limited in the current version. Many of the simpler operation have been modified, including:
* command execution
* variable creation
* input/output redirection
* piping
* conditional statements
* for loops
* functions

Commands are now wrapped by quotation marks with internal quotation marks having to be escaped. Variables are now initialized and modified by using two different key words to differentiate between numeric and text data. The same goes for functions that are now denoted by a keyword instead of a single symbol. Both variables and functions share the same rules on naming conventions in which it is limited to character, numbers, and underscores; Numbers cannot be the first character in an identifier. For loops are now built like they are in JAVA, similar to other languages. However, these for loops translate to IF statements paired with GOTO commands rather than Windows Batch FOR loops. If statements also appear the same way as they do in JAVA. However, when translated, the conditions are negated and a GOTO is used to skip the code block if the negation succeeds. Functions are denoted by the "fun" keyword and can be called similarly to functions in Python. However, such are the limitations of Windows Batch Script, there are no return values from the called functions. Global variables can be used to simulate return values

#### New Keywords
* **in** - replaces "<" for redirection
* **out** - replaces ">" for redirection
* **to** - replaces "|" for piping
* **fun** - replaces ":" for declaring fucntions
* **num** - replaces "set" for creating numerical variables
* **str** - replaces "set" for creating texted based variables
* **arg1-arg9** - replaces "%1" - "%9" that were used for global arguments
* **larg1-larg9** - replaces "%~1" - "%~9" that were used for local arguments for functions

#### Full Grammar
```antlr

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
```


## Code Snippets
#### Calculate the average of two numbers

**DSL**
```text
avg(arg1, arg2, average)
fun avg {
num a = larg1 + larg2
num a = a/2
"echo" a
}
```
**Windows Batch**
```shell
:: Name:	average.cmd
@echo off
SETLOCAL ENABLEEXTENSIONS ENABLEDELAYEDEXPANSION
call :avg %1,%2,%average%
@EXIT /B 0
:avg
set /a a=%~1 + %~2
set /a a=%a% / 2
echo %a%
EXIT /B 0
```
#### Print out numbers 0 to 9999
**DSL**
```text
for (num i = 0;i < 10000;i+1){
"echo" i
}
```
**Windows Batch**
```shell
:: Name:	print1000.cmd
@echo off
SETLOCAL ENABLEEXTENSIONS ENABLEDELAYEDEXPANSION
set /a i=0
:FORLOOP0
if /I NOT %i% LSS 10000 GOTO FOREND0
echo %i%
set /a i=%i% + 1
GOTO :FORLOOP0
:FOREND0
@EXIT /B 0
```

#### Chooses the largest value
**DSL**
```text
str first = "The first argument is greater"
str second = "The second argument is greater"
if(arg1 > arg2){
"echo" first
}
if(arg1 < arg2){
"echo" second
}
```
***Windows Batch**
```shell
:: Name:	choose.cmd
@echo off
SETLOCAL ENABLEEXTENSIONS ENABLEDELAYEDEXPANSION
set first="The first argument is greater"
set second="The second argument is greater"
if /I NOT %1 GTR %2 GOTO IFEND0
echo %first%
:IFEND0
if /I NOT %1 LSS %2 GOTO IFEND1
echo %second%
:IFEND1
@EXIT /B 0
```

## Current Issues
Currently there are not a lot of features that are provided by Windows Batch scripts that are not being utilized in the DSL. This would require an extensive design process using this grammar as a starting point and the refactoring of many features into more user friendly formats. Additionally, ANTLR4 has some peculiarities when dealing with recursive rules. For instance, to represent nested for loops in the grammar, it would require a rule that calls itself. However, this cause some issues with how ANTLR4 develops its parse tree. There was very little I could about this restriction as it would require some more experience to find a creative solution. Because of this restriction, the current DSL is greatly limited in its functionality.

## Compiling
To generate the Windows Batch ".cmd" files from text files that contain the DSL script, run:
```shell
python CustomScript.py <DSL-script>.txt <Batch-output>.cmd
```
