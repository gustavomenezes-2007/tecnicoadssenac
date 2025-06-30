n1 = int(input("digite o 1º numero: "))
n2 = int(input("digite o 2º numero: "))
n3 = int(input("digite o 3º numero: "))

if n1 > n2 and n1 > n3 and n2 > n3:
    maior = n1
    ordem = n1, n2, n3
elif n2 > n1 and n2 > n3 :
    maior = n2
else:
    maior = n3

print(f'''
--- NÚMEROS INSERIDOS ---
n1 = {n1}
n2 = {n2}
n3 = {n3}

maior = {maior}
ordem decrescente: {ordem}
''')
