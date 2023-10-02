import time
from selenium import webdriver

class A_Sintatico:
    
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.chrome = None

    def erro_sintatico(self):
        raise SyntaxError(f"Erro sintático: Token inesperado {self.tokens[self.pos]}")

    def match(self, esperado):
        if self.pos < len(self.tokens) and self.tokens[self.pos][1] == esperado:
            self.pos += 1
        else:
            self.erro_sintatico()

    def programa_SOL(self):
        self.match('programa_SOL')
        self.match('loop')
        vezes = self.vezes()
        for _ in range(vezes):
            self.sequencia()

    def vezes(self):
        if self.tokens[self.pos][0] == '<num>':
            num = int(self.tokens[self.pos][1])
            self.match(self.tokens[self.pos][1])
            return num
        elif self.tokens[self.pos][1] in ['1', '2', '3', '4', '5']:
            num = int(self.tokens[self.pos][1])
            self.match(self.tokens[self.pos][1])
            return num
        else:
            self.erro_sintatico()

    def sequencia(self):
        if self.verifica_sequencia():
            self.fases_EPIC()
        else:
            self.Present()

    def fases_EPIC(self):
        if self.tokens[self.pos][1] == 'fases_EPIC':
            self.match('fases_EPIC')
        self.Explore()
        self.Present()
        self.Interact()
        self.Critique()

    def Explore(self):
        self.navegar()
        if self.tokens[self.pos][1] == 'Explore':
            self.match('Explore')
        tempo = self.tempo()
        if tempo is not None:
            if tempo == float('inf'):
                input("Pressione Enter para fechar o Chrome...")
            else:
                time.sleep(tempo)
        self.match(';')
        self.fechar_navegador()

    def Present(self):
        if self.tokens[self.pos][1] == 'Present':
            self.match('Present')
        choice = self.tokens[self.pos][1]
        if choice == 'visualizar_pdf':
            self.match(choice)
            self.visualizar_pdf()
        elif choice == 'visualizar_vídeo':
            self.match(choice)
            self.visualizar_video()
        elif choice == 'videoconferência':
            self.match(choice)
            self.videoconferencia()
        elif choice == 'navegador':
            self.browser()
            if self.tokens[self.pos][1] == 'link_pdf':
                self.match("link_pdf")
                self.link_pdf()
            elif self.tokens[self.pos][1] == 'link_video':
                self.match("link_video")
                self.link_video()
            elif self.tokens[self.pos][1] == 'link_videoconferencia':
                self.match("link_videoconferencia")
                self.link_videoconferencia()
        else:
            self.erro_sintatico()
        tempo = self.tempo()
        if tempo is not None:
            if tempo == float('inf'):
                input("Pressione Enter para fechar o Chrome...")
            else:
                time.sleep(tempo)
        self.match(';')
        self.fechar_navegador()

    def Interact(self):
        if self.tokens[self.pos][1] == 'Interact':
            self.match('Interact')
        choice = self.tokens[self.pos][1]
        if choice == 'whatsapp_web':
            self.match(choice)
            self.whatsapp_web()
        elif choice == 'email':
            self.match(choice)
            self.email()
        elif choice == 'videoconferência':
            self.match(choice)
            self.videoconferencia()
        elif choice == 'navegador':
            self.browser()
            if self.tokens[self.pos][1] == 'link_whatsapp_web':
                self.match('link_whatsapp_web')
                self.link_whatsapp_web()
            elif self.tokens[self.pos][1] == 'link_email':
                self.match('link_email')
                self.link_email()
            elif self.tokens[self.pos][1] == 'link_videoconferencia':
                self.match('link_videoconferencia')
                self.link_videoconferencia()
        else:
            self.erro_sintatico()
        tempo = self.tempo()
        if tempo is not None:
            if tempo == float('inf'):
                input("Pressione Enter para fechar o Chrome...")
            else:
                time.sleep(tempo)
        self.match(';')
        self.fechar_navegador()

    def Critique(self):
        if self.tokens[self.pos][1] == 'Critique':
            self.match('Critique')
        choice = self.tokens[self.pos][1]
        if choice == 'whatsapp_web':
            self.match(choice)
            self.whatsapp_web()
        elif choice == 'email':
            self.match(choice)
            self.email()
        elif choice == 'videoconferência':
            self.match(choice)
            self.videoconferencia()
        elif choice == 'navegador':
            self.browser()
            if self.tokens[self.pos][1] == 'link_whatsapp_web':
                self.match('link_whatsapp_web')
                self.link_whatsapp_web()
            elif self.tokens[self.pos][1] == 'link_email':
                self.match('link_email')
                self.link_email()
            elif self.tokens[self.pos][1] == 'link_videoconferencia':
                self.match('link_videoconferencia')
                self.link_videoconferencia()
        else:
            self.erro_sintatico()
        tempo = self.tempo()
        if tempo is not None:
            if tempo == float('inf'):
                input("Pressione Enter para fechar o Chrome...")
            else:
                time.sleep(tempo)
        self.match(';')
        self.fechar_navegador()

    def tempo(self):
        if self.tokens[self.pos][1] == 'tempo':
            self.match('tempo')
        tempo = self.tokens[self.pos][1]
        if tempo == '15_min':
            self.match('15_min')
            return 15 * 60
        elif tempo == '20_min':
            self.match('20_min')
            return 20 * 60
        elif tempo == '1_hora':
            self.match('1_hora')
            return 60 * 60
        elif tempo == '1_dia':
            self.match('1_dia')
            return 24 * 60 * 60
        elif tempo == '2_dias':
            self.match('2_dias')
            return 2 * 24 * 60 * 60
        elif tempo == 'sem limite':
            self.match('sem limite')
            return float('inf')  # Nenhum limite de tempo
        elif tempo == 'sem_limite':
            self.match('sem_limite')
            return float('inf')  # Nenhum limite de tempo
        else:
            self.erro_sintatico()

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
        self.link_whatsapp_web()

    def email(self):
        self.browser()
        self.link_email()

    def browser(self):
        self.match('navegador')
        self.chrome = webdriver.Chrome()
        self.chrome.get('https://google.com')

    def link_pdf(self):
        if self.chrome is None:
            self.erro_sintatico()
        
        caminho_pdf = 'Projeto Compilador\Programas de Teste.pdf'
        self.chrome.get(caminho_pdf)

    def link_video(self):
        if self.chrome is None:
            self.erro_sintatico()

        self.chrome.get('https://youtube.com')

    def link_videoconferencia(self):
        if self.chrome is None:
            self.erro_sintatico()

        self.chrome.get('https://meet.google.com')

    def link_whatsapp_web(self):
        if self.chrome is None:
            self.erro_sintatico()

        self.chrome.get('https://web.whatsapp.com')

    def link_email(self):
        if self.chrome is None:
            self.erro_sintatico()

        self.chrome.get('https://gmail.com')

    def fechar_navegador(self):
        if self.chrome:
            self.chrome.quit()
            self.chrome = None
            
    def verifica_sequencia(self):
        i = self.pos
        while i < len(self.tokens):
            token = self.tokens[i][1]
            if token == ';':
                if i == len(self.tokens) - 1:
                    return False
                else:
                    return True
            i += 1
        return True

    def parse(self):
        try:
            self.programa_SOL()
            if self.pos == len(self.tokens):
                print("Análise sintática bem-sucedida.")
            else:
                self.erro_sintatico()
        except SyntaxError as e:
            print(str(e))