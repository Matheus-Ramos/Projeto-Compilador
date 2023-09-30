import re 

class A_Lexico:
    
    def ehDigito(self, palavra):
        if palavra.isdigit():
            return '<num>'
        else:
            return '<str>'
            
    def leitura(self):
        entrada = input()
        entrada += ' '
        #entrada.split()
        palavra = ''
        tokens = []
        for letra in range(len(entrada)):
            #entrada[letra] == ' '
            if (entrada[letra].isspace()):
                tokens.append((self.ehDigito(palavra), palavra))
                palavra = ''
            else:
                if (entrada[letra] == ';'):
                    if (entrada[letra-1].isspace()) and (entrada[letra+1].isspace()):
                        palavra += entrada[letra]
                    elif (not(entrada[letra-1].isspace())) and (not(entrada[letra+1].isspace())):
                        tokens.append((self.ehDigito(palavra), palavra))
                        tokens.append((self.ehDigito(';'), ';'))
                        palavra = ''
                    elif (not(entrada[letra-1].isspace())):
                        tokens.append((self.ehDigito(palavra), palavra))
                        palavra = ''
                        palavra += entrada[letra]
                    elif (not(entrada[letra+1].isspace())):
                        tokens.append((self.ehDigito(';'), ';'))
                        palavra = ''
                if (entrada[letra] == '_') or (entrada[letra].isalnum()):
                    palavra += entrada[letra]
        return tokens
    
    def transformacaoNumerica(self, tokens):
        tokens_transformados = []
        for index in range(len(tokens)):
            tag, palavra = tokens[index]
            if (tag == '<num>'):
                tokens_transformados.append((tag, int(palavra)))
            else:
                tokens_transformados.append((tag, palavra))
        return tokens_transformados

    def transformacaoTag(self, tokens):
        tokens_transformados = []
        for index in range(len(tokens)):
            if (not(tokens[index-1][1] == 'sem' and tokens[index][1] == 'limite')):    
                tag, palavra = tokens[index]
                if (palavra == 'loop'):
                    tag = '<loop>'
                elif (palavra == 'navegador'):
                    tag = '<navegador>'
                elif (palavra == ';'):
                    tag = '<;>'
                elif (palavra == 'sem' and tokens[index+1][1] == 'limite'):
                    tag = '<sem limite>'
                    palavra = 'sem limite'
                tokens_transformados.append((tag, palavra))
        return tokens_transformados

    def lexico(self):
        tokens = self.leitura()
        #print(tokens)
        tokens_transformados = self.transformacaoNumerica(tokens)
        #print(tokens_transformados)
        novos_tokens = self.transformacaoTag(tokens_transformados)
        #print(novos_tokens)
        return novos_tokens
    

############### Possiveis Melhorias ###############
#contagem de linhas
#somar o valor dos numeros >>implementado
#melhorar classificação dos tokens >>implementado