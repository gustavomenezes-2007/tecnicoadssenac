# Pede o valor do saque
saque = int(input("Digite o valor do saque: "))

# Verifica se o valor é válido (positivo e divisível por 2, já que a menor nota é 2)
if saque <= 0 or saque % 2 != 0:
    print("Valor inválido! O saque deve ser positivo e múltiplo de 2.")
else:
    # Inicializa variáveis para contar as notas
    notas_100 = saque // 100  # Quantas notas de 100
    resto = saque % 100       # O que sobra depois das notas de 100

    notas_50 = resto // 50    # Quantas notas de 50 no resto
    resto = resto % 50        # O que sobra depois das notas de 50

    notas_20 = resto // 20    # Quantas notas de 20 no resto
    resto = resto % 20        # O que sobra depois das notas de 20

    notas_10 = resto // 10    # Quantas notas de 10 no resto
    resto = resto % 10        # O que sobra depois das notas de 10

    notas_5 = resto // 5      # Quantas notas de 5 no resto
    resto = resto % 5         # O que sobra depois das notas de 5

    notas_2 = resto // 2      # Quantas notas de 2 no resto

    # Mostra o resultado
    print(f'''
--- VOCÊ RECEBERÁ ---
{notas_100} notas de 100
{notas_50} notas de 50
{notas_20} notas de 20
{notas_10} notas de 10
{notas_5} notas de 5
{notas_2} notas de 2
''')
