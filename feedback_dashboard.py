import streamlit as st
import numpy as np
import pandas as pd

def main():
    st.title("Dashboard Feedback")

    d = st.date_input("Please Enter Today's date",None, None, None, None)
    
    question_1 = st.text_input('Please enter your Centre Name', max_chars=50)
    
    question_2 = st.slider('Did you find this report useful?', 1,5)
    
    question_3 = st.selectbox('How often do you want to receive this update?',('Once in a Day','Once in a Week', 'Once in a Month', 'Never'))
    
    question_4 = st.text_input('What else you would like to see in email ?', max_chars=100)
    
    question_5 = st.text_input('What is not useful in the email dashboard?', max_chars=100)
    
    question_6 = st.text_input('Do you have any specific requirement? Appreciate your detailed feedback to help your better visibility.', max_chars=500)
    
    question_7 = st.text_input('Name', max_chars=30)
    
    
if __name__ == '__main__':
    main()