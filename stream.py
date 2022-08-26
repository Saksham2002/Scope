import streamlit as st
import pandas as pd
import numpy as np
st.title('Daimler Scope')

st.sidebar.title("Welcome to Daimler")

choice = st.sidebar.selectbox("Login/Signup", ["Login","Signup"])

if choice == "Signup":
    email = st.sidebar.text_input("Enter your email address")
    password = st.sidebar.text_input("Enter your password", type="password")
    st.sidebar.text_input("Region/Department")
    Signup = st.sidebar.button("Signup")
    if Signup:
        user = auth.create_user_with_email_and_password(email,password)
        st.balloons()
        st.success("Account Created")

elif choice == "Login":
    email = st.sidebar.text_input("Email")
    password = st.sidebar.text_input("Password",type="password")
    Login = st.sidebar.button("Login")
    forgot = st.sidebar.button("Forgot Password")
    if Login:
        user = auth.sign_in_with_email_and_password(email, password)
        st.balloons()
        st.title("Daimler")
        # Navigation Pane


