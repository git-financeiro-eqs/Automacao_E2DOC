import os
import smtplib
from datetime import datetime
from email.message import EmailMessage



def retornar_mes(mes):
    meses = {
        '01': 'JANEIRO',
        '02': 'FEVEREIRO',
        '03': 'MARÇO',
        '04': 'ABRIL',
        '05': 'MAIO',
        '06': 'JUNHO',
        '07': 'JULHO',
        '08': 'AGOSTO',
        '09': 'SETEMBRO',
        '10': 'OUTUBRO',
        '11': 'NOVEMBRO',
        '12': 'DEZEMBRO' 
    }
    return f'{mes} - {meses[mes]}'



def retornar_banco(caminho):
    match caminho:
        case _ if "ITAU" in caminho:
            banco = "ITAU"
        case _ if "SANTANDER" in caminho:
            banco = "SANTANDER"
        case _ if "BRADESCO" in caminho:
            banco = "BRADESCO"
        case _ if "CEF" in caminho:
            banco = "CEF"
        case _ if "BB" in caminho:
            banco = "BB (BANCO DO BRASIL)"
    return banco



def retornar_dt_festiva():
    """
    Função utilizada para lançar uma mensagem amistosa no relatório do E-mail.    
    """

    _, data = retornar_data()

    feriados = {
            "01/04": '''Viva à fantasia, a capacidade humana de imaginar e contar a realidade como ela deveria ser!
"Não sei, só sei que foi assim" - Chicó''',
            "22/04": "Dia da Terra! Vamos cuidar bem do nosso planeta.",
            "01/05": "Feliz dia do trabalhador para você que trabalha e sente muita dor.",
            "11/05": "Feliz dia das mães!",
            "05/06": "Dia Mundial do Meio Ambiente! A natureza agradece!",
            "12/06": "Para todos os sortudos que encontraram o amor, Feliz dia dos namorados!",
            "10/08": "Feliz dia dos pais!",
            "07/09": "Viva a nossa independência!",
            "23/09": "Bem-vinda, primavera! Flores para alegrar o dia.",
            "12/10": "Feliz dia das nossas crianças!",
            "31/10": "Feliz dia do Saci, pessoal!",
            "02/11": "Saudemos os nossos mortos. Eles estão diante do maior mistério da nossa existência, o estar ou o não estar."
        }

    if data >= "16/06" and data <= "24/06":
        return "Feliz São João! É festa junina com muito forró e canjica!"
    elif data >= "20/12" and data <= "31/12":
        return "Boas festas!"
    else:
        return feriados.get(data, "")



def criar_arvore_diretorios(diretorio_destino, ano_vigente, mes_vigente, data_de_pagamento, tipo='Simples', pedido=''):
    """
    Função utilizada para destinar os comprovantes para sua pasta processual compartilhada .
    """

    if tipo == "FOLHA GERAL":
        mes = mes_vigente[:2]
        if mes == "01":
            ano_vigente = str(int(ano_vigente) - 1)
            mes_vigente = retornar_mes("12")
        else:
            mes = int(mes) - 1
            mes_vigente = retornar_mes(f"{mes:02}")

    if 'RESCISOES' in diretorio_destino:
        ano_vigente = f'RESCISAO {ano_vigente}'

    if not ano_vigente in os.listdir(diretorio_destino):
        os.mkdir(diretorio_destino + "\\" + ano_vigente)

    diretorio_destino = diretorio_destino + "\\" + ano_vigente

    if not mes_vigente in os.listdir(diretorio_destino):
        os.mkdir(diretorio_destino + "\\" + mes_vigente)

    diretorio_destino = diretorio_destino + "\\" + mes_vigente

    if '13 SALARIO' not in tipo:
        if not data_de_pagamento in os.listdir(diretorio_destino):
            os.mkdir(diretorio_destino + "\\" + data_de_pagamento)
        
        diretorio_destino = diretorio_destino + "\\" + data_de_pagamento

    if tipo != 'Simples':
        if pedido != '':
            tipo = tipo + " - " + pedido
            if not tipo in os.listdir(diretorio_destino):
                os.mkdir(diretorio_destino + "\\" + tipo)

        elif tipo in ['1ª 13 SALARIO', '2ª 13 SALARIO', 'TJ 13 SALARIO']:
            if 'TJ' in tipo:
                tipo = 'TRIBUNAL DE JUSTIÇA'
            else:    
                tipo = f'{tipo[:2]} PARCELA {data_de_pagamento}'
            if not tipo in os.listdir(diretorio_destino):
                os.mkdir(diretorio_destino + "\\" + tipo)

        elif tipo == '13 SALARIO':
            tipo = ""

        elif not tipo in os.listdir(diretorio_destino):
            os.mkdir(diretorio_destino + "\\" + tipo)

        diretorio_destino = diretorio_destino + "\\" + tipo

    return diretorio_destino



def enviar_email(relatorio, tipo_pag_incorreto, cpfs_errados, compv_nao_env):
    feriado = retornar_dt_festiva()
    list_tratada = ["".join(lista) for lista in relatorio]
    string = '''

'''.join(list_tratada)

    if tipo_pag_incorreto:
        if len(tipo_pag_incorreto) > 1:
            string_tipo = "".join(tipo_pag_incorreto)
            tipo_pag_incorreto = f'''
As seguintes chaves extraídas dos comprovantes apresentaram inconsistência:
{string_tipo}'''
        else:
            string_tipo = tipo_pag_incorreto[0]
            tipo_pag_incorreto = f'''
A seguinte chave inserida em um comprovante apresentou inconsistência:
{string_tipo}'''
        

    if compv_nao_env:
        if len(compv_nao_env) > 1:
            string_cne = " - ".join(compv_nao_env)
            comp_nao_env = f'''
Devido alguma inconsistência os seguintes comprovantes não foram enviados para o E2DOC:
{string_cne}'''
        else:
            string_cne = " - ".join(str(item) for item in compv_nao_env[0])
            comp_nao_env = f'''
Devido alguma inconsistência o seguinte comprovante não foi enviado para o E2DOC:
{string_cne}'''
            

    if cpfs_errados:
        if len(cpfs_errados) > 1:
            string_cpf = ", ".join(cpfs_errados)
            cpf_nao_encontrado = f'''
Os seguintes CPFs não foram encontrados em nosso banco de dados:
{string_cpf}'''
        else:
            cpf_nao_encontrado = f'''
O CPF abaixo não foi encontrado em nosso banco de dados:
{cpfs_errados[0]}'''
        

    if tipo_pag_incorreto and cpfs_errados and comp_nao_env:
        texto = f'''Envio finalizado!    
{cpf_nao_encontrado}
{comp_nao_env}
{tipo_pag_incorreto}

{feriado}'''
    elif tipo_pag_incorreto and cpfs_errados:
        texto = f'''Envio finalizado!
{cpf_nao_encontrado}
{tipo_pag_incorreto}

{feriado}'''
    elif tipo_pag_incorreto and comp_nao_env:
        texto = f'''Envio finalizado!
{tipo_pag_incorreto}
{comp_nao_env}

{feriado}'''
    elif cpfs_errados and comp_nao_env:
        texto = f'''Envio finalizado!
{cpf_nao_encontrado}
{comp_nao_env}

{feriado}'''
    elif tipo_pag_incorreto:
        texto = f'''Envio finalizado!
{tipo_pag_incorreto}

{feriado}'''
    elif cpfs_errados:
        texto = f'''Envio finalizado!
{cpf_nao_encontrado}

{feriado}'''
    elif compv_nao_env:
        texto = f'''Envio finalizado!
{comp_nao_env}

{feriado}'''
    else:
        texto = f'''Envio finalizado com sucesso!!!
{feriado}'''


    corpo = f'''Olá, colaborador!

Segue um relatório do que foi enviado pela automação para o E2DOC;


Envios totais: {len(relatorio)}

Processos enviados:

NOME  -  MODELO DE DOCUMENTO  -  COMPETENCIA


{string}



{texto}


Grato pela colaboração.

Atensiosamente,
Doc Hudson,

    '''
    carta = EmailMessage()
    carta.set_content(corpo)
    carta['Subject'] = "Enviados para o E2DOC"
    carta['From'] = "eqsengenharia@eqsengenharia.com.br"
    carta['To'] = "Financeiro@eqsengenharia.com.br"

    try:
        with smtplib.SMTP_SSL('grid331.mailgrid.com.br', 465) as servidor:
            servidor.login("eqsengenharia@eqsengenharia.com.br", "*********")
            servidor.send_message(carta)
    except Exception as e:
        pass



def zerar_lista_controle(lista_controle):
    while not lista_controle.empty():
        lista_controle.get()
        lista_controle.task_done()



def retornar_data():
    agora = datetime.now()
    data_formatada = str(agora.strftime("%Y-%m-%d"))
    data = str(agora.strftime("%d/%m"))
    return data_formatada, data
