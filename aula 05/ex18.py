nome = str(input("digite seu nome: "))

if (len(nome) > 5) and (nome[0] in "aeiou"):
    print("nome válido!")
else:
    print("nome inválido.")
