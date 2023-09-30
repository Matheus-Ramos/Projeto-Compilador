import AnalizadorLexico as alx
import AnalizadorSintatico as ast

lex = alx.A_Lexico()
tokens = lex.lexico()

sin = ast.A_Sintatico()
sin.sintatico(tokens)