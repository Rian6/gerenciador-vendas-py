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

    def findAllNaoVendidos():
        QUERY_FIND_ALL_NAO_VENDIDOS = """SELECT * FROM carro 
                            where carro.id NOT IN (
                                select idcarro from venda v  
                            )"""
        result = Conection.execute(QUERY_FIND_ALL_NAO_VENDIDOS)
        return result
        
    def findAllVendidos():
        QUERY_FIND_ALL_VENDIDOS = """SELECT * FROM carro 
                            where carro.id IN (
                                select idcarro from venda v  
                            )"""
        result = Conection.execute(QUERY_FIND_ALL_VENDIDOS)

        return result

