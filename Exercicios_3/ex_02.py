'''2 - Crie um programa que solicite um número ao usuário e exiba a tabuada desse número de 1 a 10, utilizando a estrutura de repetição for.'''

numero = int(input("Digite um número para ver a tabuada: "))
print(f"Tabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    