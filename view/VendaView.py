import streamlit as st
import pandas as pd

from controller.ClienteController import ClienteController
from controller.CarroController import CarroController
from controller.VendedorController import VendedorController
from controller.VendaController import VendaController

from utils.Utils import Utils

def cadastrarVenda(idCliente, idVendedor, idCarro):
    VendaController.cadastrar(idCliente, idVendedor, idCarro)

def carregarVendas(sr):
    vendas = VendaController.buscarPorVendedor(sr)
    return vendas

def venda():
    st.markdown("# Vendas")

    st.markdown("---")

    st.markdown("### vender")

    col1, col2, col3 = st.columns(3)
    
    listaClientes = ClienteController.findAllCombo()
    listaVendedores = VendedorController.findAllCombo()
    listaCarros = CarroController.findAllCombo()

    with col1:
        clienteCheck = st.selectbox("Cliente", listaClientes)
    with col2:
        vendedorCheck = st.selectbox("Vendedor", listaVendedores)
    with col3:
        carroCheck = st.selectbox("Carro", listaCarros)

    idCliente = Utils.processId(clienteCheck)
    idVendedor = Utils.processId(vendedorCheck)
    idCarro = Utils.processId(carroCheck)

    b1 = st.button("Vender")

    if(b1):
        cadastrarVenda(idCliente, idVendedor, idCarro)
        st.success('Venda registrada com sucesso!', icon="✅")

    st.markdown("---")

    sr = st.text_input('Pesquisar', placeholder="Pesquisar por vendedor")

    listaVendas = carregarVendas(sr)

    st.dataframe(listaVendas, use_container_width=True)