from repository.ClienteRepository import ClienteRepository
from entity.Cliente import Cliente

class ClienteService():
    def save(nome, email):
        cliente = Cliente()
        cliente.setNome(nome)
        cliente.setEmail(email)

        ClienteRepository.save(cliente)

    def findAll():
        result = ClienteRepository.findAll()
        clientes = []
        for row in result:
            cliente = Cliente()
            cliente.setId(row[0])
            cliente.setNome(row[1])
            cliente.setEmail(row[2])

            clientes.append(cliente)
        
        return clientes