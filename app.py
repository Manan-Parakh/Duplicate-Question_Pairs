import streamlit as st
import pickle
import distance
import re
from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz
import numpy as np
import helper

# Setup the Page
st.set_page_config(page_icon="2️⃣", page_title="Duplicate Question Pair Checker")
st.title('Duplicate Question Pair Checker')

model = pickle.load(open('xgb_model.pkl', 'rb'))

q1 = st.text_input('Enter question 1')
q2 = st.text_input('Enter question 2')

if st.button('Find'):
    features = helper.query_point_creator(q1, q2)
    result = model.predict(features)[0]
    if result:
        st.subheader('Duplicate')
    else:
        st.subheader('Not Duplicate')
