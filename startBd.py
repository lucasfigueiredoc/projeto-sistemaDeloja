import psycopg2

class bd():
    def startBD():
        host = 'localhost'
        dbname = 'sisDeloja'
        user = 'lfc'
        password = '2015'
        sslmode = 'require'

        # Construct de string
        conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
        conn = psycopg2.connect(conn_string)
        print("Conecção estabelecida")

        cursor = conn.cursor()

        def create_user(nome,email,senha):
            cursor.execute("INSERT INTO usuario (nome, email, senha) values(%s,%s,%s);", (nome,email,senha))
            
        create_user('novo usuario', 'user@gmail.com', '1231')

        conn.commit()
        cursor.closer
        conn.close()