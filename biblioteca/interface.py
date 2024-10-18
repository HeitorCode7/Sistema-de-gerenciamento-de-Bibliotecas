import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Treeview, Scrollbar
from PIL import Image, ImageTk
from Usuario import Usuario
from Biblioteca import Biblioteca
from Usuario import Usuario

class Interface:
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca
        self.janela = tk.Tk()
        self.janela.title("Sistema de Biblioteca")
        self.janela.geometry('770x375')
        self.janela.configure(background='white')
        self.janela.resizable(False, False)
        
        # Chamar o método de configuração da interface
        self.setup_ui()

    def setup_ui(self):
        # Configuração do frame direito
        self.frame_direita = tk.Frame(self.janela, width=600, height=265, bg='white', relief="raised")
        self.frame_direita.grid(row=1, column=1, sticky=tk.NSEW)

        # Botão para adicionar novo usuário
        self.img_usuario = self.load_image('C:/Users/55319/Downloads/biblioteca/biblioteca/imagens/add.png', (18, 18))
        self.b_usuario = tk.Button(self.frame_direita, command=self.novo_usuario, image=self.img_usuario, compound=tk.LEFT, anchor=tk.NW,
                                   text='  Novo usuário', bg='white', fg='black', font=('Ivy 11'), overrelief=tk.RIDGE, relief=tk.GROOVE)
        self.b_usuario.grid(row=0, column=0, sticky=tk.NSEW, padx=5, pady=6)

    def load_image(self, path, size):
        try:
            img = Image.open(path)
            img = img.resize(size)
            return ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"Erro ao carregar imagem: {e}")
            return None

    def novo_usuario(self):
        def add_usuario():
            primeiro_nome = e_p_nome.get()
            sobrenome = e_sobrenome.get()
            endereco = e_endereco.get()
            email = e_email.get()
            telefone = e_telefone.get()

            usuario = Usuario(primeiro_nome, sobrenome, endereco, email, telefone)

            if self.biblioteca.adicionar_usuario(usuario):
                messagebox.showinfo('Sucesso', 'Usuário inserido com sucesso!')
            else:
                messagebox.showerror('Erro', 'Nome inválido, insira apenas letras.')

            e_p_nome.delete(0, tk.END)
            e_sobrenome.delete(0, tk.END)
            e_endereco.delete(0, tk.END)
            e_email.delete(0, tk.END)
            e_telefone.delete(0, tk.END)

        # Configuração da interface de novo usuário
        app_ = tk.Label(self.frame_direita, text="Inserir um novo usuário", width=50, compound=tk.LEFT, padx=5, pady=10, relief=tk.FLAT, anchor=tk.NW,
                        font=('Verdana 12'), bg='white', fg='black')
        app_.grid(row=0, column=0, columnspan=4, sticky=tk.NSEW)

        labels_entries = [
            ("Primeiro nome*", 1),
            ("Sobrenome*", 2),
            ("Endereço*", 3),
            ("E-mail*", 4),
            ("Telefone*", 5)
        ]

        for text, row in labels_entries:
            label = tk.Label(self.frame_direita, text=text, height=1, anchor=tk.NW, font=('Ivy 10'), bg='white', fg='black')
            label.grid(row=row, column=0, padx=5, pady=5, sticky=tk.NSEW)
            entry = tk.Entry(self.frame_direita, width=25, justify='left', relief="solid")
            entry.grid(row=row, column=1, pady=5, sticky=tk.NSEW)
            setattr(self, f"e_{text.split()[0].lower()}", entry)  # Dynamically create entry attributes

        img_salvar = self.load_image('C:/Users/55319/Downloads/biblioteca/biblioteca/imagens/save.png', (18, 18))
        b_salvar = tk.Button(self.frame_direita, command=add_usuario, image=img_salvar, compound=tk.LEFT, width=100, text='  Salvar',
                             bg='white', fg='black', font=('Ivy 11'), overrelief=tk.RIDGE)
        b_salvar.grid(row=6, column=1, pady=5, sticky=tk.NSEW)

    def iniciar(self):
        # Iniciar a interface gráfica
        self.janela.update_idletasks()  # Atualizar o layout antes de iniciar o loop
        self.janela.mainloop()

# Instância da Biblioteca e Interface
biblioteca = Biblioteca()
interface = Interface(biblioteca)
interface.iniciar()
