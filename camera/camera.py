import streamlit as st
from PIL import Image

with st.expander("click to open camera"):
    #start the camera
    camera_image = st.camera_input("camera")

if camera_image:
    #create pillow image instance
    img = Image.open(camera_image)

#convert the image into
    gray_img = img.convert("L")

# render the grayscale
    st.image(gray_img)