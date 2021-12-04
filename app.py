import streamlit as st
from PIL import Image 
import PIL 
import cv2

uploaded_files = st.file_uploader("Загрузите изображения с других камер для того, чтобы узнать где есть мусор", 
       accept_multiple_files=True)
for uploaded_file in uploaded_files:
    im = Image.open(uploaded_file)
    st.image(im)
    #im1 = im.save("img/1.jpg")
    with open(os.path.join("img",uploaded_file.name),"wb") as f: 
      f.write(uploaded_file.getbuffer()) 
