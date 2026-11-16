def find_movies(database: list, search_term: str):
    resultados = []
    for filme in database:
        if search_term.lower() in filme["name"].lower():
            resultados.append(filme)
    return resultados