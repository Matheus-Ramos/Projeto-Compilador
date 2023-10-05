let inputCodForm = document.getElementById('inputCod');
let consoleDiv = document.createElement('div');
consoleDiv.classList = 'console';
let respostaSpan = document.createElement('span');
respostaSpan.classList = 'resposta';
consoleDiv.appendChild(respostaSpan);


inputCodForm.addEventListener('submit', function (e) {
    e.preventDefault();

    const textCod = document.getElementById('textCod').value;
    
    consoleDiv.remove();
    let tempSpan = document.createElement('span');
    tempSpan.innerHTML = "AGUARDE!";
    inputCodForm.after(tempSpan);
    

    const dados = {
        mensagem: textCod
    };
    fetch('/api/receber-dados', {
        method: 'POST',
        body: dados.mensagem
    })
    .then(response => response.text())
    .then(data => {
        tempSpan.remove();
        respostaSpan.innerHTML = data;
        inputCodForm.after(consoleDiv);
    })
    .catch(error => {
        console.error('Erro:', error);
    });
});