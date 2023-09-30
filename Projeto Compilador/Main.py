from AnalizadorLexico import A_Lexico
from AnalizadorSintatico import A_Sintatico

lex = A_Lexico()
tokens = lex.lexico()

parser = A_Sintatico(tokens)
parser.parse()