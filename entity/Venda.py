from entity.Vendedor import Vendedor
from entity.Carro import Carro
from entity.Cliente import Cliente

class Venda:
    def __init__(self):
        self.vendedor = Vendedor
        self.cliente = Cliente
        self.carro = Carro

    def setCliente(self, cliente):
        self.cliente = cliente

    def getCliente(self):
        return self.cliente
    
    def setCarro(self, carro):
        self.carro = carro

    def getCarro(self):
        return self.carro
    
    def setVendedor(self, vendedor):
        self.vendedor = vendedor

    def getVendedor(self):
        return self.vendedor