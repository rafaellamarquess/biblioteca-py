import datetime


class Emprestimo:
    """
    Representa um empréstimo de um livro, armazenando o livro associado,
    a data do empréstimo e seu status (ativo ou devolvido).
    """

    def __init__(self, livro):
        """
        Inicializa um novo empréstimo para um livro, definindo a data atual
        e status como "ativo".

        Args:
            livro: Instância do livro que está sendo emprestado.
        """
        self.livro = livro
        self.data = datetime.date.today()
        self.status = "ativo"

    def concluir(self):
        """
        Marca o empréstimo como concluído, alterando o status para "devolvido".
        """
        self.status = "devolvido"


# ================================
# MELHORIAS:
#  SRP — Responsável apenas por representar um empréstimo.
# ================================
