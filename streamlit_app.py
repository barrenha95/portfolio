import streamlit as st # To create the webpage
import requests # To use gif from lottiefiles
from streamlit_lottie import st_lottie
from PIL import Image # To open images
import json

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
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("About Me")
        st.write("##")
        st.write(
            '''
            I'm a friendly and cheerful Machine Learning Engineer with more than 8 years of experience working with data. Strong skills in documentation and high adaptability. I have expertise in debt collection, fraud detection, call center operations, and digital products.
            What fullfills me is help people to solve business problems and lear about the world while I do that.
            - Proficiency in Python, SQL, Power Bi, and Microsoft Excel.
            - Experience working with cloud environments such as Azure and Databricks Lakehouse.
            - I'm able to work with technologies like Git, PySpark
            - Often I'm reference in directory management, and project documentation.
            '''
        )

    with right_column:
        with open("./src/gif/boy_coding.json") as f:
            desired_gif = json.load(f)
        st_lottie(desired_gif, height=300, key="coding")

# --- ---         