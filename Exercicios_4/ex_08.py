'''8 - Crie um programa para registrar as temperaturas de vários dias. O usuário deve digitar a temperatura em graus Celsius (ex: 25.5). O programa continua coletando até que o usuário digite "fim" ou colete 7 temperaturas. Valores inválidos devem ser ignorados. Ao final, exiba a média das temperaturas registradas.'''

temperaturas = []
for _ in range(7):
    entrada = input("Digite a temperatura em graus Celsius (ou 'fim' para terminar): ").strip()
    if entrada.lower() == "fim":
        break
    try:
        temperatura = float(entrada)
        temperaturas.append(temperatura)
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")

if temperaturas:
    media = sum(temperaturas) / len(temperaturas)
    print(f"Média das temperaturas registradas: {media:.2f} °C")
else:
    print("Nenhuma temperatura válida foi registrada.")

    