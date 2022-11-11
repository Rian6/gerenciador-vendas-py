import streamlit as st

from utils.Conection import Conection
from utils.Router import Router
from utils.Style import Style

if __name__ == "__main__":
    Conection.initialize()
    Style.renderTheme()    
    Router.router()
    