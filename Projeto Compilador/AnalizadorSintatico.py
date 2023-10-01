from selenium import webdriver
from whatsapp_api import WhatsApp

class A_Sintatico:
    
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0  # Variável para rastrear a posição atual na lista de tokens.

    def match(self, expected_tag):
        # Função para verificar se o token atual é igual à tag esperada.
        if self.index < len(self.tokens) and self.tokens[self.index][0] == expected_tag:
            self.index += 1  # Avança para o próximo token.
        else:
            raise SyntaxError(f"Erro de sintaxe: Esperava '{expected_tag}', mas obteve '{self.tokens[self.index][0]}'")

    def programa_SOL(self):
        self.index += 1
        self.match('<loop>')  # Espera que o primeiro token seja '<loop>'.
        self.vezes()  # Chama a função vezes() para processar o número de vezes.
        self.sequencia()  # Chama a função sequencia() para processar a sequência.

    def vezes(self):
        if self.tokens[self.index][1] in [1, 2, 3, 4, 5]:
            self.match(self.tokens[self.index][0])  # Verifica se o token é um número de vezes válido.
        else:
            raise SyntaxError("Erro de sintaxe: Esperava um número de vezes válido")

    def sequencia(self):
        self.Present()  # Chama a função Present() para processar a parte 'Present'.
        self.tempo()  # Chama a função tempo() para processar o tempo.
        while self.tokens[self.index][0] == 'navegador':
            self.match('navegador')  # Verifica se há um navegador.
            self.tempo()  # Chama a função tempo() novamente para processar o tempo.
            self.match(';')  # Verifica se há um ponto e vírgula no final.
    
    def fases_EPIC(self):
        pass
    
    def Explore(self):
        pass
    
    def Present(self):
        pass
    
    def Interact(self):
        pass
    
    def Critique(self):
        pass
    
    def navegar(self):
        self.browser()
    
    def visualizar_pdf(self):
        self.browser()
        self.link_pdf()
    
    def visualizar_video(self):
        self.browser()
        self.link_video()
    
    def videoconferencia(self):
        self.browser()
        self.link_videoconferencia()
    
    def whatsapp_web(self):
        self.browser()
        self.link_whatsapp_web
    
    def email(self):
        self.browser()
        self.link_email()
    
    def browser(self):
        self.match('navegador')
        chrome = webdriver.Chrome()
        chrome.get('https://google.com')
    
    def link_pdf(self):
        pass
    
    def link_video(self):
        pass
    
    def link_videoconferencia(self):
        pass
    
    def link_whatsapp_web(self):
        #wp = WhatsApp()
        pass
    
    def link_email(self):
        pass

    def tempo(self):
        if self.tokens[self.index][1] in ['20_min', '1_hora', '1_dia', '2_dias', 'sem limite', '15_min']:
            self.match(self.tokens[self.index][0])  # Verifica se o token é um valor de tempo válido.
        else:
            raise SyntaxError("Erro de sintaxe: Esperava um valor de tempo válido")

    def parse(self):
        try:
            self.programa_SOL()  # Inicia a análise sintática a partir do programa_SOL.
            if self.index == len(self.tokens):
                print("Análise sintática bem-sucedida")  # Se todos os tokens foram processados com sucesso.
            else:
                raise SyntaxError("Erro de sintaxe: Tokens extras após o programa")  # Tokens extras não processados.
        except SyntaxError as e:
            print(e)