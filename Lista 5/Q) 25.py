def older_people(people: list, year: int):
    result = []
    for nome, ano in people:
        if ano < year:
            result.append(nome)
    return result