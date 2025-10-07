'''8 - Crie um programa que solicita a nota de avaliação de um restaurante (de 0 a 5) e exibe a quantidade de estrelas equivalente, juntamente com uma mensagem personalizada. Use if, elif e else para lidar com diferentes faixas de nota.'''
nota = float(input("Digite a nota do restaurante (0 a 5): "))
if nota < 0 or nota > 5:
    print("Nota inválida. Por favor, insira uma nota entre 0 e 5.")
elif nota >= 4.5:
    estrelas = "★★★★★"
    mensagem = "Excelente! Obrigado pela sua avaliação."
elif nota >= 3.5:
    estrelas = "★★★★☆"
    mensagem = "Muito bom! Agradecemos seu feedback."
elif nota >= 2.5:
    estrelas = "★★★☆☆"
    mensagem = "Bom, mas há espaço para melhorias."
elif nota >= 1.5:
    estrelas = "★★☆☆☆"
    mensagem = "Ruim. Vamos trabalhar para melhorar."
else:
    estrelas = "★☆☆☆☆"
    mensagem = "Péssimo. Lamentamos sua experiência."
    
print(f"Nota: {nota} - {estrelas}")
print(mensagem)