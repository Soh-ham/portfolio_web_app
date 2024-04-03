import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")
    
with col2:
    st.title("Maksym Solomyanov")
    content = """
    Hi, I am Maksym or simply Max. I am a Python programmer.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""

st.write(content2)