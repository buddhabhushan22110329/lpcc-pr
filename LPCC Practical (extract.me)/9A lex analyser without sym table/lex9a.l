%{
#include <stdio.h>
%}

%%

"int"           { printf("<KEYWORD, int>\n"); }
"="             { printf("<ASSIGN_OP, =>\n"); }
";"             { printf("<SEMICOLON, ;>\n"); }
"("             { printf("<LEFT_PAREN, (>\n"); }
")"             { printf("<RIGHT_PAREN, )>\n"); }
"{"             { printf("<LEFT_BRACE, {>\n"); }
"}"             { printf("<RIGHT_BRACE, }>\n"); }
"-"             { printf("<SUB_OP, ->\n"); }
[0-9]+          { printf("<NUMBER, %s>\n", yytext); }
[a-zA-Z_][a-zA-Z0-9_]*  { printf("<IDENTIFIER, %s>\n", yytext); }
[ \t\n]         ; // Ignore whitespace and newline characters
.               { printf("Invalid character: %s\n", yytext); }

%%

int main() {
    yyin = fopen("input.txt", "r");
    yylex();
    fclose(yyin);
    return 0;
}

int yywrap() {
    return 1;
}
