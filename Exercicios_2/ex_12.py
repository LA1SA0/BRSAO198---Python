'''4- Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

* Distância percorrida: 300 km
* Combustível gasto: 25 litros
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.'''

print("Calculadora de Consumo de Combustível")

distancia = 300  # em km
combustivel = 25  # em litros
consumo_medio = distancia / combustivel

print(f"Distância percorrida: {distancia} km")
print(f"Combustível gasto: {combustivel} litros")
print(f"Consumo médio: {consumo_medio:.2f} km/l")
if consumo_medio >= 12:
    print("Consumo eficiente.")
else:
    print("Consumo ineficiente.")
    