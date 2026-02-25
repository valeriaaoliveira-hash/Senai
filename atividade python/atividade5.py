contador=0
soma=0
while contador < 4:
    contador+= 1
    nota = float(input (f"insira a {contador} nota: "))
    soma+=nota

media = soma/contador
print("a média final é ", media)
if media >= 7:
    print("aluno esta aprovado")
else:
    print("o aluno esta reprovado")