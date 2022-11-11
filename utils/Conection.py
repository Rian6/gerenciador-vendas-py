import sqlite3

class Conection():
    def initialize():
        conn = sqlite3.connect('clientes.db')
        cursor = conn.cursor()
        sql = [
            """            
            CREATE TABLE IF NOT EXISTS cliente (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL
            );
            """,
            """            
            CREATE TABLE IF NOT EXISTS vendedor (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL
            );
            """,
            """            
            CREATE TABLE IF NOT EXISTS carro (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                modelo TEXT NOT NULL,
                placa TEXT NOT NULL
            );
            """,
            """            
            CREATE TABLE IF NOT EXISTS venda (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                idcarro INTEGER NOT NULL,
                idvendedor INTEGER NOT NULL,
                idcliente INTEGER NOT NULL
            );
            """,
        ]

        for s in sql:
            cursor.execute(s)
        print('Tabelas geradas com sucesso')
        conn.close()


    def insert(sql, data):
        try:
            sqliteConnection = sqlite3.connect('clientes.db')
            cursor = sqliteConnection.cursor()
            print("Sucesso ao conectar com o banco")

            cursor.execute(sql, data)
            sqliteConnection.commit()
            print("Query executada com sucesso")

            cursor.close()

        except sqlite3.Error as error:
                print("Falha ao inserir dado ao sqlite: ", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("Conexão fechada com o banco")

    def execute(query):
        records = None
        try:
            sqliteConnection = sqlite3.connect('clientes.db')
            cursor = sqliteConnection.cursor()
            print("Conectando ao sqlite")

            cursor.execute(query)

            records = cursor.fetchall()
            cursor.close()

        except sqlite3.Error as error:
            print("Falha ao ler a tabela: ", error)
        finally:
            if sqliteConnection:
                sqliteConnection.close()
                print("Conexão com o banco fechada")
            return records