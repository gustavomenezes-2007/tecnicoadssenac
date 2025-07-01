num = int(input("digite um número: "))
fat = 1

for i in range(1, num+1):
    fat *= i
print(f"o fatorial de {num} é {fat}")
