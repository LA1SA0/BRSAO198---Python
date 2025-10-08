'''3 - Crie um programa que verifique se uma senha é forte. Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um número. O programa deve continuar pedindo senhas até que uma válida seja inserida ou o usuário digite 'sair'.'''

def verificar_senha():
    while True:
        senha = input("Digite uma senha (ou 'sair' para encerrar): ")

        if senha.lower() == 'sair':
            print("Programa encerrado.")
            break

        try:
            if len(senha) < 8:
                raise ValueError("A senha deve ter pelo menos 8 caracteres.")
            if not any(char.isdigit() for char in senha):
                raise ValueError("A senha deve conter pelo menos um número.")

            print("Senha forte! Programa encerrado.")
            break

        except ValueError as ve:
            print(f"Erro: {ve}. Por favor, tente novamente.")
verificar_senha()


