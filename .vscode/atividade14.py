numero = int(input("Digite o número da tabuada que você quer ver: "))

print(f"\nTabuada do {numero}:\n")

for i in range(0, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")