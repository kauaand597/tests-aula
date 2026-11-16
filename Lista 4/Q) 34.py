# Escreva sua solução aqui
def no_vowels(my_string):
    vogais = ("a", "e", "i", "o", "u")
    sem_vogais = ""
    for letra in my_string:
        if letra not in vogais:
            sem_vogais += letra
    return sem_vogais
