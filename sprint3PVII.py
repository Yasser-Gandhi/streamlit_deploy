# Checkbox para visualizar todos los filmes recuperados
if st.sidebar.checkbox("Mostrar Todos los Filmes"):
    # Obtener todos los filmes de la base de datos
    todos_los_filmes = db.collection(u'peliculas').get()

    # Crear una lista para almacenar los datos de todos los filmes
    data = []

    # Recorrer todos los filmes y obtener sus datos
    for filme in todos_los_filmes:
        filme_data = filme.to_dict()
        data.append(filme_data)

    # Crear un DataFrame a partir de los datos obtenidos
    df_todos_los_filmes = pd.DataFrame(data)

    # Mostrar todos los filmes en forma de tabla
    st.header("Todos los filmes:")
    st.write(df_todos_los_filmes)