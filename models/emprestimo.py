import datetime

class Emprestimo:
    """
    Representa um empréstimo de livro feito por um usuário.

    A classe armazena o livro emprestado, a data do empréstimo
    e o status (ativo ou devolvido).
    """

    def __init__(self, livro):
        """
        Inicializa um novo empréstimo com o status 'ativo' e a data atual.

        Args:
            livro (Livro): Instância do livro emprestado.
        """
        self.livro = livro
        self.data = datetime.date.today()
        self.status = "ativo"

    def concluir(self):
        """
        Marca o empréstimo como 'devolvido'.
        """
        self.status = "devolvido"



# ================================
# MELHORIAS:
#  SRP — Responsável apenas por representar um empréstimo.
# ================================
