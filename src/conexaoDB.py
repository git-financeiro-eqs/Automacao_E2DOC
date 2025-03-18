import pymysql
from pymysql.cursors import DictCursor


def consultar_db(cpf):
    try:
        conn = pymysql.connect(
            host='***.**.**.**',
            user='*****',
            password='********',
            database='e2doc',
            cursorclass=DictCursor
        )

        cursor = conn.cursor()

        try:
            sql = f"SELECT * FROM import_csv WHERE cpf = {cpf};"
            cursor.execute(sql)
            consulta = cursor.fetchone()

            regiao = consulta['regiao_pcs']
            centro_de_custo = consulta['cc']
            nome = consulta['funcionario']

            conn.close()
            return regiao, centro_de_custo, nome
        
        except Exception:
            regiao = False
            centro_de_custo = False
            nome = False
            return regiao, centro_de_custo, nome
    
    except Exception as e:
        raise Exception(f"Erro ao se conectar com o banco de dados: {e}")

