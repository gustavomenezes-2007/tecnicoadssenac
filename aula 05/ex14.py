# Cenário 3 - Crie um sistema de lanchonete que exibe na tela pelo menos 5 opções de lanche contendo Código, Nome e Preço.
# Peça para que o usuário digite o código do lanche deseja e a quantidade. Exiba na tela o valor total da compra.

print('''
--- LANCHONETE ---
1 - MC LANCHE FELIZ - R$12,00
2 - SUSHI - R$1,00 (UNIDADE)
3 - BAURU - R$7,00
4 - SALGADO - R$4,00
5 - COXINHA - R$3,00
''')

lanche = int(input("digite sua opção [1, 2, 3, 4, 5]: "))
qtd = int(input("digite a quantidade que você quer: "))

if lanche == 1:
    print(f"\nvocê escolheu {qtd} MC LANCHE FELIZ. O total do pedido é: R${qtd*12:.2f}")
elif lanche == 2:
    print(f"você escolheu {qtd} SUHSHI. o total do pedido é: R${qtd*1:.2f}")
elif lanche == 3:
    print(f"você escolheu {qtd} BAURU. o total do pedido é: R${qtd*7:.2f}")
elif lanche == 4:
    print(f"você escolheu {qtd} SALGADO. total do pedido é: R${qtd*4:.2f}")
elif lanche == 5:
    print(f"você escolheu {qtd} COXINHA. o total do pedido é: R${qtd*3:.2f}")
