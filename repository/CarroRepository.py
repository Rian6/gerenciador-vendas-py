import sqlite3
from utils.Conection import Conection

class CarroRepository():
    def save(carro):
        QUERY_INSERT = """INSERT INTO carro
                          (modelo, placa) 
                          VALUES (?,?);"""
        
        data = (carro.getModelo(), carro.getPlaca())
        Conection.insert(QUERY_INSERT, data)

    def findAll():
        QUERY_FIND_ALL = """SELECT * FROM carro;"""
        result = Conection.execute(QUERY_FIND_ALL)

        return result
        

