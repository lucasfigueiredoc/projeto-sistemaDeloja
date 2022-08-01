
import psycopg2
from configparser import ConfigParser
from config import config

def connect():
    conn = None
    try:
        # lendo parametros do config()
        params = config()
        
        # conectando ao postgres
        print('Conectando ao PostgreSQL database.')
        conn = psycopg2.connect(**params)
        
        # criando um cursor
        cur = conn.cursor()
        
        # executando o statement
        print('Versão do Postgresql')
        cur.execute('SELECT version()')
        
        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
        
        # close te communication with the PostgreSQL
        
        cur.close()
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        
    finally:
        if conn is not None:
            conn.close()
            print('DB Conecção fechada')
        
if __name__ == '__main__':
    connect()