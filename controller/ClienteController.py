from service.ClienteService import ClienteService
import streamlit as st

from entity.Cliente import Cliente
from validate.ClienteValidate import ClienteValidate

class ClienteController():
    def cadastrar(nome, email):
        cliente = Cliente()
        cliente.setNome(nome)
        cliente.setEmail(email)

        validate = ClienteValidate.validate(cliente)
        if(validate == []):
            ClienteService.save(cliente)
            st.success('Cliente ( '+nome+' ) cadastrado com sucesso!', icon="✅")
        else:
            for i in validate:
                st.error("Erro: "+i, icon="✅")

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