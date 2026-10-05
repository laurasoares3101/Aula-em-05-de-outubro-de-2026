##5 – F.U.P que calcule a média dos números digitados pelo usuário, se eles forem pares. Sendo que são 5 números.


soma = 0
quantidade = 0

for i in range(5):
    numero = int(input("Digite um número: "))
    
    if numero % 2 == 0:
        soma = soma + numero
        quantidade = quantidade + 1

if quantidade > 0:
    media = soma / quantidade
    print("Média dos números pares:", media)
else:
    print("Nenhum número par foi digitado.")