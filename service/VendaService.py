from repository.VendaRepository import VendaRepository

from entity.Carro import Carro
from entity.Cliente import Cliente
from entity.Vendedor import Vendedor
from entity.Venda import Venda

class VendaService():
    def save(idCliente, idVendedor, idCarro):

        carro = Carro()
        carro.setId(idCarro)

        vendedor = Vendedor()
        vendedor.setId(idVendedor)

        cliente = Cliente()
        cliente.setId(idCliente)

        venda = Venda()
        venda.setCarro(carro)
        venda.setCliente(cliente)
        venda.setVendedor(vendedor)

        VendaRepository.save(venda)

    def buscarPorVendedor(sr):
        result = VendaRepository.buscarPorVendedor(sr)
        vendas = []

        for row in result:        
            vendedor = Vendedor()
            vendedor.setNome(row[0])

            carro = Carro()
            carro.setModelo(row[1])

            cliente = Cliente()
            cliente.setNome(row[2])

            venda = Venda()
            venda.setCarro(carro)
            venda.setCliente(cliente)
            venda.setVendedor(vendedor)

            vendas.append(venda)
        
        return vendas