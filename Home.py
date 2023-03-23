import streamlit as st 
import pandas as pd
import time

st.set_page_config(page_title="Home",
                   layout='wide',
                   page_icon='./images/home.png')

st.title("Detection of Helmetless and Overloaded Motorcycle Riders with YOLO (YOU ONLY LOOK ONCE) Algorithm")
st.caption('This web application Object Detection')

# Content
st.markdown("""
### This App Detect Object
- Automatically detects 3 objects

Below give are the object the our model will detect
1. Helmet
2. NoHelmet
3. MotorCycle
""")