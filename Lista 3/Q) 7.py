# Escreva sua solução aqui
n = int(input("Limite: "))

soma = 0
numero = 1
calculo = []

while soma < n:
    soma += numero
    calculo.append(numero)
    numero += 1
    
print("A soma consecutiva:", " + ".join(str(x) for x in calculo), "=",soma)
