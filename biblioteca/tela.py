from playsound import playsound
import os
from tkinter.ttk import *
from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox
from Constantes import cores

from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
from datetime import date
from datetime import datetime
from tkscrolledframe import ScrolledFrame
from banco_de_dados import inserir_usuario, get_usuarios, inserir_livro, get_livros, get_livros_emprestados, atualizar_data_devolucao, inserir_emprestimo
from atalhos import configurar_atalhos

# Função para tocar o som ao clicar
def tocar_som_click():
    # Obter o diretório atual do arquivo em execução
    caminho_atual = os.path.dirname(os.path.abspath(__file__))
    
    # Caminho relativo ao arquivo de som dentro da pasta do projeto
    caminho_som = os.path.join(caminho_atual, 'click.mp3')
    
    # Tocar o som
    playsound(caminho_som)

    #Atalhos

# Criando janela ---------------------------------------------

janela = Tk()
janela.title("")
janela.geometry('770x333')
janela.configure(background=cores["co1"])
janela.resizable(width=FALSE, height=FALSE)

style = Style(janela)
style.theme_use("clam")

# Frames -----------------------------------------------------

frameCima = Frame(janela, width=770, height=50, bg=cores["co2"], relief="flat")
frameCima.grid(row=0, column=0, columnspan=2, sticky=NSEW)

frameEsquerda = Frame(janela, width=150, height=265, bg=cores["co4"], relief="solid")
frameEsquerda.grid(row=1, column=0, sticky=NSEW)

frameDireita = Frame(janela, width=600, height=265, bg=cores["co1"], relief="raised")
frameDireita.grid(row=1, column=1, sticky=NSEW)

# Logo -----------------------------------------------------

app_img = Image.open('C:/Users/55319/Downloads/biblioteca/biblioteca/imagens/logo.png')
app_img = app_img.resize((40, 40))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, width=1000, compound=LEFT, padx=5, relief=FLAT, anchor=NW, bg=cores["co2"], fg=cores["co2"])
app_logo.place(x=5, y=0)

app_ = Label(frameCima, text="Sistema de Gerenciamento de biblioteca", compound=LEFT, padx=5, relief=FLAT, anchor=NW, font=('Verdana 15 bold'), bg=cores["co2"], fg=cores["co1"])
app_.place(x=50, y=7)

l_linha = Label(frameCima, width=770, height=1, anchor=NW, font=('Verdana 1'), bg=cores["co2"], fg=cores["co2"])
l_linha.place(x=0, y=47)



# Novo usuario
def novo_usuario():
    global img_salvar

    def validar_nome(nome):
        return nome.isalpha()

    def add():
        primeiro_nome = e_p_nome.get()
        sobrenome = e_sobrenome.get()
        endereco = e_endereco.get()
        email = e_email.get()
        telefone = e_numero.get()

        lista = [primeiro_nome, sobrenome, endereco, email, telefone]


        #Verifica se o nome contém apenas letras
        if not validar_nome(primeiro_nome):
            messagebox.showerror('Erro', 'O Primeiro nome deve conter apenas letras.')
            return
        
        #verifica se o sobrenome contém apenas letras
        if not validar_nome(sobrenome):
            messagebox.showerror('Erro', 'O Sobrenome deve conter apenas letras.')
            return
  
        for i in lista:
          if i == '':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return

        inserir_usuario(primeiro_nome, sobrenome, endereco, email, telefone)
        messagebox.showinfo('Sucesso', 'Usuário inserido com sucesso!')


        e_p_nome.delete(0, END)
        e_sobrenome.delete(0, END)
        e_endereco.delete(0, END)
        e_email.delete(0, END)
        e_numero.delete(0, END)

    app_ = Label(frameDireita, text="Inserir um novo usuário", width=50, compound=LEFT, padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=cores["co1"], fg=cores["co4"])
    app_.grid(row=0, column=0, columnspan=4, sticky=NSEW)
    l_linha = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=cores["co3"], fg=cores["co1"])
    l_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    l_p_nome = Label(frameDireita, text="Primeiro nome*", height=1, anchor=NW, font=(' Ivy 10'), bg=cores["co1"], fg=cores["co4"])
    l_p_nome.grid(row=2, column=0, padx=5, pady=10, sticky=NSEW)
    e_p_nome = Entry(frameDireita, width=25, justify='left', relief="solid")
    e_p_nome.grid(row=2, column=1, pady=10, sticky=NSEW)

    l_sobrenome = Label(frameDireita, text="Sobrenome*", height=1, anchor=NW, font=(' Ivy 10'), bg=cores["co1"], fg=cores["co4"])
    l_sobrenome.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
    e_sobrenome = Entry(frameDireita, width=25, justify='left', relief="solid")
    e_sobrenome.grid(row=3, column=1, pady=5, sticky=NSEW)

    l_endereco = Label(frameDireita, text="Endereço do usuário*", height=1, anchor=NW, font=(' Ivy 10'), bg=cores["co1"], fg=cores["co4"])
    l_endereco.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)
    e_endereco = Entry(frameDireita, width=25, justify='left', relief="solid")
    e_endereco.grid(row=4, column=1, pady=5, sticky=NSEW)

    l_email = Label(frameDireita, text="Endereço de e-mail*", height=1, anchor=NW, font=(' Ivy 10'), bg=cores["co1"], fg=cores["co4"])
    l_email.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)
    e_email = Entry(frameDireita, width=25, justify='left', relief="solid")
    e_email.grid(row=5, column=1, pady=5, sticky=NSEW)

    l_numero = Label(frameDireita, text="Número de telefone*", height=1, anchor=NW, font=(' Ivy 10'), bg=cores["co1"], fg=cores["co4"])
    l_numero.grid(row=6, column=0, padx=5, pady=5, sticky=NSEW)
    e_numero = Entry(frameDireita, width=25, justify='left', relief="solid")
    e_numero.grid(row=6, column=1, pady=5, sticky=NSEW)

    img_salvar = Image.open('C:/Users/55319/Downloads/biblioteca/biblioteca/imagens/save.png')
    img_salvar = img_salvar.resize((18, 18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frameDireita, command=add, image=img_salvar, compound=LEFT, width=100, text='  Salvar', bg=cores["co1"], fg=cores["co4"], font=('Ivy 11'), overrelief=RIDGE)
    b_salvar.grid(row=7, column=1, pady=5, sticky=NSEW)

# Novo livro
def novo_livro():
    global img_salvar

   


    def add():
        title = e_titlo.get()
        author = e_autor.get()
        publisher = e_editora.get()
        year = e_ano.get()
        isbn = e_isbn.get()

        lista = [title, author, publisher, year, isbn]

        for i in lista:
            if i == '':
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return

        inserir_livro(title, author, publisher, year, isbn)
        messagebox.showinfo('Sucesso', 'Livro inserido com sucesso!')

        e_titlo.delete(0, END)
        e_autor.delete(0, END)
        e_editora.delete(0, END)
        e_ano.delete(0, END)
        e_isbn.delete(0, END)

    app_ = Label(frameDireita, text="Inserir um Novo Livro", width=50, compound=LEFT, padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=cores["co1"], fg=cores["co4"])
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    l_linha = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=cores["co3"], fg=cores["co1"])
    l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    l_titlo = Label(frameDireita, text="Título do livro*", height=1, anchor=NW, font=(' Ivy 10'), bg=cores["co1"], fg=cores["co4"])
    l_titlo.grid(row=2, column=0, padx=5, pady=10, sticky=NSEW)
    e_titlo = Entry(frameDireita, width=25, justify='left', relief="solid")
    e_titlo.grid(row=2, column=1, pady=10, sticky=NSEW)

    l_autor = Label(frameDireita, text="Autor do livro*", height=1, anchor=NW, font=(' Ivy 10'), bg=cores["co1"], fg=cores["co4"])
    l_autor.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
    e_autor = Entry(frameDireita, width=25, justify='left', relief="solid")
    e_autor.grid(row=3, column=1, pady=5, sticky=NSEW)

    l_editora = Label(frameDireita, text="Editora do livro*", height=1, anchor=NW, font=(' Ivy 10'), bg=cores["co1"], fg=cores["co4"])
    l_editora.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)
    e_editora = Entry(frameDireita, width=25, justify='left', relief="solid")
    e_editora.grid(row=4, column=1, pady=5, sticky=NSEW)

    l_ano = Label(frameDireita, text="Ano de publicação do livro*", height=1, anchor=NW, font=(' Ivy 10'), bg=cores["co1"], fg=cores["co4"])
    l_ano.grid(row=5, column=0, padx=5, pady=5, sticky=NSEW)
    e_ano = Entry(frameDireita, width=25, justify='left', relief="solid")
    e_ano.grid(row=5, column=1, pady=5, sticky=NSEW)

    l_isbn = Label(frameDireita, text="ISBN do livro*", height=1, anchor=NW, font=(' Ivy 10'), bg=cores["co1"], fg=cores["co4"])
    l_isbn.grid(row=6, column=0, padx=5, pady=5, sticky=NSEW)
    e_isbn = Entry(frameDireita, width=25, justify='left', relief="solid")
    e_isbn.grid(row=6, column=1, pady=5, sticky=NSEW)

    img_salvar = Image.open('C:/Users/55319/Downloads/biblioteca/biblioteca/imagens/save.png')
    img_salvar = img_salvar.resize((18, 18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frameDireita, command=add, image=img_salvar, compound=LEFT, width=100, text='  Salvar', bg=cores["co1"], fg=cores["co4"], font=('Ivy 11'), overrelief=RIDGE)
    b_salvar.grid(row=7, column=1, pady=5, sticky=NSEW)

# Função ver usuários
def ver_usuarios():
    app_ = Label(frameDireita, text="Todos os usuários do banco de dados", width=50, compound=LEFT, padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=cores["co1"], fg=cores["co4"])
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    l_linha = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=cores["co3"], fg=cores["co1"])
    l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    dados = get_usuarios()

    list_header = ['ID', 'Nome', 'Sobrenome', 'Endereço', 'Email', 'Telefone']
    
    global tree

    tree = ttk.Treeview(frameDireita, selectmode="extended", columns=list_header, show="headings")

    vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frameDireita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDireita.grid_rowconfigure(0, weight=12)

    hd = ["nw", "nw", "nw", "nw", "nw", "nw"]
    h = [20, 80, 80, 120, 120, 76, 100]
    n = 0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        tree.column(col, width=h[n], anchor=hd[n])
        n += 1

    for item in dados:
        tree.insert('', 'end', values=item)

# Função ver livros
def ver_livros():
    app_ = Label(frameDireita, text="Todos os livros do banco de dados", width=50, compound=LEFT, padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=cores["co1"], fg=cores["co4"])
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    l_linha = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=cores["co3"], fg=cores["co1"])
    l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    dados = get_livros()

    list_header = ['ID', 'Título', 'Autor', 'Editora', 'Ano', 'ISBN']
    
    global tree

    tree = ttk.Treeview(frameDireita, selectmode="extended", columns=list_header, show="headings")

    vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frameDireita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDireita.grid_rowconfigure(0, weight=12)

    hd = ["nw", "nw", "nw", "nw", "nw", "nw"]
    h = [20, 165, 110, 100, 50, 50, 100]
    n = 0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        tree.column(col, width=h[n], anchor=hd[n])
        n += 1

    for item in dados:
        tree.insert('', 'end', values=item)

# Realizar um empréstimo
def realizar_emprestimo():
    global img_salvar

    def add():
        user_id = e_id_usuario.get()
        book_id = e_id_livro.get()

        lista = [user_id, book_id]

        for i in lista:
            if i == '':
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return

        atualizar_data_devolucao(user_id, book_id)
        messagebox.showinfo('Sucesso', 'Empréstimo realizado com sucesso!')

        e_id_usuario.delete(0, END)
        e_id_livro.delete(0, END)

    app_ = Label(frameDireita, text="Realizar um empréstimo", width=50, compound=LEFT, padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=cores["co1"], fg=cores["co4"])
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    l_linha = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=cores["co3"], fg=cores["co1"])
    l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    l_id = Label(frameDireita, text="Digite o ID do usuário*", height=1, anchor=NW, font=(' Ivy 10'), bg=cores["co1"], fg=cores["co4"])
    l_id.grid(row=2, column=0, padx=5, pady=10, sticky=NSEW)
    e_id_usuario = Entry(frameDireita, width=25, justify='left', relief="solid")
    e_id_usuario.grid(row=2, column=1, pady=10, sticky=NSEW)

    l_id = Label(frameDireita, text="Digite o ID do livro*", height=1, anchor=NW, font=(' Ivy 10'), bg=cores["co1"], fg=cores["co4"])
    l_id.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
    e_id_livro = Entry(frameDireita, width=25, justify='left', relief="solid")
    e_id_livro.grid(row=3, column=1, pady=5, sticky=NSEW)

    img_salvar = Image.open('C:/Users/55319/Downloads/biblioteca/biblioteca/imagens/save.png')
    img_salvar = img_salvar.resize((18, 18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frameDireita, command=add, image=img_salvar, compound=LEFT, width=100, text='  Salvar', bg=cores["co1"], fg=cores["co4"], font=('Ivy 11'), overrelief=RIDGE)
    b_salvar.grid(row=4, column=1, pady=5, sticky=NSEW)

# Livros emprestados no momento
def ver_livros_emprestados():
    app_ = Label(frameDireita, text="Todos os livros emprestados no momento", width=50, compound=LEFT, padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=cores["co1"], fg=cores["co4"])
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    l_linha = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=cores["co3"], fg=cores["co1"])
    l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    dados = []

    books_on_loan = get_livros_emprestados()

    for book in books_on_loan:
        dado = [f"{book[0]}", f"{book[1]}", f"{book[2]} {book[3]}", f"{book[4]}", f"{book[5]}"]
        dados.append(dado)
      
    list_header = ['ID', 'Título', 'Nome do usuário', 'D. empréstimo', 'D. devolução']
    
    global tree

    tree = ttk.Treeview(frameDireita, selectmode="extended", columns=list_header, show="headings")

    vsb = ttk.Scrollbar(frameDireita, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frameDireita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDireita.grid_rowconfigure(0, weight=12)

    hd = ["nw", "nw", "ne", "ne", "ne", "ne"]
    h = [20, 175, 120, 90, 90, 100, 100]
    n = 0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        tree.column(col, width=h[n], anchor=hd[n])
        n += 1

    for item in dados:
        tree.insert('', 'end', values=item)

# Devolução de um empréstimo
def devolucao_emprestimo():
    global img_salvar

    def add():
        loan_id = e_id_emprestimo.get()
        return_date = e_data_retorno.get()

        lista = [loan_id, return_date]

        for i in lista:
            if i == '':
                messagebox.showerror('Erro', 'Preencha todos os campos')
                return
        atualizar_data_devolucao(loan_id, return_date)
        messagebox.showinfo('Sucesso', 'Data de devolução atualizada com sucesso!')

        e_id_emprestimo.delete(0, END)
        e_data_retorno.delete(0, END)

    app_ = Label(frameDireita, text="Atualizar a data de devolução de um empréstimo", width=50, compound=LEFT, padx=5, pady=10, relief=FLAT, anchor=NW, font=('Verdana 12'), bg=cores["co1"], fg=cores["co4"])
    app_.grid(row=0, column=0, columnspan=3, sticky=NSEW)
    l_linha = Label(frameDireita, width=400, height=1, anchor=NW, font=('Verdana 1'), bg=cores["co3"], fg=cores["co1"])
    l_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)

    l_id_emprestimo = Label(frameDireita, text="ID do empréstimo*", height=1, anchor=NW, font=(' Ivy 10'), bg=cores["co1"], fg=cores["co4"])
    l_id_emprestimo.grid(row=2, column=0, padx=5, pady=10, sticky=NSEW)
    e_id_emprestimo = Entry(frameDireita, width=15, justify='left', relief="solid")
    e_id_emprestimo.grid(row=2, column=1, pady=10, sticky=NSEW)

    l_data_retorno = Label(frameDireita, text="Nova data de devolução (formato: DD-MM-AAAA)*", height=1, anchor=NW, font=(' Ivy 10'), bg=cores["co1"], fg=cores["co4"])
    l_data_retorno.grid(row=3, column=0, padx=5, pady=5, sticky=NSEW)
    e_data_retorno = Entry(frameDireita, width=15, justify='left', relief="solid")
    e_data_retorno.grid(row=3, column=1, pady=5, sticky=NSEW)

    img_salvar = Image.open('C:/Users/55319/Downloads/biblioteca/biblioteca/imagens/save.png')
    img_salvar = img_salvar.resize((18, 18))
    img_salvar = ImageTk.PhotoImage(img_salvar)
    b_salvar = Button(frameDireita, command=add, image=img_salvar, compound=LEFT, width=100, text='  Salvar', bg=cores["co1"], fg=cores["co4"], font=('Ivy 11'), overrelief=RIDGE)
    b_salvar.grid(row=4, column=1, pady=5, sticky=NSEW)

# Frame Esquerda --------------------------------------------------

def control(i):
    if i == 'novo_usuario':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        novo_usuario()

    if i == 'novo_livro':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        novo_livro()

    if i == 'ver_livros':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        ver_livros()

    if i == 'ver_usuarios':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        ver_usuarios()

    if i == 'realizar_emprestimo':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        realizar_emprestimo()

    if i == 'ver_livros_emprestados':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        ver_livros_emprestados()

    if i == 'devolucao_emprestimo':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        devolucao_emprestimo()

  

def tocar_som_click():
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load('C:/Users/55319/Downloads/biblioteca/biblioteca/click.mp3')
    pygame.mixer.music.play()


def control(i):
    # Reproduz o som de clique
    tocar_som_click()
    
    # Novo usuário
    if i == 'novo_usuario':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        novo_usuario()

    # Novo livro
    if i == 'novo_livro':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        novo_livro()

    # Ver livros
    if i == 'ver_livros':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        ver_livros()

    # Ver usuários
    if i == 'ver_usuarios':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        ver_usuarios()

    # Realizar um empréstimo
    if i == 'realizar_emprestimo':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        realizar_emprestimo()

    # Livros emprestados no momento
    if i == 'ver_livros_emprestados':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        ver_livros_emprestados()

    # Devolução de um empréstimo
    if i == 'devolucao_emprestimo':
        for widget in frameDireita.winfo_children():
            widget.destroy()
        devolucao_emprestimo()


# Menu ------------------------------------------------------------
img_usuario = Image.open('C:/Users/55319/Downloads/biblioteca/biblioteca/imagens/add.png')
img_usuario = img_usuario.resize((18, 18))
img_usuario = ImageTk.PhotoImage(img_usuario)
b_usuario = Button(frameEsquerda, command=lambda: control('novo_usuario'), image=img_usuario, compound=LEFT, anchor=NW, text='  Novo usuário', bg=cores["co4"], fg=cores["co1"], font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_usuario.grid(row=0, column=0, sticky=NSEW, padx=5, pady=6)

img_novo_livro = Image.open('C:/Users/55319/Downloads/biblioteca/biblioteca/imagens/add.png')
img_novo_livro = img_novo_livro.resize((18, 18))
img_novo_livro = ImageTk.PhotoImage(img_novo_livro)
b_novo_livro = Button(frameEsquerda, command=lambda: control('novo_livro'), image=img_novo_livro, compound=LEFT, anchor=NW, text='  Novo livro', bg=cores["co4"], fg=cores["co1"], font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_novo_livro.grid(row=1, column=0, sticky=NSEW, padx=5, pady=6)

img_ver_livros = Image.open('C:/Users/55319/Downloads/biblioteca/biblioteca/imagens/logo.png')
img_ver_livros = img_ver_livros.resize((18, 18))
img_ver_livros = ImageTk.PhotoImage(img_ver_livros)
b_ver_livros = Button(frameEsquerda, command=lambda: control('ver_livros'), image=img_ver_livros, compound=LEFT, anchor=NW, text=' Exibir todos os livros', bg=cores["co4"], fg=cores["co1"], font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_ver_livros.grid(row=2, column=0, sticky=NSEW, padx=5, pady=6)

img_ver_usuario = Image.open('C:/Users/55319/Downloads/biblioteca/biblioteca/imagens/user.png')
img_ver_usuario = img_ver_usuario.resize((18, 18))
img_ver_usuario = ImageTk.PhotoImage(img_ver_usuario)
b_ver_usuario = Button(frameEsquerda, command=lambda: control('ver_usuarios'), image=img_ver_usuario, compound=LEFT, anchor=NW, text='  Exibir todos os usuarios', bg=cores["co4"], fg=cores["co1"], font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_ver_usuario.grid(row=3, column=0, sticky=NSEW, padx=5, pady=6)

img_emprestimo = Image.open('C:/Users/55319/Downloads/biblioteca/biblioteca/imagens/add.png')
img_emprestimo = img_emprestimo.resize((18, 18))
img_emprestimo = ImageTk.PhotoImage(img_emprestimo)
b_emprestimo = Button(frameEsquerda, command=lambda: control('realizar_emprestimo'), image=img_emprestimo, compound=LEFT, anchor=NW, text=' Realizar um empréstimo', bg=cores["co4"], fg=cores["co1"], font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_emprestimo.grid(row=4, column=0, sticky=NSEW, padx=5, pady=6)

img_devolucao = Image.open('C:/Users/55319/Downloads/biblioteca/biblioteca/imagens/update.png')
img_devolucao = img_devolucao.resize((18, 18))
img_devolucao = ImageTk.PhotoImage(img_devolucao)
b_devolucao = Button(frameEsquerda, command=lambda: control('devolucao_emprestimo'), image=img_devolucao, compound=LEFT, anchor=NW, text='  Devolução de um empréstimo', bg=cores["co4"], fg=cores["co1"], font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_devolucao.grid(row=5, column=0, sticky=NSEW, padx=5, pady=6)

img_livros_emprestados = Image.open('C:/Users/55319/Downloads/biblioteca/biblioteca/imagens/livro2.png')
img_livros_emprestados = img_livros_emprestados.resize((18, 18))
img_livros_emprestados = ImageTk.PhotoImage(img_livros_emprestados)
b_livros_emprestados = Button(frameEsquerda, command=lambda: control('ver_livros_emprestados'), image=img_livros_emprestados, compound=LEFT, anchor=NW, text=' Livros emprestados no momento', bg=cores["co4"], fg=cores["co1"], font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_livros_emprestados.grid(row=6, column=0, sticky=NSEW, padx=5, pady=6)


configurar_atalhos(janela, control)
janela.mainloop()
