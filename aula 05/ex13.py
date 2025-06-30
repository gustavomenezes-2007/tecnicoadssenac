# Cenário 2 - Crie um menu de um sistema de RH que contém as opções:

# 1 - Cadastro de Vendedor
# 2 - Cadastro de Gerente
# 3 - Cadastro de Cliente

# Para o vendedor peça as informações nome, cpf, idade e cidade
# Para o gerente peça as informações nome, cpf, idade, cidade e salario
# Para o cliente peça as informações nome, cpf, idade, endereço e telefone

print('''
--- SISTEMA DE CADASTRO ---
1 - cadastro de vendedor
2 - cadastro de gerente
3 - cadastro de cliente
''')

user = int(input("digite sua opção [1, 2, 3]: "))

if user == 1:
    nome = str(input("digite seu nome: "))
    cpf = str(input("digite seu cpf: "))
    idade = int(input("digite sua idade: "))
    cidade = str(input("digite sua cidade: "))
    print(f'''
VOCÊ É O VENDEDOR DA LOJA
seu nome é {nome}
seu cpf é {cpf}
sua idade é {idade}
sua cidade é {cidade}
''')

elif user == 2:
    nome = str(input("digite seu nome: "))
    cpf = str(input("digite seu cpf: "))
    idade = int(input("digite sua idade: "))
    cidade = str(input("digite sua cidade: "))
    salario = float(input("qual é seu salário: R$"))
    print(f'''
VOCÊ É O GERENTE DA LOJA
seu nome é {nome}
seu cpf é {cpf}
sua idade é {idade}
sua cidade é {cidade}
seu salário é {salario}
''')

elif user == 3:
    nome = str(input("digite seu nome: "))
    cpf = str(input("digite seu cpf: "))
    idade = int(input("digite sua idade: "))
    endereco = str(input("digite seu endereço: "))
    telefone = int(input("digite seu telefone: "))
    print(f'''
VOCÊ É O CLIENTE DA LOJA
seu nome é {nome}
seu cpf é {cpf}
sua idade é {idade}
seu endereço é {endereco}
seu telefone é: {telefone}
''')
