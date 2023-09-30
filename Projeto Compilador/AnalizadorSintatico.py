class A_Sintatico:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def erro_sintatico(self):
        raise SyntaxError(f"Erro sintático: Token inesperado {self.tokens[self.pos]}")

    def match(self, esperado):
        if self.pos < len(self.tokens) and self.tokens[self.pos][1] == esperado:
            self.pos += 1
        else:
            self.erro_sintatico()

    def programa_SOL(self):
        self.match('loop')
        self.vezes()
        self.sequencia()

    def vezes(self):
        if self.tokens[self.pos][0] == '<num>':
            self.match(self.tokens[self.pos][1])
        elif self.tokens[self.pos][1] in ['1', '2', '3', '4', '5']:
            self.match(self.tokens[self.pos][1])
        else:
            print("teste")
        

    def sequencia(self):
        if self.tokens[self.pos][1] == 'Present':
            self.match('Present')
            self.Present()
        elif self.tokens[self.pos][1] == 'fases_EPIC':
            self.fases_EPIC()
        else:
            self.erro_sintatico()

    def fases_EPIC(self):
        self.match('Explore')
        self.Explore()
        self.match('Present')
        self.Present()
        self.match('Interact')
        self.Interact()
        self.match('Critique')
        self.Critique()
        
    def Explore(self):
        self.match('navegar')
        self.tempo()
        self.match(';')

    def Present(self):
        choice = self.tokens[self.pos][1]
        if choice in ['visualizar_pdf', 'visualizar_vídeo', 'videoconferência']:
            self.match(choice)
            self.tempo()
            self.match(';')
        else:
            self.erro_sintatico()

    def Interact(self):
        choice = self.tokens[self.pos][1]
        if choice in ['whatsapp_web', 'email', 'videoconferência']:
            self.match(choice)
            self.tempo()
            self.match(';')
        else:
            self.erro_sintatico()

    def Critique(self):
        choice = self.tokens[self.pos][1]
        if choice in ['whatsapp_web', 'email', 'videoconferência']:
            self.match(choice)
            self.tempo()
            self.match(';')
        else:
            self.erro_sintatico()

    def tempo(self):
        if self.tokens[self.pos][1] in ['15_min', '20_min', '1_hora', '1_dia', '2_dias', 'sem limite']:
            self.match(self.tokens[self.pos][1])
        else:
            self.erro_sintatico()

    def parse(self):
        try:
            self.programa_SOL()
            if self.pos == len(self.tokens):
                print("Análise sintática bem-sucedida.")
            else:
                self.erro_sintatico()
        except SyntaxError as e:
            print(str(e))
