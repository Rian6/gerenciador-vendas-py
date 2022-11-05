from service.CarroService import CarroService

class CarroController():
    def cadastrar(modelo, placa):
        CarroService.save(modelo, placa)

    def buscarTodos():
        carros = CarroService.findAll()

        dicCarros = []
        for objeto in carros:
            dic = {}
            dic["Modelo"] = objeto.getModelo()
            dic["Placa"] = objeto.getPlaca()

            dicCarros.append(dic)
        return dicCarros

    def findAllCombo():
        carros = CarroService.findAll()
        
        listaFinal = []
        for objeto in carros:
            data = [objeto.getId(), objeto.getModelo()]
            listaFinal.append(data)
        return tuple([str(p[0])+" - "+p[1] for p in listaFinal])