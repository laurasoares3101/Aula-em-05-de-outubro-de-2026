##4 – F.U.P para informar 10 números e no final, mostrar a quantidade de números pares, a quanƟdade de números ímpares, a soma dos números pares e a soma dos números ímpares...

pares = 0
impares = 0
soma_pares = 0
soma_impares = 0

for i in range(10):
    numero = int(input("Digite um número: "))
    
    if numero % 2 == 0:
        pares = pares + 1
        soma_pares = soma_pares + numero
    else:
        impares = impares + 1
        soma_impares = soma_impares + numero

print("Quantidade de pares:", pares)
print("Soma dos pares:", soma_pares)
print("Quantidade de ímpares:", impares)
print("Soma dos ímpares:", soma_impares)