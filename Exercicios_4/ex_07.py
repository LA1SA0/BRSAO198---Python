''' - Crie um programa que permita que o usuário monte uma lista de compras digitando nomes de produtos. O usuário pode digitar até 10 itens. Se digitar "fim", o programa para imediatamente (break). Se o item for vazio (só apertar Enter), ele é ignorado com continue. Use try/except para garantir que apenas strings sejam inseridas.'''

lista_compras = []
for _ in range(10):
    try:
        item = input("Digite o nome do produto (ou 'fim' para terminar): ").strip()
        if item.lower() == "fim":
            break
        if item == "":
            continue
        lista_compras.append(item)
    except Exception as e:
        print("Erro ao inserir o item. Tente novamente.")

print("Lista de compras:", lista_compras)
