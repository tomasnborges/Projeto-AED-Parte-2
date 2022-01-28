from tkinter import *

def adicionarCategoria(criar_categoria):
    nova_categoria = criar_categoria.get()

    categorias_txt = open("ficheiros/categorias.txt", "a", encoding="utf-8")
    categorias_txt.write(nova_categoria + "\n")
    categorias_txt.close()
