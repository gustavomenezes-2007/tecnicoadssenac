nome = str(input("digite seu nome: ")).upper()
n1 = float(input("digite sua 1º nota: "))
n2 = float(input("digite sua 2º nota: "))
n3 = float(input("digite sua 3º nota: "))
n4 = float(input("digite sua 4º nota: "))
 
print(f'''
--- NOTAS DE {nome} ---
nota 1: {n1}
nota 2: {n2}
nota 3: {n3}
nota 4: {n4}

sua média foi: {(n1 + n2 + n3 + n4) / 4:.1f}
''')
