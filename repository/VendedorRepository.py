import sqlite3
from utils.Conection import Conection

class VendedorRepository():
    def save(vendedor):
        QUERY_INSERT = """INSERT INTO vendedor
                          (nome, email) 
                          VALUES (?,?);"""
        
        data = (vendedor.getNome(), vendedor.getEmail())
        Conection.insert(QUERY_INSERT, data)

    def findAll():
        QUERY_FIND_ALL = """SELECT * FROM vendedor;"""
        result = Conection.execute(QUERY_FIND_ALL)

        return result
        