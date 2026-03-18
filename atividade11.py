estoque = {}
print ("Bem Vindo ao sistema de gestao de estoque desenvolvido por João Maciel")
while True:
    operacao = input ("deseja reagir a entrada e saída de produto? (digite'entrada ou saída') ou 'sair'").lower()

    if operacao not in ['entrada', 'saida', 'sair']:
        print("operacao inválida.")
        continue

    if operacao == 'sair':
        break
    produto = input("nome do produto:").strip()
    qtd = int(input("quantidade: "))
    
    if operacao == 'entrada': 
        estoque[produto] = estoque.get(produto, 0) + qtd
    elif operacao == 'saída':
        if estoque.get(produto, 0) >= qtd:
            estoque [produto]-= qtd
        else:
            print("erro:produto inexistente ou estoque insuficiente.")

print("\n Estoque Final ---")
for p, q in estoque.items():
    print(f"{p}: {q}")
    #adicione produtos (entrada)
#retire produtos (saída)