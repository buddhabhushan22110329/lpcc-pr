%{
#include <stdio.h>
%}

%option noyywrap

%%


noun        [A-Za-z]+
verb        \b(runs?|ran|running)\b
adjective   \b(dreadful|same)\b
adverb      \b(from|all)\b
punctuation [.,;!?]

{noun}        { printf("<NOUN> %s\n", yytext); }
{verb}        { printf("<VERB> %s\n", yytext); }
{adjective}   { printf("<ADJECTIVE> %s\n", yytext); }
{adverb}      { printf("<ADVERB> %s\n", yytext); }
{punctuation} { printf("<PUNCTUATION> %s\n", yytext); }
.             { /* Ignore other characters */ }

%%

int main() {
    // Set input to the text string
    yy_scan_string("Dread it. Run from it. Destiny arrives all the same.");

    // Call the lexer
    yylex();

    return 0;
}