'''4 - Crie uma função em Python que receba um número como parâmetro e retorne o dobro desse número. Depois, chame essa função com um número fornecido pelo usuário. '''

def dobro(numero):
    return numero * 2

numero = int(input("Digite um número: "))
resultado = dobro(numero)
print(f"O dobro de {numero} é {resultado}.")



