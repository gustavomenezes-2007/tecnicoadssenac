cargo = str(input("informe seu cargo: ")).upper()

while cargo not in ["VENDEDOR", "GERENTE", "RH"]:
    cargo = str(input("cargo INVÁLIDO. insira um cargo VÁLIDO: ")).upper()

salario = float(input("informe seu salário: "))

print("\n--- SISTEMA DA LOJA ---")
if cargo == "gerente":
    bonus = (salario) + (salario*0.20)
elif cargo == "vendedor":
    bonus = (salario) + (salario*0.15)
elif cargo == "rh":
    bonus = (salario) + (salario*0.10)
print(f'''
você é o {cargo} da loja 
seu salário é de R${salario} 
mas com bônus de 20% será de R${bonus:.2f}''')
