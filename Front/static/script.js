document.getElementById('inputCod').addEventListener('submit', function (e) {
    e.preventDefault();

    const textCod = document.getElementById('textCod').value;

    const dados = {
        mensagem: textCod
    };

    fetch('http://127.0.0.1:5000/api/receber-dados', {
        method: 'POST', 
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(dados)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('resposta').innerHTML = data.mensagem;
    })
    .catch(error => {
        console.error('Erro:', error);
    });
});