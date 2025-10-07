'''8- Calculadora Simples
Enunciado:
Crie um programa que simule uma calculadora simples. O usuário deve informar dois números e a operação desejada (+, -, *, /) e o programa deve exibir o resultado da operação.'''

print("Calculadora Simples")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação desejada (+, -, *, /): ")
resultado = None

if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2     
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida.")
if resultado is not None:
    print(f"O resultado de {num1} {operacao} {num2} é: {resultado}")

