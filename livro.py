class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.emprestado = False
        self.usuario_emprestou = None  # Novo atributo para armazenar o usuário que pegou o livro

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            if livro.devolver():  # Marca o livro como disponível
                self.livros_emprestados.remove(livro)
                return True
        return False

    def emprestar(self, usuario):
        if not self.emprestado:
            self.emprestado = True
            self.usuario_emprestou = usuario  # Atribui o usuário que pegou o livro
            return True
        return False

    def devolver(self):
        if self.emprestado:
            self.emprestado = False
            self.usuario_emprestou = None  # Remove o usuário ao devolver
            return True
        return False

    def __str__(self):
        status = 'Disponível' if not self.emprestado else 'Emprestado'
        return f'{self.titulo} por {self.autor} - {status}'
