## Visão Geral da Arquitetura – Automação E2DOC

Arquitetura procedural modular.\
Este documento descreve a arquitetura modular do projeto E2DOC, detalhando os papéis e responsabilidades de cada módulo. O objetivo é garantir que o código seja fácil de entender, manter e expandir.
<br/>
<br/>
<br/>
O código é composto por seis módulos:
- integradorE2DOC.py;
- conexaoDB.py;
- docHudson.py;
- guiLog.py;
- utils.py
- gui.py;
<br/>
<br/>
<br/>
| Módulo            | Descrição                                                                 | Principais Responsabilidades                                    |
| ----------------- | ------------------------------------------------------------------------- | --------------------------------------------------------------- |
| integradorE2DOC.py | Classe que estabelece comunicação com o E2DOC via API. Cada método corresponde a uma requisição POST. | Comunicação com a API E2DOC, autenticação e envio de dados.     |
| conexaoDB.py      | Função que realiza a conexão com o banco de dados da empresa para busca de informações do colaborador. | Conexão segura com o banco de dados.                             |
| docHudson.py      | Contém a função principal e o roteiro da automação.                      | Fluxo de trabalho da automação.                                  |
| guiLog.py         | Interface de resultado que exibe o log da execução, apresentando os totais enviados. | Apresentar resultados ao usuário.                                |
| utils.py          | Funções auxiliares que suportam a execução do programa.                  | Operações utilitárias, manipulação de strings, validações.       |
| gui.py            | Interface gráfica principal, permitindo interação do usuário para seleção de arquivos e execução da automação. | Interface de interação com o usuário (Tkinter).                  |

<br/>
<br/>
<br/>
<br/>
(Isto é um resumo, o código é bem escrito e de fácil leitura, não havendo assim a necessidade de maior aprofundamento neste documento).
