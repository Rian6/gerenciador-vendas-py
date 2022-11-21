from service.CarroService import CarroService
import streamlit as st

from entity.Carro import Carro
from validate.CarroValidate import CarroValidate

class CarroController():
    def cadastrar(modelo, placa):
        carro = Carro()
        carro.setModelo(modelo)
        carro.setPlaca(placa)

        validate = CarroValidate.validate(carro)
        if(validate == []):
            CarroService.save(carro)
            st.success('Carro ( '+modelo+' ) cadastrado com sucesso!', icon="✅")
        else:
            for i in validate:
                st.error("Erro: "+i, icon="✅")

    def findAllNaoVendidos(typ):
        if(typ == "Não Vendidos"):
            carros = CarroService.findAllNaoVendidos()
        elif(typ == "Vendidos"):
            carros = CarroService.findAllVendidos()
        elif("Todos"):
            carros = CarroService.findAll()
        
        dicCarros = []
        for objeto in carros:
            dic = {}
            dic["Modelo"] = objeto.getModelo()
            dic["Placa"] = objeto.getPlaca()

            dicCarros.append(dic)
        return dicCarros

    def findAllCombo():
        carros = CarroService.findAllNaoVendidos()
        
        listaFinal = []
        for objeto in carros:
            data = [objeto.getId(), objeto.getModelo()]
            listaFinal.append(data)
        return tuple([str(p[0])+" - "+p[1] for p in listaFinal])