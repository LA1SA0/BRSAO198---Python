'''4 - Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia.'''

from datetime import datetime

def calcular_dias_vivo(data_nascimento):
    data_atual = datetime.now()
    dias_vivo = (data_atual - data_nascimento).days
    return dias_vivo
try:
    data_nascimento_str = input("Digite sua data de nascimento (DD/MM/AAAA): ")
    data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y")
    
    if data_nascimento > datetime.now():
        print("A data de nascimento não pode ser no futuro.")
    else:
        dias_vivo = calcular_dias_vivo(data_nascimento)
        print(f"Você está vivo há {dias_vivo} dias.")

except ValueError:
    print("Formato de data inválido. Por favor, use DD/MM/AAAA.")