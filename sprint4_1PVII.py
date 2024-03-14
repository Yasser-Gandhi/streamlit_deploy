import streamlit as st
from firebase_admin import firestore

# Función para insertar un nuevo filme en Firestore
def insertar_filme(nombre, director, genero, compañia):
    # Crear un documento en la colección 'peliculas' con los datos proporcionados
    db.collection(u'peliculas').add({
        u'name': nombre,
        u'director': director,
        u'genre': genero,
        u'company': compañia
    })
    st.success("El filme se ha insertado correctamente en la base de datos.")
    # Limpiar los campos del formulario después de insertar el filme
    nombre_input.text_input = ""
    director_input.text_input = ""
    genero_select.selectbox = ""
    compañia_input.text_input = ""

# Interfaz de Streamlit
st.sidebar.title("Agregar Nuevo Filme")

# Crear contenedores para los controles del formulario
form_container = st.sidebar.beta_container()

# Controles para ingresar los datos del nuevo filme
with form_container:
    st.subheader("Ingrese los datos del nuevo filme")
    nombre_input = st.text_input("Nombre del Filme")
    director_input = st.text_input("Director")
    genero_select = st.selectbox("Género", ["Acción", "Comedia", "Drama", "Ciencia Ficción", "Suspenso", "Animación", "Documental"])
    compañia_input = st.text_input("Compañía Productora")
    submit_button = st.form_submit_button("Insertar Filme")

# Botón para insertar el nuevo filme
if submit_button:
    # Validar que se hayan ingresado todos los datos
    if nombre_input.strip() and director_input.strip() and genero_select.strip() and compañia_input.strip():
        # Llamar a la función para insertar el nuevo filme en Firestore
        insertar_filme(nombre_input, director_input, genero_select, compañia_input)
    else:
        st.warning("Por favor ingresa todos los datos del filme.")