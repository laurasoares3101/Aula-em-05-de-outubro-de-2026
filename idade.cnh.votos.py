##2 – F.U.P para informar o nome, ano de nascimento e ano atual. Deverá calcular a idade. (idade = anoatual – anonascimento). Se a idade for 18 anos ou mais, exibir mensagem: Voce já é de maior e pode fazer a carteira de motorista. Se a idade for menor que 18 e maior ou igual a 16, exibir a mensagem: Voce já pode votar. 

nome = input("Digite o seu nome: ")
ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))
idade = ano_atual - ano_nascimento

print(f"\nNome: {nome}")
print(f"Idade: {idade} anos")

if idade >= 18:
    print("Voce já é de maior e pode fazer a carteira de motorista.")
elif idade >= 16:
    print("Voce já pode votar.")