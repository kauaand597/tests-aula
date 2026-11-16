pontos = int(input("Quantos pontos [0-100]: "))


if pontos>100 or pontos<0:
    print("Nota: impossível!")
elif pontos <50:
    print("Nota: reprovado")
elif pontos>= 50 and pontos <60:
    print("Nota: 1") 
elif pontos>= 60 and pontos <70:
    print("Nota: 2") 
elif pontos>= 70 and pontos <80:
    print("Nota: 3") 
elif pontos>= 80 and pontos <90:
    print("Nota: 4") 
elif pontos>= 90 and pontos <=100:
    print("Nota: 5") 
