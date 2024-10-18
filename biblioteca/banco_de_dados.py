import sqlite3
from fpdf import FPDF

# Função para conectar ao banco de dados
def conectar():
    conn = sqlite3.connect('biblioteca.db')
    return conn

# Função para criar as tabelas se elas não existirem
def criar_tabelas():
    conn = conectar()
    conn.execute('CREATE TABLE IF NOT EXISTS livros (\
                    id INTEGER PRIMARY KEY,\
                    titulo TEXT,\
                    autor TEXT,\
                    editora TEXT,\
                    ano_publicacao INTEGER,\
                    isbn TEXT)')
    
    conn.execute('CREATE TABLE IF NOT EXISTS usuarios (\
                    id INTEGER PRIMARY KEY,\
                    nome TEXT,\
                    sobrenome TEXT,\
                    endereco TEXT,\
                    email TEXT,\
                    telefone TEXT)')
    
    conn.execute('CREATE TABLE IF NOT EXISTS emprestimos (\
                    id INTEGER PRIMARY KEY,\
                    id_livro INTEGER,\
                    id_usuario INTEGER,\
                    data_emprestimo TEXT,\
                    data_devolucao TEXT,\
                    FOREIGN KEY(id_livro) REFERENCES livros(id),\
                    FOREIGN KEY(id_usuario) REFERENCES usuarios(id))')
    conn.close()

def verificar_tabelas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='livros';")
    if cursor.fetchone() is None:
        print("Tabela 'livros' não existe.")
    else:
        print("Tabela 'livros' existe.")
    conn.close()
    
# Função para inserir um novo usuário
def inserir_usuario(nome, sobrenome, endereco, email, telefone):
    conn = conectar()
    conn.execute("INSERT INTO usuarios (nome, sobrenome, endereco, email, telefone) VALUES (?, ?, ?, ?, ?)",
                 (nome, sobrenome, endereco, email, telefone))
    conn.commit()
    conn.close()

# Função para buscar todos os usuários
def get_usuarios():
    conn = conectar()
    c = conn.cursor()
    c.execute("SELECT * FROM usuarios")
    usuarios = c.fetchall()
    conn.close()
    return usuarios

# Função para inserir um novo livro
def inserir_livro(titulo, autor, editora, ano_publicacao, isbn):
    conn = conectar()
    conn.execute("INSERT INTO livros (titulo, autor, editora, ano_publicacao, isbn) VALUES (?, ?, ?, ?, ?)",
                 (titulo, autor, editora, ano_publicacao, isbn))
    conn.commit()
    conn.close()

# Função para buscar todos os livros
def get_livros():
    conn = conectar()
    c = conn.cursor()
    c.execute("SELECT * FROM livros")
    livros = c.fetchall()
    conn.close()
    return livros

# Função para inserir um novo empréstimo
def inserir_emprestimo(id_livro, id_usuario, data_emprestimo, data_devolucao):
    conn = conectar()
    conn.execute("INSERT INTO emprestimos (id_livro, id_usuario, data_emprestimo, data_devolucao) VALUES (?, ?, ?, ?)",
                 (id_livro, id_usuario, data_emprestimo, data_devolucao))
    conn.commit()
    conn.close()

# Função para buscar todos os livros emprestados
def get_livros_emprestados():
    conn = conectar()
    c = conn.cursor()
    c.execute("SELECT emprestimos.id, livros.titulo, usuarios.nome, usuarios.sobrenome, emprestimos.data_emprestimo, emprestimos.data_devolucao \
               FROM emprestimos \
               JOIN livros ON emprestimos.id_livro = livros.id \
               JOIN usuarios ON emprestimos.id_usuario = usuarios.id \
               WHERE emprestimos.data_devolucao IS NULL")
    livros_emprestados = c.fetchall()
    conn.close()
    return livros_emprestados

# Função para atualizar a data de devolução de um empréstimo
def atualizar_data_devolucao(id_emprestimo, data_devolucao):
    conn = conectar()
    conn.execute("UPDATE emprestimos SET data_devolucao = ? WHERE id = ?",
                 (data_devolucao, id_emprestimo))
    conn.commit()
    conn.close()

