### Sistema de Biblioteca

Este projeto simula uma biblioteca com funcionalidades de cadastro de livros, usuários e empréstimos.

### Funcionalidades

- Cadastro de livros
- Registro de usuários
- Empréstimo e devolução de livros
- Listagem de livros disponíveis
- Listagem de usuários e seus empréstimos
- Tratamento de erros

### Como executar o projeto

##### > Crie o ambiente virtual (opcional):
```bash
python -m venv venv
```

##### > Ative o ambiente virutal:
```bash
WINDOWSN:
venv\Scripts\activate

LINUX:
source venv/bin/activate
```

##### > Instale as dependencias:
```bash
pip install -r requirements.txt
```

##### > Execute o projeto com:
```bash
python main.py
```
##### > Execute os testes com:

```bash
pytest
```
ou:

```bash
python -m pytest
```

#### Como gerar diagrama UML

Pré-requisitos

Python (com pylint instalado)
Graphviz (para renderizar as imagens geradas)

Como instalar o Graphviz

No Windows:
Baixe e instale a versão apropriada em https://graphviz.org/download/

No Linux:

```bash
sudo apt-get install graphviz
```

No MacOS (via Homebrew):

```bash
brew install graphviz
```

Gerar o diagrama com pyreverse

1.Instale o pylint:

```bash
pip install pylint
```

2️. Gere o diagrama

```bash
pyreverse png -p BibliotecaProjeto -ASmy
```