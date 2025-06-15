from exceptions.erros import LivroNaoDisponivelError


class Livro:
    def __init__(self, titulo: str, autor: str, ano: int):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True

    def emprestar(self):
        if not self.disponivel:
            raise LivroNaoDisponivelError(f"O livro '{self.titulo}' não está disponível.")
        self.disponivel = False

    def devolver(self):
        self.disponivel = True



# ================================
# MELHORIAS:
#  SRP — Responsável apenas pelos dados e estado do livro.
#  Encapsulamento — Disponibilidade controlada por métodos.
#  Preparado para OCP/LSP — Extensível.
# ================================