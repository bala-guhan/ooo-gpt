import streamlit as st
import time
def image_gen():
    st.header("Image generation (Text-to-Image)")
    
    with st.spinner():
        time.sleep(3)
        st.image('page_under_const.webp')
    

