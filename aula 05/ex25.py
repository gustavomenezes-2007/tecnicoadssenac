num = int(input("digite um número: "))

for i in range(1, num+1):
    soma = num * (num+1)/2
print(f"a soma de todos os números de 1 até {num} é: {soma:.0f}!")
