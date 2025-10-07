'''6 - Crie um programa que simula a validação de uma senha usando um loop while True. O usuário tem no máximo 3 tentativas para acertar a senha correta. Use break para encerrar o loop quando a senha for correta ou quando o número máximo de tentativas for atingido.'''

senha_correta = "senha123"
tentativas = 0
max_tentativas = 3
while True:
    senha_usuario = input("Digite a senha: ")
    tentativas += 1
    if senha_usuario == senha_correta:
        print("Senha correta! Acesso concedido.")
        break
    else:
        print("Senha incorreta.")
    if tentativas >= max_tentativas:
        print("Número máximo de tentativas atingido. Acesso negado.")
        break
    