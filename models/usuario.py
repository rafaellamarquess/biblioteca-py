from exceptions.erros import EmprestimoNaoEncontradoError
from models.emprestimo import Emprestimo  # ajuste o caminho conforme sua estrutura real

class Usuario:
    """
    Representa um usuário da biblioteca, contendo informações pessoais
    e controle dos empréstimos de livros associados a ele.
    """

    def __init__(self, nome: str, email: str):
        """
        Inicializa um novo usuário com nome, email e lista de empréstimos vazia.

        Args:
            nome (str): Nome do usuário.
            email (str): Email do usuário.
        """
        self.nome = nome
        self.email = email
        self.emprestimos: list[Emprestimo] = []

    def adicionar_emprestimo(self, emprestimo: Emprestimo):
        """
        Adiciona um novo empréstimo à lista de empréstimos do usuário.

        Args:
            emprestimo (Emprestimo): Instância de empréstimo a ser adicionada.
        """
        self.emprestimos.append(emprestimo)

    def concluir_emprestimo(self, titulo: str):
        """
        Conclui (finaliza) o empréstimo ativo de um livro pelo título.

        Procura na lista de empréstimos por um empréstimo ativo com o título informado.
        Se encontrado, chama o método concluir() do empréstimo.
        Caso contrário, levanta a exceção EmprestimoNaoEncontradoError.

        Args:
            titulo (str): Título do livro cujo empréstimo deve ser concluído.

        Raises:
            EmprestimoNaoEncontradoError: Se não houver empréstimo ativo com o título.
        """
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
