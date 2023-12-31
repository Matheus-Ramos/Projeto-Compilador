import AnalizadorLexico as alx
import AnalizadorSintatico as ast
from flask import Flask, render_template, request
import os

app = Flask(__name__)

simbolosTerminais = ['loop', 1, 2, 3, 4, 5, '15_min', '20_min', '1_hora', '1_dia', '2_dias', 'sem limite', 'navegador', ';']
simbolosNTerminais = ['programa_SOL', 'vezes', 'sequência', 'Present', 'tempo', 
                      'fases_EPIC', 'Explore', 'Interact', 'Critique', 'navegar',
                      'visualizar_pdf', 'visualizar_vídeo', 'videoconferência',
                      'whatsapp_web', 'email', 'browser', 'link_pdf', 'link_video',
                      'link_videoconferencia', 'link_whatsapp_web', 'link_email']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/receber-dados', methods=['POST'])
def receber_dados():
    try:
        os.system('cls')
        data = request.data.decode("utf-8") # Obter dados da solicitação
        # Faz o processamento dos dados aqui
        lex = alx.A_Lexico()
        tokens = lex.lexico(data) # Inicia a análise léxica.
        parser = ast.A_Sintatico(tokens)


        results = "Léxico: \n" + "".join([str(token).replace('<', '&lt;').replace('>', '&gt;')+"\n" for token in tokens])
        results += "\nSintático:\n" + parser.parse() # Inicia a análise sintática.

        # Retorno com quebra de linha para o front end
        return results.replace("\n", "<br>")
    
    except Exception as e:
        results = "Léxico: \n" + "".join([str(token).replace('<', '&lt;').replace('>', '&gt;')+"\n" for token in tokens])
        results += str(e)
        return results.replace("\n", "<br>")

if __name__ == '__main__':
    app.run(debug=True)