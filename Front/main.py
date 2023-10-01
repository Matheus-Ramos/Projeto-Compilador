from flask import Flask, render_template, request, jsonify, send_from_directory

app = Flask(__name__)

@app.route('/')
def homees():
    return render_template('index.html')

@app.route('/api/receber-dados', methods=['POST'])
def receber_dados():
    try:
        data = request.get_json()  # Obter dados JSON da solicitação
        # Faça o processamento dos dados aqui
        #print(jsonify(data))
        return jsonify(data)
    except Exception as e:
        print("-------------------Exception")
        return jsonify({'error': str(e)}), 400  # Responder com um erro se a análise do JSON falhar

if __name__ == '__main__':
    app.run(debug=True)