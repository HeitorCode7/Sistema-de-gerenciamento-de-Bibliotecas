
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Treeview, Scrollbar
from PIL import Image, ImageTk
from Emprestimo import Emprestimo

# Classes base do sistema de biblioteca
class Biblioteca:
    def __init__(self):
        self.usuarios = []
        self.livros = []
        self.emprestimos = []

    def adicionar_usuario(self, usuario):
        if usuario.validar_nome(usuario.primeiro_nome) and usuario.validar_nome(usuario.sobrenome):
            self.usuarios.append(usuario)
            return True
        else:
            return False

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def realizar_emprestimo(self, usuario_id, livro_id):
        emprestimo = Emprestimo(usuario_id, livro_id)
        self.emprestimos.append(emprestimo)

    def devolver_livro(self, emprestimo_id, data_devolucao):
        for emprestimo in self.emprestimos:
            if emprestimo.id == emprestimo_id:
                emprestimo.data_devolucao = data_devolucao
                break
