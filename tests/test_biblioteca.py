import pytest
from services.biblioteca import Biblioteca
from exceptions.erros import (
    LivroNaoDisponivelError,
    LivroNaoEncontradoError,
    UsuarioNaoEncontradoError
)


def setup_biblioteca():
    """
    Cria e configura uma instância de Biblioteca com dados iniciais:
    - 2 livros: 'Python Básico' e 'POO Avançado'
    - 1 usuário: 'Rafaella' (rafa@dev.com)
    """
    b = Biblioteca()
    b.adicionar_livro("Python Básico", "Guido", 2020)
    b.adicionar_livro("POO Avançado", "Alan Kay", 2019)
    b.registrar_usuario("Rafaella", "rafa@dev.com")
    return b


def test_emprestar_livro():
    """
    Testa o empréstimo de um livro disponível.
    O livro deve deixar de aparecer na lista de livros disponíveis.
    """
    b = setup_biblioteca()
    b.emprestar_livro("Python Básico", "rafa@dev.com")
    livros_disp = b.listar_livros_disponiveis()
    assert "Python Básico" not in " ".join(livros_disp)


def test_emprestar_livro_indisponivel():
    """
    Testa o caso em que um livro já emprestado não pode ser emprestado novamente.
    Deve lançar LivroNaoDisponivelError.
    """
    b = setup_biblioteca()
    b.emprestar_livro("Python Básico", "rafa@dev.com")
    with pytest.raises(LivroNaoDisponivelError):
        b.emprestar_livro("Python Básico", "rafa@dev.com")


def test_devolver_livro():
    """
    Testa a devolução de um livro.
    O livro devolvido deve reaparecer na lista de livros disponíveis.
    """
    b = setup_biblioteca()
    b.emprestar_livro("POO Avançado", "rafa@dev.com")
    b.devolver_livro("POO Avançado", "rafa@dev.com")
    livros_disp = b.listar_livros_disponiveis()
    assert any("POO Avançado" in l for l in livros_disp)


def test_emprestar_livro_inexistente():
    """
    Testa o empréstimo de um livro que não existe no acervo.
    Deve lançar LivroNaoEncontradoError.
    """
    b = setup_biblioteca()
    with pytest.raises(LivroNaoEncontradoError):
        b.emprestar_livro("Livro Fake", "rafa@dev.com")


def test_emprestar_para_usuario_inexistente():
    """
    Testa o empréstimo de um livro para um usuário não registrado.
    Deve lançar UsuarioNaoEncontradoError.
    """
    b = setup_biblioteca()
    with pytest.raises(UsuarioNaoEncontradoError):
        b.emprestar_livro("Python Básico", "naoexiste@dev.com")
