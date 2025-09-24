'''8 - Crie um programa que armazene nomes de países e suas capitais em um dicionário. O usuário digita o nome do país e o programa mostra a capital correspondente.
Se o país não estiver no dicionário, o programa deve informar que a capital não está disponível.'''

paises_capitais = {
    "Brasil": "Brasília",   
    "Argentina": "Buenos Aires",
    "França": "Paris",
    "Japão": "Tóquio",
    "Canadá": "Ottawa"
}
pais = input("Digite o nome de um país: ")
capital = paises_capitais.get(pais)
if capital:
    print(f"A capital de {pais} é {capital}.")
else:
    print(f"Desculpe, a capital de {pais} não está disponível.")
