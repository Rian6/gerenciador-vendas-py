import streamlit as st

class Style():
    def renderTheme():
        f = open('./style/style.css', 'r')
        style = f.read()
        st.markdown("<style>"+style+"</style>", unsafe_allow_html=True)