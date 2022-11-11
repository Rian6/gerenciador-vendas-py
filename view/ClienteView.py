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
        st.markdown("---")
        st.markdown("##### Geral")
        col1, col2 = st.columns(2)
        with col1:
            nome = st.text_input("Nome *",  key = "inpt_nome")
            sobrenome = st.text_input("Sobrenome *",  key = "inpt_sobrenome")
        with col2:
            cpf = st.text_input("CPF *",  key = "inpt_cpf")
            data_nasc = st.date_input("Data de nascimento *",  key = "inpt_datanasc")
        st.markdown("---")

        st.markdown("##### Endereço")
        col3, col4 = st.columns(2)
        with col3:
            endereco = st.text_input("Endereço *", key="impt_endereco")
            numero = st.text_input("Numero *", key="impt_numero")
        with col4:
            cep = st.text_input("CEP *", key="impt_cep")
            cidade = st.text_input("Cidade *", key="impt_cidade")
        st.markdown("---")
        
        st.markdown("##### Contato")
        col5, col6 = st.columns(2)
        with col5:
            telefone = st.text_input("Telefone *")
        with col6:
            email = st.text_input("Email *")

        b1 = st.button("Cadastrar")

    if(b1):
        cadastrarCliente(nome, email)
        st.success('Cliente ('+nome+') cadastrado com sucesso!', icon="✅")
    
    clientes = carregarClientes()
    
    st.markdown("---")
    st.dataframe(clientes, use_container_width=True)