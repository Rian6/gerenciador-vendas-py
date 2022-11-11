import streamlit as st
from controller.CarroController import CarroController

def cadastrarCarro(modelo, placa):
    CarroController.cadastrar(modelo, placa)

def carregarCarros(typ):
    carros = CarroController.findAllNaoVendidos(typ)
    return carros

def carro():
    st.markdown("# Carro")

    st.markdown("---")

    st.markdown("### Cadastrar")

    col1, col2 = st.columns(2)
    with col1:
        modelo = st.text_input("Modelo")
    with col2:
        placa = st.text_input("Placa")

    b1 = st.button("Cadastrar")

    if(b1):
        cadastrarCarro(modelo, placa)
        st.success('Carro ('+modelo+') cadastrado com sucesso!', icon="✅")
    
    st.markdown("---")
    typ = st.selectbox("Filtrar: ", ["Todos", "Vendidos", "Não Vendidos"])
    carros = carregarCarros(typ)
    st.dataframe(carros, use_container_width=True)