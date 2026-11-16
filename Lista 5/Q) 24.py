def oldest_person(people: list):
    mais_velha = min(people, key=lambda pessoa: pessoa[1])
    return mais_velha[0]