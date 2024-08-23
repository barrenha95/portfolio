import streamlit as st
import streamlit.components.v1 as components

path_to_html = "./content/portfolio.html"

with open(path_to_html, 'r') as f:
    html_data = f.read()

st.header("Show an external HTML")
st.components.v1.html(html_data, scrolling=True, height=500)
#st.markdown(html_data, unsafe_allow_html=True)

#st.write('Hello world!')
