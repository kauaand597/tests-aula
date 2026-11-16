n = int(input("Por favor, digite um número: "))

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i} x {j} = {i * j}")