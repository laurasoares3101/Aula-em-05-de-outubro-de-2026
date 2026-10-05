##3 – F.U.P para informar 10 números e no final, mostrar o resultado da soma. Ex: Se for informado: 2, 4, 10.....Deverá somar esses números e mostrar o resultado. (Usar o for)

soma = 0
for i in range(1,11):
    numero = int(input(f"Informe o número: {i} "))
    soma = soma+numero
print(soma)
