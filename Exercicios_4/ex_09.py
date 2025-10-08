'''9 - Solicite ao usuário números inteiros até que ele digite "0". Armazene os positivos e negativos separadamente em duas listas. Ignore valores não inteiros com try/except. No final, mostre quantos positivos e negativos foram inseridos.'''

positivos = []
negativos = []

while True:
    entrada = input("Digite um número inteiro (ou '0' para terminar): ").strip()
    if entrada == "0":
        break
    try:
        numero = int(entrada)
        if numero > 0:
            positivos.append(numero)
        elif numero < 0:
            negativos.append(numero)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro válido.")

print(f"Números positivos inseridos: {len(positivos)}")
print(f"Números negativos inseridos: {len(negativos)}")
print(f"Lista de números positivos: {positivos}")
print(f"Lista de números negativos: {negativos}")

