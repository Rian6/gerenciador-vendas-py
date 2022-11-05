import streamlit as st
import time
from controller.VendedorController import VendedorController

def cadastrarVendedor(nome, email):
    VendedorController.cadastrar(nome, email)

def carregarVendedores():
    vendedores = VendedorController.buscarTodos()
    return vendedores

def vendedor():
    st.markdown("# Vendedor")

    st.markdown("---")

    st.markdown("### Cadastrar")

    col1, col2 = st.columns(2)
    with col1:
        nome = st.text_input("Nome")
    with col2:
        email = st.text_input("Email")

    b1 = st.button("Cadastrar")

    isSucess = False
    if(b1):
        cadastrarVendedor(nome, email)
        st.success('Vendedor ('+nome+') cadastrado com sucesso!', icon="✅")
        
    vendedores = carregarVendedores()
    
    st.markdown("---")
    st.dataframe(vendedores, use_container_width=True)