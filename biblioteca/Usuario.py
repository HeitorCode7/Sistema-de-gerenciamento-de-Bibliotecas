
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Treeview, Scrollbar
from PIL import Image, ImageTk

# Classes base do sistema de biblioteca

class Usuario:
    def __init__(self, primeiro_nome, sobrenome, endereco, email, telefone):
        self.primeiro_nome = primeiro_nome
        self.sobrenome = sobrenome
        self.endereco = endereco
        self.email = email
        self.telefone = telefone

    def validar_nome(self, nome):
        return nome.isalpha()
