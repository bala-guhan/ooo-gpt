import streamlit as st
import sys
import google.generativeai as genai
import os
from dotenv import load_dotenv
import numpy as np
import random

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def bot():
    st.title("Chatbot (Text-Text conversational bot)")
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What's up?"):
        
        with st.chat_message("user"):
            st.markdown(prompt)
        
        st.session_state.messages.append({"role": "user", "content": prompt})
        response = model.generate_content(prompt).text

        with st.chat_message("assistant"):
            st.markdown(response)
        
        st.session_state.messages.append({"role": "assistant", "content": response})


