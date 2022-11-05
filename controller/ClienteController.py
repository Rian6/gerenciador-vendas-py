from service.ClienteService import ClienteService

class ClienteController():
    def cadastrar(nome, email):
        ClienteService.save(nome, email)

    def buscarTodos():
        clientes = ClienteService.findAll()

        dicClientes = []
        for objeto in clientes:
            dic = {}
            dic["Nome"] = objeto.getNome()
            dic["Email"] = objeto.getEmail()

            dicClientes.append(dic)
        return dicClientes
    
    def findAllCombo():
        clientes = ClienteService.findAll()

        listaFinal = []
        for objeto in clientes:
            data = [objeto.getId(), objeto.getNome()]
            listaFinal.append(data)
        return tuple([str(p[0])+" - "+p[1] for p in listaFinal])