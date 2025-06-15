import pytest
from services.biblioteca import Biblioteca
from exceptions.erros import (
    LivroNaoDisponivelError,
    LivroNaoEncontradoError,
    UsuarioNaoEncontradoError
)


def setup_biblioteca():
    b = Biblioteca()
    b.adicionar_livro("Python Básico", "Guido", 2020)
    b.adicionar_livro("POO Avançado", "Alan Kay", 2019)
    b.registrar_usuario("Rafaella", "rafa@dev.com")
    return b


def test_emprestar_livro():
    b = setup_biblioteca()
    b.emprestar_livro("Python Básico", "rafa@dev.com")
    livros_disp = b.listar_livros_disponiveis()
    assert "Python Básico" not in " ".join(livros_disp)


def test_emprestar_livro_indisponivel():
    b = setup_biblioteca()
    b.emprestar_livro("Python Básico", "rafa@dev.com")
    with pytest.raises(LivroNaoDisponivelError):
        b.emprestar_livro("Python Básico", "rafa@dev.com")


def test_devolver_livro():
    b = setup_biblioteca()
    b.emprestar_livro("POO Avançado", "rafa@dev.com")
    b.devolver_livro("POO Avançado", "rafa@dev.com")
    livros_disp = b.listar_livros_disponiveis()
    assert any("POO Avançado" in l for l in livros_disp)


def test_emprestar_livro_inexistente():
    b = setup_biblioteca()
    with pytest.raises(LivroNaoEncontradoError):
        b.emprestar_livro("Livro Fake", "rafa@dev.com")


def test_emprestar_para_usuario_inexistente():
    b = setup_biblioteca()
    with pytest.raises(UsuarioNaoEncontradoError):
        b.emprestar_livro("Python Básico", "naoexiste@dev.com")
