for i in range(5):
    numero = float(input("digite um número: "))
    if i == 0:
        menor = numero
    else:
        if numero < menor:
            menor = numero

print(f"o menor número é {menor}")
