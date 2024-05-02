%{
#include "calc.tab.h"  // Include Bison-generated header for YYSTYPE and token types
%}

%%

[0-9]+(\.[0-9]+)? {
    yylval.val = atof(yytext);  // Assign the atof result to the union member 'val'
    return NUMBER;
}

[ \t]+ ;  // Ignore spaces and tabs
\n      { return 0; }  // Return 0 on a newline to signal the end of input
.       { return yytext[0]; }  // Return any other character as itself

%%

int yywrap() {
    return 1;
}