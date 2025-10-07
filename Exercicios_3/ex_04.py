'''4 - Crie um programa que continue pedindo uma senha ao usuário até que ele digite a senha correta. Quando a senha correta for digitada, o programa mostra uma mensagem de sucesso e interrompe o loop com break.'''

senha_correta = "senha123"
while True:
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        print("Senha correta! Acesso concedido.")
        break
    else:
        print("Senha incorreta. Tente novamente.")

        