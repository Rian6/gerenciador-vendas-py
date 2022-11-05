from repository.CarroRepository import CarroRepository
from entity.Carro import Carro

class CarroService():
    def save(modelo, placa):
        carro = Carro()
        carro.setModelo(modelo)
        carro.setPlaca(placa)

        CarroRepository.save(carro)

    def findAll():
        result = CarroRepository.findAll()
        carros = []
        for row in result:
            carro = Carro()
            carro.setId(row[0])
            carro.setModelo(row[1])
            carro.setPlaca(row[2])

            carros.append(carro)
        
        return carros