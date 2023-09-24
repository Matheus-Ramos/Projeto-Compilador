import re 

class A_Lexico:
    
    def leitura(self):
        entrada = input()
        entrada += ' '
        #entrada.split()
        palavra = ''
        tokens = []
        for letra in range(len(entrada)):
            #entrada[letra] == ' '
            if (entrada[letra].isspace()):
                if palavra.isdigit():
                    tokens.append(('<num>', palavra))
                else:
                    tokens.append(('<str>', palavra))
                palavra = ''
            else:
                if (entrada[letra] == '_') or (entrada[letra] == ';'):
                    palavra += entrada[letra]
                if entrada[letra].isalnum():
                    palavra += entrada[letra]
        return tokens

lex = A_Lexico()
print(lex.leitura())

############### Possiveis Melhorias ###############
#contagem de linhas
#somar o valor dos numeros