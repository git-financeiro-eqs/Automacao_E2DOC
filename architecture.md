## Arquitetura do código

Código procedural.\
\
O código é composto por seis módulos:
- integradorE2DOC.py;
- conexaoDB.py;
- docHudson.py;
- guiLog.py;
- utils.py
- gui.py;
  
\
\
O integradorE2DOC contém uma classe responsável por estabelecer a comunicação entre a automação e o E2DOC. Ela possui como atributos as credenciais para conexão, 
e cada método dela corresponde a uma requisição POST feita à plataforma E2DOC;

O conexaoDB contém uma função que realiza a conexão da automação com o banco de dados e2doc da empresa;

O docHudson contém a função principal, o roteiro da automação. Seu fluxo de trabalho segue esse roteiro;

O guiLog é a janela de resultados que apresenta os totais enviados na ultima execução da automação;

O utils contém funções pertinentes para a execução do programa;

O gui é a interface de interação do usuário.\
\
\
\
\
(Isto é um resumo, o código é bem escrito e de fácil leitura, não havendo assim a necessidade de maior aprofundamento neste documento).
