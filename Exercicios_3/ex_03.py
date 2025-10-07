'''3 - Crie um programa que faça uma contagem regressiva a partir de um número informado pelo usuário até 0. O programa deve mostrar cada número da contagem e, ao final, exibir "FIM!".'''

numero = int(input("Digite um número para iniciar a contagem regressiva: "))
print("Contagem regressiva:")
for i in range(numero, -1, -1):
    print(i)
print("FIM!")

