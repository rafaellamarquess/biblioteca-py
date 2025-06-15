# ========================
# EXCEÇÕES CUSTOMIZADAS
# ========================

class BibliotecaError(Exception):
    """
    Exceção base para erros relacionados à biblioteca.

    Esta classe deve ser herdada por todas as exceções específicas
    do domínio da biblioteca para facilitar o tratamento genérico.
    """
    pass


class LivroNaoDisponivelError(BibliotecaError):
    """
    Exceção lançada quando um livro solicitado não está disponível para empréstimo.

    Pode ser usada para indicar que o livro está emprestado ou reservado.
    """
    pass


class LivroNaoEncontradoError(BibliotecaError):
    """
    Exceção lançada quando o livro buscado não é encontrado no acervo da biblioteca.
    """
    pass


class UsuarioNaoEncontradoError(BibliotecaError):
    """
    Exceção lançada quando o usuário buscado não está registrado na biblioteca.
    """
    pass


class EmprestimoNaoEncontradoError(BibliotecaError):
    """
    Exceção lançada quando um empréstimo específico não é encontrado.

    Pode ser usada para indicar que não existe registro de empréstimo
    para um dado usuário ou livro.
    """
    pass
