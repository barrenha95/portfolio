import streamlit as st # To create the webpage
import requests # To use gif from lottiefiles
from streamlit_lottie import st_lottie
from PIL import Image # To open images
import json

st.set_page_config(page_title="Isa's playground",  page_icon=":game_die:", layout="wide")

# --- LOAD ASSETS ---
hero_img = Image.open("./src/img/hero_cropped.jpeg")
diabetes_img = Image.open("./src/img/diabetes.jpg")

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
        st.write(
            '''
            I'm a friendly and cheerful Machine Learning Engineer with more than 8 years of experience working with data. Strong skills in documentation and high adaptability. I have expertise in debt collection, fraud detection, call center operations, and digital products.
            What fullfills me is help people to solve business problems and learn about the world while I do that.
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

# --- My projects ---
with st.container():
    st.write("---")
    st.header("My projects")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(diabetes_img)
    with text_column:
        st.subheader("Diabetes Prediction")
        st.write(
            '''
            Creation of a ML model that will predict if the patient will need special care for Diabetes or not. 
            This kind of model can help hospitals to foresee health risks making the treatment more accurate and agile.
            
            In this project you will see:
            - How a machine learning model is created using Python (Sklearn: Random Forest and Logistic Regression)
            - Basic artifacts every machine learning model must have
            - The fastest/simplest deployment possible of a model (API created using Streamlit)
            '''
        )
        st.markdown("[Project here...](https://github.com/barrenha95/diabetes-prediction)")

# --- ---         