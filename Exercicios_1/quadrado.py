'''10 - Crie uma função que receba um número como argumento e retorne o quadrado desse número. Depois, chame essa função passando um número digitado pelo usuário.'''

def calcular_quadrado(numero):
    return numero ** 2
try:
    numero_usuario = float(input("Digite um número para calcular o quadrado: "))
    resultado = calcular_quadrado(numero_usuario)
    print(f"O quadrado de {numero_usuario} é {resultado}.")

except ValueError:
    print("Por favor, digite um número válido.")
    