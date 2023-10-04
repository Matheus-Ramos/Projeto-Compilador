document.getElementById('inputCod').addEventListener('submit', function (e) {
    e.preventDefault();

    const textCod = document.getElementById('textCod').value;

    const dados = {
        mensagem: textCod
    };

    fetch('/api/receber-dados', {
        method: 'POST',
        body: dados.mensagem
    })
    .then(response => response.text())
    .then(data => {
        document.getElementById('resposta').innerHTML = data;
    })
    .catch(error => {
        console.error('Erro:', error);
    });
});