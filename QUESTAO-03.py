listaTodos = []

soma = 0
mult = 1

for i in range(10):
    numero = int(input("Digite um número: "))
    listaTodos.append(numero)
    mult = mult * numero
    soma = soma + numero

print("A soma de todos os numeros: ", soma)
print("A multiplicacao de todos os numeros: ", mult)
print("A lista de todos os numeros: ", listaTodos)