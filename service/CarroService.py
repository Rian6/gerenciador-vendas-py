from repository.CarroRepository import CarroRepository
from entity.Carro import Carro

class CarroService():
    def save(carro):
        CarroRepository.save(carro)
    
    def findAllNaoVendidos():
        result = CarroRepository.findAllNaoVendidos()
        carros = []
        
        if(type(result) == list):
            for row in result:
                carro = Carro()
                carro.setId(row[0])
                carro.setModelo(row[1])
                carro.setPlaca(row[2])

                carros.append(carro)
        return carros

    def findAllVendidos():
        result = CarroRepository.findAllVendidos()
        carros = []
        if(type(result) is list):
            for row in result:
                carro = Carro()
                carro.setId(row[0])
                carro.setModelo(row[1])
                carro.setPlaca(row[2])

                carros.append(carro)
        
        return carros

    def findAll():
        result = CarroRepository.findAll()
        carros = []

        if(type(result) is list):
            for row in result:
                carro = Carro()
                carro.setId(row[0])
                carro.setModelo(row[1])
                carro.setPlaca(row[2])

                carros.append(carro)
        
        return carros