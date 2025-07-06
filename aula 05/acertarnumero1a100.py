import random

#TENTATIVA 1
maquina = random.randint(1, 10)
jogador = int(input("\nescolha um número de 1 a 10: "))
print(f'''eu escolhi: {maquina}\nvocê escolheu: {jogador}\n''')


if jogador == maquina:
    print("você acertou. programa encerrado.")
else:
    if jogador > maquina:
        print("você chutou ALTO! O número era menor.")
    else:
        print("você chutou BAIXO! O número era maior.")
    
    #TENTATIVA 2
    jogador = int(input("escolha um número de 1 a 10: "))
    if jogador == maquina:
        print("você acertou. programa encerrado.")
    else:
        if jogador > maquina:
            print("você chutou ALTO! O número era menor.")
        else:
            print("você chutou BAIXO! O número era maior.")
        
        #TENTATIVA 3
        jogador = int(input("escolha um número de 1 a 10: "))
        if jogador == maquina:
            print("você acertou. programa encerrado.")
        else:
            if jogador > maquina:
                print("você chutou ALTO! O número era menor.")
            else:
                print("você chutou BAIXO! O número era maior.")
