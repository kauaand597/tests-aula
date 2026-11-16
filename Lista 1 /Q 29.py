# Corrigir o programa
pontos = int(input("Quantos pontos estão no seu cartão? "))
if pontos < 100:
    pontos = pontos * 1.1
    print("Seu bônus é de 10 %")
 
else:
    pontos >= 100
    pontos= pontos * 1.15
    print("Seu bônus é de 15 %")
 
print(f"Agora você tem {pontos} pontos")