'''2- Calculadora de IMC
Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa. 
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário, 
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.'''

print("Calculadora de IMC")

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    classificacao = "Abaixo do peso"
    saudavel = False
elif 18.5 <= imc < 25:
    classificacao = "Peso normal"
    saudavel = True
elif 25 <= imc < 30:
    classificacao = "Sobrepeso"
    saudavel = False
else:
    classificacao = "Obesidade"
    saudavel = False

print(f"Classificação: {classificacao}")
if saudavel:
    print("Você está saudável.")
else:
    print("Você não está saudável.")
