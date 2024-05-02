%{
#include <stdio.h>
#include <stdlib.h>
%}

%%
"int"           { printf("<KEYWORD, int>\n"); }
"float"         { printf("<KEYWORD, float>\n"); }
"="             { printf("<ASSIGN_OP, =>\n"); }
";"             { printf("<SEMICOLON, ;>\n"); }
"("             { printf("<LEFT_PAREN, (>\n"); }
")"             { printf("<RIGHT_PAREN, )>\n"); }
","             { printf("<COMMA, ,>\n"); }
"+"             { printf("<ADD_OP, +>\n"); }
"-"             { printf("<SUB_OP, ->\n"); }
"*"             { printf("<MUL_OP, *>\n"); }
"/"             { printf("<DIV_OP, />\n"); }
[0-9]+          { printf("<NUMBER, %s>\n", yytext); }
[a-zA-Z_][a-zA-Z0-9_]*  { printf("<IDENTIFIER, %s>\n", yytext); }
[ \t\n]         ; // Ignore whitespace and newline characters
.               { printf("Invalid character: %s\n", yytext); }
%%

int main() {
    yyin = fopen("input.txt", "r");
    if (yyin == NULL) {
        fprintf(stderr, "Error: Unable to open input file.\n");
        exit(EXIT_FAILURE);
    }
    yylex();
    fclose(yyin);
    return 0;
}

int yywrap(){
    return 1;
}
