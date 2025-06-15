from exceptions.erros import EmprestimoNaoEncontradoError


class Usuario:
    def __init__(self, nome: str, email: str):
        self.nome = nome
        self.email = email
        self.emprestimos = []

    def adicionar_emprestimo(self, emprestimo):
        self.emprestimos.append(emprestimo)

    def concluir_emprestimo(self, titulo: str):
        for emprestimo in self.emprestimos:
            if emprestimo.livro.titulo == titulo and emprestimo.status == "ativo":
                emprestimo.concluir()
                return
        raise EmprestimoNaoEncontradoError(f"Empréstimo ativo para '{titulo}' não encontrado.")


# ================================
# # MELHORIAS:
#  SRP — Gerencia dados e empréstimos do usuário.
#  Preparado para OCP e extensão futura.
# ================================