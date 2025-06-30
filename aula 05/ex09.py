tempf = int(input("digite a temperatura em fahrenheit: "))
tempc = (tempf-32) * (5/9)

print(f"a temperatura convertida para celsius é: {tempc:.2f}C°")

if (tempc >= 40):
    print("Tá quente heeein")
elif (tempf >= 20):
    print("tá de boa!")
