from flask import Flask, render_template, request, redirect, url_for
from biblioteca import Biblioteca
from livro import Livro
from usuario import Usuario

app = Flask(__name__)

# Criando a instância da biblioteca
biblioteca = Biblioteca()

# Página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Cadastrar novos livros
@app.route('/cadastrar_livro', methods=['GET', 'POST'])
def cadastrar_livro():
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        autor = request.form.get('autor')
        livro = Livro(titulo, autor)
        biblioteca.adicionar_livro(livro)
        return redirect(url_for('listar_livros'))
    return render_template('cadastrar_livro.html')

# Listar livros disponíveis
@app.route('/livros')
def listar_livros():
    livros = biblioteca.listar_livros_disponiveis()
    return render_template('livros.html', livros=livros)

# Emprestar um livro
@app.route('/emprestar', methods=['POST'])
def emprestar_livro():
    titulo = request.form.get('titulo')
    nome_usuario = request.form.get('usuario')

    usuario = biblioteca.buscar_usuario(nome_usuario)
    livro = biblioteca.buscar_livro(titulo)

    if usuario and livro and usuario.pegar_emprestado(livro):
        return redirect(url_for('listar_livros'))
    return 'Erro ao emprestar livro', 400

# Devolver um livro
@app.route('/devolver', methods=['GET', 'POST'])
def devolver_livro():
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        nome_usuario = request.form.get('usuario')

        usuario = biblioteca.buscar_usuario(nome_usuario)
        livro = biblioteca.buscar_livro(titulo)

        if usuario and livro and usuario.devolver_livro(livro):
            return redirect(url_for('listar_livros'))
        return 'Erro ao devolver livro', 400
    return render_template('devolver_livro.html')

# Cadastrar novos usuários
@app.route('/cadastrar_usuario', methods=['GET', 'POST'])
def cadastrar_usuario():
    if request.method == 'POST':
        nome = request.form.get('nome')
        usuario = Usuario(nome)
        biblioteca.adicionar_usuario(usuario)
        return redirect(url_for('listar_usuarios'))
    return render_template('cadastrar_usuario.html')

# Listar usuários cadastrados
@app.route('/usuarios')
def listar_usuarios():
    usuarios = biblioteca.usuarios
    return render_template('usuarios.html', usuarios=usuarios)

# Ver livros emprestados
@app.route('/livros_emprestados')
def listar_livros_emprestados():
    livros = [livro for livro in biblioteca.livros if livro.emprestado]
    return render_template('livros_emprestados.html', livros=livros)

if __name__ == '__main__':
    app.run(debug=True)
