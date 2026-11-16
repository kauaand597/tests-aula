temperature = float(input("Por favor, digite um número: "))

inteira = int(temperature // 1)

decimal = round(temperature % 1, 2)
'''
em round(temperature - inteira, 2) a divisao 
entre a parte inteira e decimal é feita subtraindo
 a parte inteira do número original, e o resultado 
 é arredondado para duas casas decimais. Isso garante que a 
 parte decimal seja representada corretamente, 
 mesmo que o número original tenha mais de duas 
 casas decimais.


'''

print(f"Parte inteira: {inteira}")

if decimal == 0:
    print("Parte decimal: 0.00")
else:
    print(f"Parte decimal: {decimal}")


'''
a condicao de 
if decimal == 0: é usada para verificar
se a parte decimal do número é igual a zero.
Se a parte decimal for zero, o programa imprime 
"Parte decimal: 0.00", garantindo que a saída seja
formatada corretamente com duas casas decimais. 
Caso contrário, o programa imprime a parte decimal
normalmente, mantendo a formatação com duas casas
decimais.
'''