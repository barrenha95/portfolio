import streamlit as st # To create the webpage
from PIL import Image # To open images

st.set_page_config(page_title="Isa's playground",  page_icon=":game_die:", layout="wide")

# --- LOAD ASSETS ---
hero_img = Image.open("./src/img/hero_cropped.jpeg")

# --- HERO SECTION ---
with st.container():
    #st.image(hero_img)
    st.title("João Barrenha")
    st.subheader("Machine Learning Engineer")
    st.write("Bauru, SP.")

# --- ABOUT ME ---
st.write("---")
left_column, right_column = st.columns(2)
with left_column:
    st.header("About Me")
    st.write("##")