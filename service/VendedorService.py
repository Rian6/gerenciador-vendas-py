from repository.VendedorRepository import VendedorRepository
from entity.Vendedor import Vendedor

class VendedorService():
    def save(nome, email):
        vendedor = Vendedor()
        vendedor.setNome(nome)
        vendedor.setEmail(email)

        VendedorRepository.save(vendedor)

    def findAll():
        result = VendedorRepository.findAll()
        vendedores = []
        if(type(result) is list):
            for row in result:
                vendedor = Vendedor()
                vendedor.setId(row[0])
                vendedor.setNome(row[1])
                vendedor.setEmail(row[2])

                vendedores.append(vendedor)
        return vendedores