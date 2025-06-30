# Cenário 1 - Crie um menu de atendimento que exibe pelo menos 4 opções de serviços de uma operadora telefônica,
# peça ao usuário para escolher um item desse menu e exiba uma resposta de acordo com o menu escolhido.

print('''
--- MENU DE ATENDIMENTO ---
1 - CADASTRAR CHIP
2 - CANCELAR PLANO
3 - SAC
4 - FALAR COM ATENDENTE
5 - SAIR
''')

usuario = int(input("escolha uma opção [1, 2, 3, 4, 5]: "))

while usuario < 5 and usuario > 0:
    if usuario == 1:
        print("você escolheu a opção CADASTRAR CHIP")
    elif usuario == 2:
        print("você escolheu a opção CANCELAR PLANO")
    elif usuario == 3:
        print("você escolheu a opção SAC")
    elif usuario == 4:
        print("você escolheu a opção FALAR COM ATENDENTE")
    elif usuario == 5:
        print("você escolheu a opção SAIR. atendimento encerrado.")
    else:
        print("opção inávlida.")
print("você escolheu a opção SAIR. atendimento encerrado.")
