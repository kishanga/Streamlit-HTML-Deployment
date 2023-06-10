import streamlit as st

st.title("Streamlit Form")
st.subheader("Enter your details below")

with st.form("myform", clear_on_submit=True):
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    
    slider = st.slider("Enter your age", min_value=10, max_value=100)
    
    button = st.form_submit_button("Submit")