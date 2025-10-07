'''5- Verificador de Número Primo
Enunciado:
Crie um programa que solicite um número inteiro positivo ao usuário e verifique se ele é um número primo. Um número primo só é divisível por 1 e por ele mesmo.
'''

print("Verificador de Número Primo")

num = int(input("Digite um número inteiro positivo: "))
if num <= 1:
    print("Por favor, digite um número inteiro positivo maior que 1.")
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} não é um número primo.")
            break
    else:
        print(f"{num} é um número primo.")

