# ========================
# EXCEÇÕES CUSTOMIZADAS
# ========================

class BibliotecaError(Exception):
    """Erro genérico da biblioteca."""


class LivroNaoDisponivelError(BibliotecaError):
    pass


class LivroNaoEncontradoError(BibliotecaError):
    pass


class UsuarioNaoEncontradoError(BibliotecaError):
    pass


class EmprestimoNaoEncontradoError(BibliotecaError):
    pass
