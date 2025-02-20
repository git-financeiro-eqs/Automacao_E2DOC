# Automação E2DOC

Essa automação conta com uma interface para interação do usuário, 
e faz conexão com uma plataforma de gestão de documentos voltada para o setor jurídico chamada E2DOC.

O objetivo dessa automação é alimentar a plataforma E2DOC com os comprovantes de pagamento feitos isoladamente no portal de um banco determinado. 
Em detalhes, o que ocorre é que a maioria dos pagamentos feitos pelo setor financeiro são realizados de forma automática pelo sistema ERP da empresa, 
mas, existem os casos onde, devido uma falha no processo, o título de pagamento não pode ser efetivado pelas vias comuns, implicando que seu pagamento seja feito de forma manual, direto no portal do banco.
Esses comprovantes "manuais" precisam estar disponíveis para consulta do setor jurídico na plataforma E2DOC. Ao contrario dos comprovantes pagos pelo sistema ERP, - que alimentam a plataforma automaticamente devido uma integração que há entre o ERP e o E2DOC - os comprovantes manuais não são integrados automaticamente à plataforma, fazendo com que seja necessário a ação de um operador para separar esse documento do arquivo lote de comprovantes extraídos da plataforma do banco, e, fazer a sua integração manual, alimentando uma pasta processual compartilhada na nuvem com aquele documento e preenchendo um formulário com os seus dados no E2DOC, fazendo assim sua indexação.

Na interface de interação, o usuário irá clicar em um botão que o permitirá selecionar o, ou, os arquivos lote desejados. 
O caminho desses arquivos lote é armazenado em uma lista, que será percorrida pela automação. Antigamente, o usuário separava comprovante por comprovante pela sua natureza, pelo seu tipo de pagamento, por exemplo: pagamento de VA, VT, salário, férias, e etc...
Existe uma lista de processos que podem ocorrer pagamento manual, todos mapeados nessa automação, e, cada tipo de natureza de pagamento tem uma pasta final correspondente na nuvem, onde o comprovante deve ser salvo isolado dos demais comprovantes, tendo como título do arquivo apenas o nome completo do colaborador para o qual se destinou aquele pagamento.
Através de uma informação complementar distinta inserida no comprovante "manual" - convencionada em reuniões de levantamento de requisitos onde determinou-se a criação de uma chave de identificação - faz-se então a distinção dos comprovantes. Essa chave obedece a seguinte estrutura: CHAVECPFCÓDDENATUREZA; CHAVE00000000000FER.

A automação irá ler cada comprovante do arquivo lote, separar aquele pago manualmente, coletar o CPF do colaborador, destiná-lo a sua pasta processual final, e, através do CPF, buscar os dados pertinentes ao preenchimento do formulário do E2DOC direto no banco de dados da empresa, depois integrar os tais comprovantes à plataforma através da API que eles disponibilizam para os seus clientes.
Essa é a versão final da automação, e já está em produção na maquina dos operadores do financeiro. É um software Desktop, um executável que pode ser distribuido, não é hospedado em um servidor geral.  
<br/>
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
4. Observação:\
   O programa temo como servidor a própria máquina do operador. Como ele alimenta a pasta de comprovantes compartilhada da empresa,
   é preciso que o operador tenha localmente as pastas financeiras sincronizadas com a nuvem.
<br/>
<br/>
<br/>

## Como Usar<br/>

1. Abra o programa.
2. Clique no botão "Selecionar Arquivos" e escolha o arquivo lote de comprovantes.
3. Clique em "Enviar" e acompanhe o progresso até que finalize e apresente a tela de resultados.
4. Você pode também vizualizar o PDF do arquivo lote ou tirá-lo da lista de arquivos a enviar, basta clicar no botão que tem como ícone a logo da EQS. Esse botão abrirá uma pequena tela que oferece essas duas opções.
