'''9 - Crie um programa onde o computador escolhe um número entre 1 e 10, e o usuário deve adivinhar qual é. O programa continua pedindo tentativas até que o usuário acerte. Use while, break e True para controlar o fluxo.'''
import random

numero = random.randint(1, 10)

while True:
    tentativa = int(input('Tente adivinhar o número que o computador escolheu entre 1 e 10: '))
    if tentativa == numero:
        print('Parabéns! Você acertou!')
        break
    else:
        print('Tente novamente!')

        