## Visão Geral da Arquitetura – Automação E2DOC
<br/>
<br/>
Arquitetura procedural modular.<br/>

Este documento descreve a arquitetura modular do projeto Automação E2DOC, detalhando os papéis e responsabilidades de cada módulo. O objetivo é garantir que o código seja fácil de entender, manter e expandir.
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
      <td><strong>integradorE2DOC</strong></td>
      <td>Classe que estabelece comunicação com o E2DOC via API. Cada método corresponde a uma requisição POST.</td>
      <td>Comunicação com a API E2DOC, autenticação e envio de dados.</td>
    </tr>
    <tr>
      <td><strong>conexaoDB</strong></td>
      <td>Função que realiza a conexão com o banco de dados da empresa para busca de informações do colaborador.</td>
      <td>Conexão segura com o banco de dados.</td>
    </tr>
    <tr>
      <td><strong>docHudson</strong></td>
      <td>Contém a função principal e o roteiro da automação.</td>
      <td>Fluxo de trabalho da automação.</td>
    </tr>
    <tr>
      <td><strong>guiLog</strong></td>
      <td>Interface de resultado que exibe o log da execução, apresentando os totais enviados.</td>
      <td>Apresentar resultados ao usuário.</td>
    </tr>
    <tr>
      <td><strong>utils</strong></td>
      <td>Funções auxiliares que suportam a execução do programa.</td>
      <td>Operações utilitárias, manipulação de strings, validações.</td>
    </tr>
    <tr>
      <td><strong>gui</strong></td>
      <td>Interface gráfica principal, permitindo interação do usuário para seleção de arquivos e execução da automação.</td>
      <td>Interface de interação com o usuário (Tkinter).</td>
    </tr>
  </tbody>
</table>
<br/>
<br/>
O fluxo principal do programa ocorre no módulo docHudson.py, que coordena a execução da automação. Ele utiliza:<br/>
<br/>

- gui.py para obter os arquivos lote selecionados pelo usuário.
- utils.py para manipulações necessárias no processo.
- conexaoDB.py para buscar dados no banco da empresa.
- integradorE2DOC.py para enviar os dados e arquivos para o E2DOC via API. Após a conclusão, os resultados são exibidos ao usuário pelo guiLog.py.
<br/>
<br/>

## Fluxos Alternativos
Exceções e cenários específicos:
<br/>
O sistema foi pensado para capturar tipos de pagamento incorretos, que não correspondem a nenhum indice de classificação, e CPFs errados. Esses dados são apresentados no relatório que a própria automação envia para o E-mail.

Os comprovantes do tipo folha tem uma particularidade no seu envio para o E2DOC. No formulário do E2DOC é preciso informar a competência daquele pagamento. Todos os pagamentos tem como competência o mês vigente, menos os comprovantes do tipo folha. Esses comprovantes tem como competência sempre o mês anterior ao de geração do documento.

"Se o nome do arquivo não corresponder ao padrão, ele será movido para a pasta 'Não Processados' e o log será atualizado."
<br/>
<br/>
(Isto é um resumo, o código é bem escrito e de fácil leitura, não havendo assim a necessidade de maior aprofundamento neste documento).
