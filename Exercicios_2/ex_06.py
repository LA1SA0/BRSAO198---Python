'''6- Calculadora de Média Escolar
Enunciado:
Desenvolva um programa que solicite o nome de um aluno e suas 3 notas. O programa deve calcular a média e informar se o aluno foi aprovado (média >= 7), está em recuperação (5 <= média < 7) ou foi reprovado (média < 5).'''

print("Calculadora de Média Escolar")

nome_aluno = input("Digite o nome do aluno: ")
notas = []
for i in range(1, 4):
    nota = float(input(f"Digite a nota {i}: "))
    notas.append(nota)


media = sum(notas) / len(notas)
print(f"A média de {nome_aluno} é: {media:.2f}")

if media >= 7:
    print(f"{nome_aluno} foi aprovado.")
elif 5 <= media < 7:
    print(f"{nome_aluno} está em recuperação.")
else:
    print(f"{nome_aluno} foi reprovado.")

