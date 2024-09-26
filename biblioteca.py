class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros_disponiveis(self):
        return [livro for livro in self.livros if not livro.emprestado]

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def buscar_usuario(self, nome):
        for usuario in self.usuarios:
            if usuario.nome == nome:
                return usuario
        return None

    def buscar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                return livro
        return None

    # Método a sem implementado

    def listar_livros_emprestados(self):
        """Método para listar livros que estão emprestados."""
        return [livro for livro in self.livros if livro.emprestado]
