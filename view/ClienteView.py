import streamlit as st
from controller.ClienteController import ClienteController

def cadastrarCliente(nome, email):
    ClienteController.cadastrar(nome, email)

def carregarClientes():
    clientes = ClienteController.buscarTodos()
    return clientes

def cliente():
    st.markdown("# 🧒 Cliente")

    with st.expander("Cadastrar"):
        st.markdown("### Cadastrar")
        col1, col2 = st.columns(2)
        with col1:
            nome = st.text_input("Nome *",  key = "inpt_nome")
        with col2:
            email = st.text_input("Email *")

        b1 = st.button("Cadastrar")

    if(b1):
        cadastrarCliente(nome, email)

    clientes = carregarClientes()
    
    st.markdown("---")
    st.dataframe(clientes, use_container_width=True)