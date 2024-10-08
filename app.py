import streamlit as st
import chatbot
import image_gen
import numpy as np
import random

page = st.sidebar.selectbox("Page", ("Home", "Chatbot","Image_gen", "Log-out"))

if page == "Home":
    st.title("Home")
    st.write("Welcome to drip AI")
    st.info("Drip AI usage analysis!")
    st.bar_chart(np.random.randn(30,3))
elif page =="Chatbot":
    chatbot.bot()
elif page =="Image_gen":
    image_gen.image_gen()
elif page == 'Log-out':
    st.info("You have logged out. successfully!")