from exceptions.erros import LivroNaoDisponivelError


class Livro:
    """
    Representa um livro na biblioteca, contendo informações básicas
    e controle de disponibilidade para empréstimo.
    """

    def __init__(self, titulo: str, autor: str, ano: int):
        """
        Inicializa um novo livro com título, autor, ano e disponibilidade padrão como True.

        Args:
            titulo (str): Título do livro.
            autor (str): Nome do autor.
            ano (int): Ano de publicação do livro.
        """
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True

    def emprestar(self):
        """
        Marca o livro como emprestado, alterando seu status para indisponível.

        Raises:
            LivroNaoDisponivelError: Se o livro já não estiver disponível para empréstimo.
        """
        if not self.disponivel:
            raise LivroNaoDisponivelError(f"O livro '{self.titulo}' não está disponível.")
        self.disponivel = False

    def devolver(self):
        """
        Marca o livro como disponível, sinalizando que foi devolvido.
        """
        self.disponivel = True


# ================================
# MELHORIAS:
#  SRP — Responsável apenas pelos dados e estado do livro.
#  Encapsulamento — Disponibilidade controlada por métodos.
#  Preparado para OCP/LSP — Extensível.
# ================================
