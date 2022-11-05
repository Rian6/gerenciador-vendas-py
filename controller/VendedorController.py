from service.VendedorService import VendedorService

class VendedorController():
    def cadastrar(nome, email):
        VendedorService.save(nome, email)

    def buscarTodos():
        vendedores = VendedorService.findAll()

        dicVendedores = []
        for objeto in vendedores:
            dic = {}
            dic["Nome"] = objeto.getNome()
            dic["Email"] = objeto.getEmail()

            dicVendedores.append(dic)
        return dicVendedores

    def findAllCombo():
        vendedores = VendedorService.findAll()

        listaFinal = []
        for objeto in vendedores:
            data = [objeto.getId(), objeto.getNome()]
            listaFinal.append(data)
        return tuple([str(p[0])+" - "+p[1] for p in listaFinal])