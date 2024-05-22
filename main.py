import streamlit as st
import helper
import pickle
import keras
# model = pickle.load(open('model/model.pkl','rb'))
model = keras.models.load_model('model/model.pkl')


st.header('Duplicate Question Pairs')

q1 = st.text_input('Enter question 1')
q2 = st.text_input('Enter question 2')

if st.button('Find'):
    query = helper.PreprocessQuery(q1,q2)
    result = model.predict(query)[0]

    if result:
        st.header('Duplicate')
    else:
        st.header('Not Duplicate')
