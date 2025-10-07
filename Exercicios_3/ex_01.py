'''1 - Crie um programa que solicite ao usuário uma nota (de 0 a 10) e exiba uma mensagem dizendo se o aluno foi reprovado, em recuperação ou aprovado.
Use as estruturas de decisão if, elif e else.
'''
nota = float(input("Digite a nota do aluno (0 a 10): "))

if nota < 0 or nota > 10:
    print("Nota inválida. Por favor, insira uma nota entre 0 e 10.")
elif nota < 5:
    print("Aluno reprovado.")
elif 5 <= nota < 7:
    print("Aluno em recuperação.")
else:
    print("Aluno aprovado.")

    