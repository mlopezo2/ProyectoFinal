import streamlit as st
from PIL import Image

st.title("Control de luces y puerta en casa")

image = Image.open("Lights.jpg")
st.image(image, caption="Luces de interior")

st.header("¿Cómo puedo utilizar el asistente de control del hogar?")
st.write("En la página de Luces podrás cambiar el color de las luces a través de dos gestos:")

image2 = Image.open("DedoApuntando.jpg")
st.image(image2, caption="Dedo apuntando")

st.write("El gesto de dedo apuntando enfrente de la cámara encenderá la luz rosada.")

image3 = Image.open("PuñoMano.jpg")
st.image(image3, caption="Mano en puño")

st.write("El gesto de la mano en forma de puño enfrente de la cámara encenderá la luz azul.")

