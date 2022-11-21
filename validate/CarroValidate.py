class CarroValidate:
    def validate(carro):
        msg = []

        if(carro.getModelo() == ""):
            msg.append("Favor preencher o modelo!")
        if(carro.getPlaca() == ""):
            msg.append("Favor preencher a placa!")
        return msg