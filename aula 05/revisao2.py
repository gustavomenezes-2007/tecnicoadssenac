while True:
    idade = int(input("digite sua idade: "))

    if idade <= 25:
        print(f"você é jovem, tem apenas {idade} anos. aproveite a vida garoto!\n")

    if idade >= 26 and idade <= 35:
        print(f"você é um homem adulto. tem {idade} anos. guarde dinheiro para o futuro!\n")

    if idade >= 36:
        print(f"você é idoso. tem {idade} anos. pegue o dinheiro que juntou e faça seu testamento.\n")
    
    seguir = str(input("quer continuar? [SIM] [NÃO]: ")).upper()
    
    while seguir != "SIM":
        seguir = str(input("opção inválida. digite apenas SIM ou NÃO: ")).upper()
        
        if seguir == "NÃO":
            print("ok, até logo!")
        