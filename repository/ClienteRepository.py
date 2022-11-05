import sqlite3
from utils.Conection import Conection

class ClienteRepository():
    def save(cliente):
        QUERY_INSERT = """INSERT INTO cliente
                          (nome, email) 
                          VALUES (?,?);"""
        
        data = (cliente.getNome(), cliente.getEmail())
        Conection.insert(QUERY_INSERT, data)

    def findAll():
        QUERY_FIND_ALL = """SELECT * FROM cliente;"""
        result = Conection.execute(QUERY_FIND_ALL)

        return result
        

