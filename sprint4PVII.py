# Campo de texto para ingresar el título de la película a buscar
titulo_busqueda = st.sidebar.text_input("Buscar por Título")

# Botón de comando para realizar la búsqueda
if st.sidebar.button("Buscar", key="buscar_button"):
    # Convertir el título de búsqueda a minúsculas
    titulo_busqueda = titulo_busqueda.lower()

    # Filtrar los filmes que contengan el título de búsqueda (sin importar mayúsculas o minúsculas)
    filmes_coincidentes = [filme.to_dict() for filme in db.collection(u'peliculas').get() if titulo_busqueda in filme.to_dict()['name'].lower()]



    # Mostrar los datos en una tabla si se encontraron filmes coincidentes
    if filmes_coincidentes:
        # Mostrar el total de registros encontrados
        st.write(f"Total de filmes mostrados: {len(filmes_coincidentes)}")
        df_filmes_coincidentes = pd.DataFrame(filmes_coincidentes)
        st.write(df_filmes_coincidentes)
    else:
        st.write("No se encontraron filmes con ese título.")