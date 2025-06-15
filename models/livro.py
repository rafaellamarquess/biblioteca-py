from exceptions.erros import LivroNaoDisponivelError


class Livro:
    """
    Representa um livro no sistema da biblioteca.

    Atributos:
        titulo (str): Título do livro.
        autor (str): Autor do livro.
        disponivel (bool): Indica se o livro está disponível para empréstimo.
    """

    def __init__(self, titulo: str, autor: str):
        """
        Inicializa um novo livro como disponível.

        Args:
            titulo (str): O título do livro.
            autor (str): O autor do livro.
        """
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def emprestar(self):
        """
        Marca o livro como emprestado, tornando-o indisponível.
        Lança uma exceção se o livro já estiver emprestado.

        Raises:
            LivroNaoDisponivelError: Se o livro já estiver emprestado.
        """
        if not self.disponivel:
            raise LivroNaoDisponivelError(f"Livro '{self.titulo}' não está disponível.")
        self.disponivel = False

    def devolver(self):
        """
        Marca o livro como disponível novamente.
        """
        self.disponivel = True



# ================================
# MELHORIAS:
#  SRP — Responsável apenas pelos dados e estado do livro.
#  Encapsulamento — Disponibilidade controlada por métodos.
#  Preparado para OCP/LSP — Extensível.
# ================================