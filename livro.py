class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.emprestado = False  # Status do livro

    def emprestar(self):
        if not self.emprestado:
            self.emprestado = True
            return True
        return False

    def devolver(self):
        if self.emprestado:
            self.emprestado = False
            return True
        return False

    def __str__(self):
        status = 'Disponível' if not self.emprestado else 'Emprestado'
        return f'{self.titulo} por {self.autor} - {status}'
