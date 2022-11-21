import streamlit as st

from utils.Conection import Conection
from utils.Router import Router
from utils.Style import Style

st.set_page_config(
    page_title="Vendas App"
)
Conection.initialize()
Style.renderTheme()    
Router.router()
    