'''2-  Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.'''

import string

def eh_palindromo(texto):
    texto_limpo = ''.join(char.lower() for char in texto if char.isalnum())
    return texto_limpo == texto_limpo[::-1]
entrada_usuario = input("Digite uma palavra ou frase: ")
if eh_palindromo(entrada_usuario):
    print("Sim")
else:
    print("Não")
