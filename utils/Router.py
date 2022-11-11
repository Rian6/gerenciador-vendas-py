import streamlit as st

#rotas
from view.ClienteView import cliente
from view.VendedorView import vendedor
from view.CarroView import carro
from view.VendaView import venda

class Router():
    def router():
        def renderCliente():
            cliente()

        def renderVendedor():
            vendedor()

        def renderCarro():
            carro()

        def renderVenda():
            venda()
        
        a = open("screen_cache.bin", "r")
        pagina_selecionada = a.read()
        a.close()
        
        st.sidebar.markdown("# Menu")
        st.sidebar.markdown("---")
        
        bvenda = st.sidebar.button("👜​ Vender", key = "b1")
        bcliente = st.sidebar.button("🧒​ Cliente")
        bvendedor = st.sidebar.button("🧑‍💼​ Vendedor", key = "b3")
        bcarro = st.sidebar.button("🚗 Carro", key = "b4")

        pages = {
            "venda": renderVenda,
            "cliente": renderCliente,
            "vendedor": renderVendedor,
            "carro": renderCarro,
        }

        if(bvenda):
            pagina_selecionada = "venda"
        elif(bcliente):
            pagina_selecionada = "cliente"
        elif(bvendedor):
            pagina_selecionada = "vendedor"
        elif(bcarro):
            pagina_selecionada = "carro"

        ar = open("screen_cache.bin", "w")
        ar.write(pagina_selecionada)
        ar.close()

        pages[pagina_selecionada]()
