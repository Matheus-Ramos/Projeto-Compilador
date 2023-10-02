# Projeto-Compilador
Esse compilador contém apenas análise léxica e sintática.


## Como executar o compilador:
Certifique-se que a máquina possui o python instalado
instale:
- '''pip install selenium'''
- '''pip install flask'''
Faça o build da aplicação e rode.
Abra no navegador o servidor orientado pelo console.


TESTES:
    SUCEDIDOS:
        programa_SOL loop 1 navegador sem limite ;
        programa_SOL loop 1 videoconferência navegador sem limite ;

    NãoSUCEDIDOS:
        programa_SOL loop 1 navegador sem limite
        programa_SOL loop 1 videoconferência sem limite ;

    NãoTESTADO
        programa_SOL loop 2 navegador sem limite; navegador videoconferência sem limite;