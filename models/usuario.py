from exceptions.erros import EmprestimoNaoEncontradoError


class Usuario:
    """
    Representa um usuário da biblioteca.

    Atributos:
        nome (str): Nome completo do usuário.
        email (str): E-mail do usuário.
        emprestimos (list): Lista de objetos Emprestimo ativos do usuário.
    """

    def __init__(self, nome: str, email: str):
        """
        Inicializa um novo usuário com uma lista de empréstimos vazia.

        Args:
            nome (str): Nome do usuário.
            email (str): E-mail do usuário.
        """
        self.nome = nome
        self.email = email
        self.emprestimos = []

    def adicionar_emprestimo(self, emprestimo):
        """
        Adiciona um novo empréstimo à lista do usuário.

        Args:
            emprestimo (Emprestimo): O objeto de empréstimo a ser adicionado.
        """
        self.emprestimos.append(emprestimo)

    def concluir_emprestimo(self, titulo_livro):
        """
        Marca como concluído o empréstimo de um livro específico.

        Args:
            titulo_livro (str): O título do livro a ser devolvido.

        Raises:
            EmprestimoNaoEncontradoError: Se o empréstimo não for encontrado na lista do usuário.
        """
        for emprestimo in self.emprestimos:
            if emprestimo.livro.titulo == titulo_livro and not emprestimo.concluido:
                emprestimo.concluir()
                return
        raise EmprestimoNaoEncontradoError(f"Empréstimo do livro '{titulo_livro}' não encontrado para o usuário {self.nome}.")


# ================================
# # MELHORIAS:
#  SRP — Gerencia dados e empréstimos do usuário.
#  Preparado para OCP e extensão futura.
# ================================