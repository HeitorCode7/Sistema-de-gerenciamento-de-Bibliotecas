import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Treeview, Scrollbar
from PIL import Image, ImageTk

# Classes base do sistema de biblioteca

class Livro:
    def __init__(self, titulo, autor, editora, ano, isbn):
        self.titulo = titulo
        self.autor = autor
        self.editora = editora
        self.ano = ano
        self.isbn = isbn
