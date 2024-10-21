all: lex_analyzer

lex_analyzer: lex_analyzer.l
	flex lex_analyzer.l
	gcc -o lex_analyzer lex.yy.c -lfl

clean:
	rm -f lex_analyzer lex.yy.c
