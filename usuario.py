class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.livros_emprestados = []

    def pegar_emprestado(self, livro):
        if livro.emprestar(self):  # Passa o usuário ao emprestar
            self.livros_emprestados.append(livro)
            return True
        return False

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            if livro.devolver():
                self.livros_emprestados.remove(livro)
                return True
        return False

    def listar_livros(self):
        return [str(livro) for livro in self.livros_emprestados]
