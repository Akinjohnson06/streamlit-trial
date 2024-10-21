# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 23:06:59 2024

@author: AKIN-JOHNSON
"""

import numpy as np
import pickle
import streamlit as st
import warnings
warnings.filterwarnings('ignore')

model = pickle.load(open("school_record.pkl", "rb"))

# creating a funtion for prediction
def record_prediction(input_data):
    prediction = model.predict(input_data)
    if (prediction[0] == 0):
        return 'Student Failed the exam'
    else:
        return 'Student Passed!!!'
    
def main():
    # giving a title
    st.title('Examination Prediction')
    
    # getting the input data from the user
    maths = st.text_input('Mathematics Score')
    eng = st.text_input('English Score')
    com = st.text_input('Commerce Score')
    acc = st.text_input('Accounting Score')
    eco = st.text_input('Economics Score')
    gov = st.text_input('Government Score')
    comp = st.text_input('Computer Score')
    op = st.text_input('Office Practice Score')
    
    # code for prediction
    records = ''
    
    # creating a button for prediction
    if st.button('Predict'):
        records = record_prediction([[maths, eng, com, acc, eco, gov, comp, op]])
    
    st.success(records)
    

if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
