def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    filme = {
        "name": name,
        "director": director,
        "year": year,
        "runtime": runtime
    }
    database.append(filme)