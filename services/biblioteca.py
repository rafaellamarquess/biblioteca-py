from models.livro import Livro
from models.usuario import Usuario
from models.emprestimo import Emprestimo
from exceptions.erros import (
    LivroNaoEncontradoError,
    UsuarioNaoEncontradoError
)

class Biblioteca:
    """
    Representa uma biblioteca que gerencia livros, usuários e empréstimos.

    Responsável por operações CRUD simples de livros e usuários, bem como
    controle de empréstimos e devoluções de livros.
    """

    def __init__(self):
        """
        Inicializa a biblioteca com listas vazias de livros e usuários.
        """
        self.livros = []
        self.usuarios = []

    def adicionar_livro(self, titulo: str, autor: str, ano: int):
        """
        Adiciona um novo livro ao acervo da biblioteca.

        Args:
            titulo (str): Título do livro.
            autor (str): Autor do livro.
            ano (int): Ano de publicação do livro.
        """
        self.livros.append(Livro(titulo, autor, ano))

    def buscar_livro(self, titulo: str):
        """
        Busca um livro pelo título no acervo da biblioteca.

        Args:
            titulo (str): Título do livro a ser buscado.

        Returns:
            Livro: Instância do livro encontrado.

        Raises:
            LivroNaoEncontradoError: Se o livro com o título especificado não for encontrado.
        """
        for livro in self.livros:
            if livro.titulo == titulo:
                return livro
        raise LivroNaoEncontradoError(f"Livro '{titulo}' não encontrado.")

    def registrar_usuario(self, nome: str, email: str):
        """
        Registra um novo usuário na biblioteca.

        Args:
            nome (str): Nome do usuário.
            email (str): Email do usuário.
        """
        self.usuarios.append(Usuario(nome, email))

    def buscar_usuario(self, email: str):
        """
        Busca um usuário pelo email.

        Args:
            email (str): Email do usuário a ser buscado.

        Returns:
            Usuario: Instância do usuário encontrado.

        Raises:
            UsuarioNaoEncontradoError: Se o usuário com o email especificado não for encontrado.
        """
        for usuario in self.usuarios:
            if usuario.email == email:
                return usuario
        raise UsuarioNaoEncontradoError(f"Usuário '{email}' não encontrado.")

    def emprestar_livro(self, titulo: str, email: str):
        """
        Realiza o empréstimo de um livro para um usuário.

        Procura o livro e o usuário, marca o livro como emprestado e registra
        o empréstimo no histórico do usuário.

        Args:
            titulo (str): Título do livro a ser emprestado.
            email (str): Email do usuário que irá receber o livro.

        Raises:
            LivroNaoEncontradoError: Se o livro não for encontrado.
            UsuarioNaoEncontradoError: Se o usuário não for encontrado.
            (Possíveis outras exceções internas ao chamar `livro.emprestar()`.)
        """
        livro = self.buscar_livro(titulo)
        usuario = self.buscar_usuario(email)

        livro.emprestar()
        emprestimo = Emprestimo(livro)
        usuario.adicionar_emprestimo(emprestimo)

    def devolver_livro(self, titulo: str, email: str):
        """
        Realiza a devolução de um livro emprestado por um usuário.

        Procura o livro e o usuário, atualiza o status do empréstimo para concluído
        e marca o livro como disponível novamente.

        Args:
            titulo (str): Título do livro a ser devolvido.
            email (str): Email do usuário que está devolvendo o livro.

        Raises:
            LivroNaoEncontradoError: Se o livro não for encontrado.
            UsuarioNaoEncontradoError: Se o usuário não for encontrado.
            (Possíveis outras exceções internas ao chamar `usuario.concluir_emprestimo()`.)
        """
        livro = self.buscar_livro(titulo)
        usuario = self.buscar_usuario(email)

        usuario.concluir_emprestimo(titulo)
        livro.devolver()

    def listar_livros_disponiveis(self):
        """
        Retorna uma lista formatada de livros que estão disponíveis para empréstimo.

        Returns:
            list[str]: Lista de strings com informações dos livros disponíveis
            no formato "Título - Autor (Ano)".
        """
        return [
            f"{livro.titulo} - {livro.autor} ({livro.ano})"
            for livro in self.livros if livro.disponivel
        ]

    def listar_usuarios(self):
        """
        Retorna uma lista dos usuários cadastrados com seus respectivos empréstimos.

        Returns:
            list[tuple]: Lista de tuplas, onde cada tupla contém:
                - info (str): Nome e email do usuário no formato "Nome (email)".
                - emprestimos (list[str]): Lista dos títulos dos livros emprestados e seus status.
        """
        resultado = []
        for usuario in self.usuarios:
            info = f"{usuario.nome} ({usuario.email})"
            emprestimos = [
                f"  - {e.livro.titulo} ({e.status})"
                for e in usuario.emprestimos
            ]
            resultado.append((info, emprestimos))
        return resultado
