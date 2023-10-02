document.getElementById('inputCod').addEventListener('submit', function (e) {
    e.preventDefault();

    const textCod = document.getElementById('textCod').value;

    const dados = {
        mensagem: textCod
    };

    fetch('/api/receber-dados', {
        method: 'POST', 
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(textCod)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('resposta').innerHTML = data;
    })
    .catch(error => {
        console.error('Erro:', error);
    });
});