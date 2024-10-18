import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Treeview, Scrollbar
from PIL import Image, ImageTk

# Classes base do sistema de biblioteca
class Emprestimo:
    def __init__(self, usuario_id, livro_id, data_emprestimo=None, data_devolucao=None):
        self.usuario_id = usuario_id
        self.livro_id = livro_id
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao
