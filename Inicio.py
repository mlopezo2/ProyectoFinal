import streamlit as st
from PIL import Image

st.title("Control de luces y puerta en casa")

image = Image.open("Lights.jpg")
st.image(image, caption="Luces de interior")

st.header("¿Cómo puedo utilizar el asistente de control del hogar?")
st.write("En la página de Luces podrás cambiar el color de las luces a través de dos gestos:")

