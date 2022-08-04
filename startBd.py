from distutils.log import error
import errno
from traceback import print_exc
from bd.connectBD import connect
from .bd.configbd import config
import psycopg2
def main():
    
    connect()
    receptor = ' '
    
    print("Criação de banco de dados")
    print("A execução deste código criara um \n banco de dados para execução deste software")
    print("Deseja instalar? ")

    receptor = input()
    
    if receptor == 'sim':
        execbd()
    else:
        quit()

    
main()


def execbd():
    ## criando tabelas
    commands = (
        """CREATE TABLE cliente(
    cliente_id serial primary key,
    nome varchar(50) unique not null,
    cpf varchar(11),
    endereco varchar()100
    );"""
        
    )
conn = None


try:
    params = config()
    
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    
    for command in commands:
        cur.execute(command)
        
        
    cur.close()
    
    conn.commit()
    
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
    
finally:
    if conn is not None:
        conn.close()
