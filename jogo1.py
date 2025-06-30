import random

maquina = random.choice(("pedra", "papel", "tesoura"))
player = str(input("escolha pedra, papel ou tesoura: ")).lower()

print(f'''
maquina escolheu: {maquina}
você escolheu: {player}

o resultado foi:
''')

if maquina == player:
    print("EMPATE!")
elif (player == "pedra" and maquina == "papel") or (player == "papel" and maquina == "tesoura") or (player == "tesoura" and maquina == "pedra"):
    print("você perdeu!")
else:
    print("você venceu!")
