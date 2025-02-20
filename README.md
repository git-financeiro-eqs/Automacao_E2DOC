# Automação E2DOC

Este projeto automatiza o processo manual de integração de comprovantes financeiros na plataforma E2DOC. A automação conta com uma interface para interação do usuário, 
e faz conexão com o E2DOC através de sua API.

O objetivo dessa automação é alimentar a plataforma E2DOC com os comprovantes de pagamento feitos isoladamente no portal de um banco determinado. 
Em detalhes, o que ocorre é que a maioria dos pagamentos feitos pelo setor financeiro são realizados de forma automática pelo sistema ERP da empresa, 
mas, existem os casos onde, devido a uma falha no processo, o título de pagamento não pode ser efetivado pelas vias comuns, implicando que seu pagamento seja feito de forma manual, direto no portal do banco.
Esses comprovantes "manuais" precisam estar disponíveis para consulta do setor jurídico na plataforma E2DOC. Ao contrário dos comprovantes pagos pelo sistema ERP, - que alimentam a plataforma automaticamente devido uma integração que há entre o ERP e o E2DOC - os comprovantes manuais não são integrados automaticamente à plataforma, fazendo com que seja necessário a ação de um operador para separar esse documento do arquivo lote de comprovantes extraídos da plataforma do banco, e, fazer a sua integração manual, alimentando uma pasta processual compartilhada na nuvem e preenchendo um formulário com os dados do documento no E2DOC, fazendo assim sua indexação.

Na interface de interação, o usuário irá clicar em um botão que o permitirá selecionar o, ou, os arquivos lote desejados. 
O caminho desses arquivos lote é armazenado em uma lista, que será percorrida pela automação. Antigamente, o usuário separava comprovante por comprovante pela sua natureza, pelo seu tipo de pagamento, por exemplo: pagamento de VA, VT, salário, férias, e etc...
Existe uma lista de processos que podem ocorrer pagamento manual, todos mapeados nessa automação, e, cada tipo de natureza de pagamento tem uma pasta final correspondente na nuvem, onde o comprovante deve ser salvo isolado dos demais comprovantes, tendo como título do arquivo apenas o nome completo do colaborador para o qual se destinou aquele pagamento.
Através de uma informação complementar distinta inserida no comprovante "manual" - convencionada em reuniões de levantamento de requisitos onde determinou-se a criação de uma chave de identificação - faz-se então a distinção dos comprovantes. Essa chave obedece a seguinte estrutura: 

Nomenclatura para os comprovantes manuais: 
 
Será seguido da seguinte maneira: CHAVE CPF + SIGLA  
Com exceção dos VAs e VTs, que terá o acréscimo do pedido no final da chave: CHAVE CPF + SIGLA + PEDIDO
<br/>
<br/>
<table>
  <thead>
    <tr>
      <th>TIPO COMP</th>
      <th>SIGLA</th>
      <th>CHAVE-EXEMPLO</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Locação veículo</td>
      <td>LOC</td>
      <td>CHAVE 00000000000LOC</td>
    </tr>
    <tr>
      <td>VT</td>
      <td>VAT</td>
      <td>CHAVE 00000000000VATPEDIDO</td>
    </tr>
    <tr>
      <td>VA</td>
      <td>VAR</td>
      <td>CHAVE 00000000000VARPEDIDO</td>
    </tr>
    <tr>
      <td>Folha geral</td>
      <td>FOL</td>
      <td>CHAVE 00000000000FOL</td>
    </tr>
    <tr>
      <td>Adto Revap</td>
      <td>ARV</td>
      <td>CHAVE 00000000000ARV</td>
    </tr>
    <tr>
      <td>Adto Repar</td>
      <td>ARP</td>
      <td>CHAVE 00000000000ARP</td>
    </tr>
    <tr>
      <td>Adto 13º</td>
      <td>13A</td>
      <td>CHAVE 0000000000013A</td>
    </tr>
    <tr>
      <td>13º - 1ª Parcela</td>
      <td>131</td>
      <td>CHAVE 00000000000131</td>
    </tr>
    <tr>
      <td>13º - 2ª Parcela</td>
      <td>132</td>
      <td>CHAVE 00000000000132</td>
    </tr>
    <tr>
      <td>13º - Tribunal de Justiça</td>
      <td>13T</td>
      <td>CHAVE 0000000000013T</td>
    </tr>
    <tr>
      <td>Rescisão</td>
      <td>RES</td>
      <td>CHAVE 00000000000RES</td>
    </tr>
    <tr>
      <td>Férias</td>
      <td>FER</td>
      <td>CHAVE 00000000000FER</td>
    </tr>
    <tr>
      <td>Multa FGTS</td>
      <td>FGT</td>
      <td>CHAVE 00000000000FGT</td>
    </tr>
  </tbody>
</table>
<br/>

A automação irá ler cada comprovante do arquivo lote, separar aquele pago manualmente, coletar o CPF do colaborador, destiná-lo a sua pasta processual final, e, através do CPF, buscar os dados pertinentes ao preenchimento do formulário do E2DOC direto no banco de dados da empresa, depois integrar os tais comprovantes à plataforma através da API que eles disponibilizam para os seus clientes.
Essa é a versão final da automação, e já está em produção na maquina dos operadores do financeiro. É um software Desktop, um executável que pode ser distribuído, não é hospedado em um servidor geral.  
<br/>
<br/>
## Tecnologias Utilizadas
- Python;
- PyPDF2 para manipulação de arquivos PDF;
- Tkinter (Interface Gráfica);
- Base64 para conversão dos arquivos na base padrão exigida no objeto da API;
- hashlib para a criação de uma chave de identificação exigida no objeto da API;
- API E2DOC (Integração via HTTP) - Requests para fazer as requisições -;
- pymysql (Consulta ao banco de dados da empresa)
  <br/>
  <br/>
## Instalação
1. Clone o repositório ou baixe o arquivo ZIP do programa:
```bash
    https://github.com/git-financeiro-eqs/Automacao_E2DOC.git
```
2. Instale as dependências:
```bash
    pip install -r requirements.txt
```
3. Execute o programa:
```bash
    python gui.py
```
4. Atente-se!\
   O programa tem como servidor a própria máquina do operador. Como o programa alimenta a pasta de comprovantes compartilhada da empresa,
   é preciso que o operador tenha localmente essas pastas financeiras sincronizadas com a nuvem.
<br/>

## Como Usar<br/>

1. Abra o programa.
2. Clique no botão "Selecionar Arquivos" e escolha o arquivo lote de comprovantes.
3. Clique em "Enviar" e acompanhe o progresso até que finalize e apresente a tela de resultados.
4. Você pode também visualizar o PDF do arquivo lote ou tirá-lo da lista de arquivos a enviar, basta clicar no botão que tem como ícone a logo da EQS. Esse botão abrirá uma pequena tela que oferece essas duas opções.
