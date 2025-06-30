import random

#TENTATIVA 1
maquina = random.randint(1, 10)
jogador = int(input("Escolha um número de 1 a 10: "))
print(f'Eu escolhi: {maquina}\nVocê escolheu: {jogador}\n')


if jogador == maquina:
    print("Parabéns, você ACERTOU! Jogo finalizado.")
else:
    if jogador > maquina:
        print("TENTATIVA 1 - Você chutou ALTO! O número era menor.")
    else:
        print("TENTATIVA 1 - Você chutou BAIXO! O número era maior.")

    #TENTATIVA 2
    jogador = int(input("Escolha outro número de 1 a 10: "))
    if jogador == maquina:
        print("Parabéns, você ACERTOU! Jogo finalizado.")
    else:
        if jogador > maquina:
            print("TENTATIVA 2 - Você chutou ALTO! O número era menor.")
        else:
            print("TENTATIVA 2 - Você chutou BAIXO! O número era maior.")
        
        #TENTATIVA 3
        jogador = int(input("Última tentativa! Escolha um número de 1 a 10: "))
        if jogador == maquina:
            print("Parabéns, você ACERTOU! Jogo finalizado.")
        else:
            if jogador > maquina:
                print("TENTATIVA 3 - Você chutou ALTO! O número era menor.")
            else:
                print("TENTATIVA 3 - Você chutou BAIXO! O número era maior.")
            print(f"Suas tentativas acabaram! O número era {maquina}.")
