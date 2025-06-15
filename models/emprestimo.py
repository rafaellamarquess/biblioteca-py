import datetime


class Emprestimo:
    def __init__(self, livro):
        self.livro = livro
        self.data = datetime.date.today()
        self.status = "ativo"

    def concluir(self):
        self.status = "devolvido"



# ================================
# MELHORIAS:
#  SRP — Responsável apenas por representar um empréstimo.
# ================================