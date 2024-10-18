import tkinter as tk

def configurar_atalhos(janela, control_function):
    # F1 para adicionar novo usuário
    janela.bind('<F1>', lambda event: control_function('novo_usuario'))

    # F2 para adicionar novo livro
    janela.bind('<F2>', lambda event: control_function('novo_livro'))

    # F3 para exibir todos os livros
    janela.bind('<F3>', lambda event: control_function('ver_livros'))

    # F4 para exibir todos os usuários
    janela.bind('<F4>', lambda event: control_function('ver_usuarios'))

    # F5 para realizar um empréstimo
    janela.bind('<F5>', lambda event: control_function('realizar_emprestimo'))

    # F6 para exibir todos os livros emprestados no momento
    janela.bind('<F6>', lambda event: control_function('ver_livros_emprestados'))

    # F7 para devolução de um empréstimo
    janela.bind('<F7>', lambda event: control_function('devolucao_emprestimo'))

    # F8 para gerar o relatório em PDF
    janela.bind('<F8>', lambda event: control_function('gerar_relatorio_pdf'))

