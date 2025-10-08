'''6 - Peça ao usuário que digite 10 números inteiros. Armazene apenas os números pares válidos em uma lista. Use try/except para capturar erros, continue para ignorar números ímpares ou inválidos, e exiba a lista final ao terminar.'''

numeros_pares = []
for _ in range(10):
    try:
        numero = int(input("Digite um número inteiro: "))
        if numero % 2 != 0:
            continue
        numeros_pares.append(numero)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

print("Números pares válidos:", numeros_pares)

