from services.biblioteca import Biblioteca

biblioteca = Biblioteca()

# Adiciona livros
biblioteca.adicionar_livro("Clean Code", "Robert C. Martin", 2008)
biblioteca.adicionar_livro("Arquitetura Limpa", "Robert C. Martin", 2017)

# Registra usuários
biblioteca.registrar_usuario("Rafaella", "rafa@dev.com")

# Faz um empréstimo
biblioteca.emprestar_livro("Clean Code", "rafa@dev.com")

# Lista livros disponíveis
print("Livros disponíveis:")
print(biblioteca.listar_livros_disponiveis())

# Devolve livro
biblioteca.devolver_livro("Clean Code", "rafa@dev.com")

# Verifica usuários e empréstimos
print("\nUsuários:")
for usuario, emprestimos in biblioteca.listar_usuarios():
    print(usuario)
    for e in emprestimos:
        print(e)
