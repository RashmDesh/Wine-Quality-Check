'''@Author : Rashmi Deshmukh'''
import streamlit as st
import pandas as pd
from PIL import Image
import pickle


model = pickle.load(open('C:/Users/lenovo/Desktop/datasets/Red wine quality/ML_Model.pkl', 'rb'))

html_temp=""" <div style="background-color:#722F37;padding:2px"> """

def run():
    img1 = Image.open('C:/Users/lenovo/Desktop/datasets/Red wine quality/wine.png')
    img1 = img1.resize((500,245))
    st.image(img1,use_column_width=False)
    st.title("Wine Quality Check")

    st.markdown(html_temp, unsafe_allow_html=True)

    fixed_acidity=st.slider("1.Select fixied acidity level :",4,16)
    volatile_acidity=st.number_input("2.Select volatile acidity level(Min=0.00 and Max=2.00) :")
    residual_sugar=st.slider("3.Select residual sugar level:",0,15)
    pH=st.slider("4.Select pH level :",2.0,4.0)
    alcohol=st.slider("5.Select alcohol level :",1,14)

    st.markdown(html_temp, unsafe_allow_html=True)

    if st.button("Submit"):
        features = [[fixed_acidity,volatile_acidity,residual_sugar,pH,alcohol]]
        #st.table(features)
        prediction = model.predict(features)
        lc = [str(i) for i in prediction]
        ans = int("".join(lc))
        st.write("Quality of wine is ",ans," out of 10")
        if ans >6:
            st.success("Quality of Wine is Superb")
        elif(ans<=6 and ans >= 5):
            st.success("Quality of Wine is Good")
        else:
            st.success("Quality of  Wine  is Bad")
run()
