'''- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
'''
print("Conversor de Temperatura")

temp = float(input("Digite a temperatura que deseja converter:  "))
unidade_origem = input("Digite a unidade de origem (C, F, K): ").upper()
unidade_destino = input("Digite a unidade de destino (C, F, K): ").upper()
resultado = None

if unidade_origem == 'C':
    if unidade_destino == 'F':
        resultado = (temp * 9/5) + 32
    elif unidade_destino == 'K':
        resultado = temp + 273.15
    elif unidade_destino == 'C':
        resultado = temp
    else:
        print("Unidade de destino inválida.")

elif unidade_origem == 'F':
    if unidade_destino == 'C':
        resultado = (temp - 32) * 5/9
    elif unidade_destino == 'K':
        resultado = (temp - 32) * 5/9 + 273.15
    elif unidade_destino == 'F':
        resultado = temp
    else:
        print("Unidade de destino inválida.")

elif unidade_origem == 'K':
    if unidade_destino == 'C':
        resultado = temp - 273.15
    elif unidade_destino == 'F':
        resultado = (temp - 273.15) * 9/5 + 32
    elif unidade_destino == 'K':
        resultado = temp
    else:
        print("Unidade de destino inválida.")

else:
    print("Unidade de origem inválida.")

if resultado is not None:
    print(f"{temp}°{unidade_origem} é igual a {resultado:.2f}°{unidade_destino}")

