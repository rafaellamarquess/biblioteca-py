from models.livro import Livro
from models.usuario import Usuario
from models.emprestimo import Emprestimo
from exceptions.erros import (
    LivroNaoEncontradoError,
    UsuarioNaoEncontradoError
)

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []
        

            #  CRUD simples de Livros
    def adicionar_livro(self, titulo: str, autor: str, ano: int):
        self.livros.append(Livro(titulo, autor, ano))

    def buscar_livro(self, titulo: str):
        for livro in self.livros:
            if livro.titulo == titulo:
                return livro
        raise LivroNaoEncontradoError(f"Livro '{titulo}' não encontrado.")


        # CRUD  simples de Usuários 
    def registrar_usuario(self, nome: str, email: str):
        self.usuarios.append(Usuario(nome, email))

    def buscar_usuario(self, email: str):
        for usuario in self.usuarios:
            if usuario.email == email:
                return usuario
        raise UsuarioNaoEncontradoError(f"Usuário '{email}' não encontrado.")
    
        #  Empréstimos
    def emprestar_livro(self, titulo: str, email: str):
        livro = self.buscar_livro(titulo)
        usuario = self.buscar_usuario(email)

        livro.emprestar()
        emprestimo = Emprestimo(livro)
        usuario.adicionar_emprestimo(emprestimo)

    def devolver_livro(self, titulo: str, email: str):
        livro = self.buscar_livro(titulo)
        usuario = self.buscar_usuario(email)

        usuario.concluir_emprestimo(titulo)
        livro.devolver()


# Retorna uma lista de livros disponíveis
    def listar_livros_disponiveis(self):
        return [
            f"{livro.titulo} - {livro.autor} ({livro.ano})"
            for livro in self.livros if livro.disponivel
        ]

# Retorna dados dos usuários e seus empréstimos
    def listar_usuarios(self):
        resultado = []
        for usuario in self.usuarios:
            info = f"{usuario.nome} ({usuario.email})"
            emprestimos = [
                f"  - {e.livro.titulo} ({e.status})"
                for e in usuario.emprestimos
            ]
            resultado.append((info, emprestimos))
        return resultado



# ================================
# MELHORIAS:
#  SRP — Ooordena operações e não guarda lógica interna das entidades.
#  DIP — Depende das abstrações das entidades.
#  ISP/OCP — Preparada para expansão e extensão.
# ================================