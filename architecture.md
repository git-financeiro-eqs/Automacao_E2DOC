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
<table>
  <thead>
    <tr>
      <th>Módulo</th>
      <th>Descrição</th>
      <th>Principais Responsabilidades</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>integradorE2DOC.py</strong></td>
      <td>Classe que estabelece comunicação com o E2DOC via API. Cada método corresponde a uma requisição POST.</td>
      <td>Comunicação com a API E2DOC, autenticação e envio de dados.</td>
    </tr>
    <tr>
      <td><strong>conexaoDB.py</strong></td>
      <td>Função que realiza a conexão com o banco de dados da empresa para busca de informações do colaborador.</td>
      <td>Conexão segura com o banco de dados.</td>
    </tr>
    <tr>
      <td><strong>docHudson.py</strong></td>
      <td>Contém a função principal e o roteiro da automação.</td>
      <td>Fluxo de trabalho da automação.</td>
    </tr>
    <tr>
      <td><strong>guiLog.py</strong></td>
      <td>Interface de resultado que exibe o log da execução, apresentando os totais enviados.</td>
      <td>Apresentar resultados ao usuário.</td>
    </tr>
    <tr>
      <td><strong>utils.py</strong></td>
      <td>Funções auxiliares que suportam a execução do programa.</td>
      <td>Operações utilitárias, manipulação de strings, validações.</td>
    </tr>
    <tr>
      <td><strong>gui.py</strong></td>
      <td>Interface gráfica principal, permitindo interação do usuário para seleção de arquivos e execução da automação.</td>
      <td>Interface de interação com o usuário (Tkinter).</td>
    </tr>
  </tbody>
</table>
<br/>
<br/>
<br/>
<br/>
(Isto é um resumo, o código é bem escrito e de fácil leitura, não havendo assim a necessidade de maior aprofundamento neste documento).
