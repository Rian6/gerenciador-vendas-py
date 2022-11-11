from service.VendaService import VendaService

class VendaController():
    def cadastrar(idCliente, idVendedor, idCarro):
        VendaService.save(idCliente, idVendedor, idCarro)

    def buscarPorVendedor(sr=""):
        vendas = VendaService.buscarPorVendedor(sr)

        dicVendas = []
        for objeto in vendas:
            dic = {}
            dic["Vendedor"] = objeto.getVendedor().getNome()
            dic["Cliente"] = objeto.getCliente().getNome()
            dic["Carro"] = objeto.getCarro().getModelo()

            dicVendas.append(dic)
        return dicVendas

    def buscarPorCliente(sr=""):
        vendas = VendaService.buscarPorCliente(sr)

        dicVendas = []
        for objeto in vendas:
            dic = {}
            dic["Cliente"] = objeto.getCliente().getNome()
            dic["Carro"] = objeto.getCarro().getModelo()

            dicVendas.append(dic)
        return dicVendas