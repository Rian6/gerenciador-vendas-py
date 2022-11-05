import streamlit as st

#rotas
from view.ClienteView import cliente
from view.VendedorView import vendedor
from view.CarroView import carro
from view.VendaView import venda

from utils.Conection import Conection

def router():
    def renderCliente():
        cliente()

    def renderVendedor():
        vendedor()

    def renderCarro():
        carro()

    def renderVenda():
        venda()

    router = {
        "Vender": renderVenda,
        "Cliente": renderCliente,
        "Vendedor": renderVendedor,
        "Carro": renderCarro,
    }
    
    st.sidebar.markdown("# Menu")
    st.sidebar.markdown("---")
    page = st.sidebar.selectbox("Paginas", router.keys())
    router[page]()

if __name__ == "__main__":
    Conection.initialize()

    
router()
    