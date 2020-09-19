import streamlit as st

st.title("Data Mining")
st.subheader("Welcome to our first streamlit app")

x=st.slider('x')
st.write(x, 'squared is', x*x)
