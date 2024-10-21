%{
#include <stdio.h>
int print_flag = 0;
%}

%%
"//".*			{ printf("COMMENT\n"); }
"f"			{ printf("floatdcl "); print_flag = 1; }
"i"			{ printf("intdcl "); print_flag = 1; }
"p"			{ printf("print "); print_flag = 1; }
[a-zA-z][a-zA-Z0-9]*	{ printf("id "); if (print_flag) {printf("\n"); print_flag = 0; } }
"="			{ printf("assign "); }
[0-9]+			{ printf("inum\n"); }
[0-9]+\.[0-9]+		{ printf("fnum\n"); }
"+"			{ printf("plus "); }
"-"			{ printf("minus "); }
"*"			{ printf("mult "); }
"/"			{ printf("div "); }
\n			{ /* Ignore new lines */ }
[ \t]+			{ /* Ignore whitespace */ }
.			{ printf("Error: Unrecognized character: %s\n", yytext); }
%%

int main(int argc, char **argv) {
	if (argc > 1) {
		FILE *file = fopen(argv[1], "r");
		if (!file) {
			printf("Error opening file %s\n", argv[1]);
			return 1;
		}
		yyin = file;
		yylex();
		fclose(file);
		}
	return 0;
}
