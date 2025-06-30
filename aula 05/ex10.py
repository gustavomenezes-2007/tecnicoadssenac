nome = str(input("digite seu nome: ")).upper()
n1 = float(input("digite a primeira nota: "))
n2 = float(input("digite a segunda nota: "))
n3 = float(input("digite a terceira nota: "))
n4 = float(input("digite a quarta nota: "))

media = round(((n1 + n2 + n3 + n4) / 4), 1)

print(f'''
--- MÉDIA DE {nome} ---
nota 1: {n1}
nota 2: {n2}
nota 3: {n3}
nota 4: {n4}

média: {media}
''')

if media >= 7 and media <= 10:
    print("resultado: APROVADO!")
elif media == 5 or media == 6:
    print("resultado: RECUPERAÇÃO!")
elif media >= 0 and media <= 4:
    print("resultado: REPROVADO!")
else:
    print("média inválida")
