import sqlite3
from utils.Conection import Conection

class VendaRepository():
    def save(venda):
        QUERY_INSERT = """INSERT INTO venda
                        (idcliente, idvendedor, idcarro) 
                        VALUES (?, ?, ?);"""
        cliente = venda.getCliente()
        vendedor = venda.getVendedor()
        carro = venda.getCarro()

        data = ( cliente.getId(), vendedor.getId(), carro.getId())
        Conection.insert(QUERY_INSERT, data)

    def buscarPorVendedor(sr):
        QUERY_FIND_ALL = """select ve.nome as nomevendedor, ca.modelo as modelocarro, cl.nome as nomecliente from venda ven
                            left join carro ca on ca.id = ven.idcarro
                            left join vendedor ve on ve.id = ven.idvendedor
                            left join cliente cl on cl.id = ven.idcliente
                            WHERE ve.nome like '%:sr%'"""

        query = QUERY_FIND_ALL.replace(":sr", sr)

        result = Conection.execute(query)

        return result

    def buscarPorCliente(sr):
        QUERY_FIND_ALL = """select cl.nome as nomecliente, ca.modelo as modelocarro from venda ven
                            left join carro ca on ca.id = ven.idcarro
                            left join cliente cl on cl.id = ven.idcliente
                            WHERE cl.nome like '%:sr%'"""

        query = QUERY_FIND_ALL.replace(":sr", sr)

        result = Conection.execute(query)

        return result