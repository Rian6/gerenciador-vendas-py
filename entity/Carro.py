class Carro:
    def __init__(self):
        self.id = 0
        self.modelo = ""
        self.placa = ""
    
    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

    def setPlaca(self, placa):
        self.placa = placa

    def getPlaca(self):
        return self.placa