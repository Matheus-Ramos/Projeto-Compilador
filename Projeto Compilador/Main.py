import AnalizadorLexico as alx
import AnalizadorSintatico as ast
from flask import Flask, render_template, request, jsonify, send_from_directory

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
        data = request.get_json()  # Obter dados JSON da solicitação

        # Faz o processamento dos dados aqui
        lex = alx.A_Lexico()
        tokens = lex.lexico(data) # Inicia a análise léxica.
        
        parser = ast.A_Sintatico(tokens)

        results = "Léxico: \n" + "\n".join([str(token).replace('<', '&lt;').replace('>', '&gt;') for token in tokens])
        results += "\nSintático:\n"  + str(parser.parse()) # Inicia a análise sintática.

        # Retorno com quebra de linha para o front end

        return jsonify(results.replace("\n", "<br>"))
    
    except Exception as e:
        print("-------------------Exception")
        return jsonify(str(e))  # Responder com um erro se a análise do JSON falhar


if __name__ == '__main__':
    app.run(debug=True)