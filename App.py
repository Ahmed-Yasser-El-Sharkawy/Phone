import streamlit as st
import numpy as np
import pickle


st.title("Mobile Price Classification")
st.write("Bob has started his own mobile company. He wants to give tough fight to big companies like Apple,Samsung etc.")


phone_catagory={0:'Low Cost',
                1:'Mid Cost',
                2:'High Cost',
                3:"Very High Cost"}

def F_Mobile_Category( l ):
    with open('pricetelephone','rb') as file: 
        ourModel = pickle.load(file) 
    pred=ourModel.predict([l])
    return pred

# User Input
def user_Input():
    Ram = st.number_input('Ram: Random Access Memory in Mega Bytes',min_value=256,max_value=9000,step=1)
    battery_power = st.number_input('battery_power: Total energy a battery can store in one time measured in mAh',min_value=501,max_value=4000,step=1)
    px_width = st.number_input('px_width: Pixel Resolution Width',min_value=500,max_value=4000,step=1)
    px_height = st.number_input('px_height: Pixel Resolution Height',min_value=0,max_value=4000,step=1)
    int_memory = st.number_input('int_memory: Internal Memory in Gigabytes',min_value=2,max_value=512,step=1)
    sc_w = st.number_input('sc_w : Screen Width of mobile in cm',min_value=0,max_value=40,step=1)
    pc = st.number_input('PC: Primary Camera mega pixels',min_value=0,max_value=40,step=1)
    touch_screen = st.selectbox('Touch Screen: Has touch screen or not', ['Yes', 'No'])
    if touch_screen == 'Yes':
        touch_scr=1
    else:
        touch_scr=0
    three_g = st.selectbox('three_g: Has 3G or not', ['Yes', 'No'])
    if three_g == 'Yes':
        thre_g=1
    else:
        thre_g=0
    mobile_wt = st.number_input('mobile_wt: Weight of mobile phone',min_value=80,max_value=400,step=1)
    l =[Ram , battery_power, px_width , px_height,  int_memory, sc_w ,pc ,touch_scr, mobile_wt,thre_g] 
    return l

# Display the user input
l=user_Input()

# Classify the phone
pred=F_Mobile_Category(l)
run=st.button("Predicate")
if run:
    st.write('Predicted Mobile Category: ',phone_catagory[pred[0]])
