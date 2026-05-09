print("=" * 50)
print("Sistema de autenticação 2000 🖥️")
print("=" * 50)


nomeUsuario = input("Digite seu nome: ")
senhaUsuario = input("Digite a sua senha: ")

if nomeUsuario == "Arthur" and senhaUsuario == "1234":
    print("\nAcesso liberado!")
else:
    print("\nAcesso negado! O usuário ou senha estão incorretos.")
