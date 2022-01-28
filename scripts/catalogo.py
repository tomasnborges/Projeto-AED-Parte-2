from tkinter import *

def ordenarDescAscVisualizacoes(lbox_roteiros,ordem, nome_roteiro, roteiros_filtrados):
    nr_roteiros = len(roteiros_filtrados)

    txt_roteiros = open("ficheiros/roteiros.txt", "r", encoding="utf-8")
    roteiros = txt_roteiros.readlines()
    txt_roteiros.close()

    txt_vusualizacoes = open("ficheiros/visualizacoes.txt", "r", encoding="utf-8")
    linhas = txt_vusualizacoes.readlines()
    txt_vusualizacoes.close()

    #lista que armazena todos os números de visualizações
    visualizacoes = []

    #lista que armazena todos os ids dos roteiros
    nomes_roteiros = []

    nr_visualizacoes = 0
    for i in range(nr_roteiros):
        campos = roteiros_filtrados[i].split(";")
        nome_roteiro1 = roteiros_filtrados[i]
        for roteiro in roteiros:
            campos = roteiro.split(";")
            if campos[1] == nome_roteiro1: #Se o nome do roteiro do ficheiro roteiros.txt é igual ao nome do roteiro iterado existente na lista roteiros_filtrados
                id_roteiro = campos[0][:1]
        for linha in linhas:
            campos1 = linha.split(";")
            id_roteiro1 = campos1[0]
            if id_roteiro == id_roteiro1: #se o id do roteiro do ficheiro roteiros.txt é igual ao id do roteiro do ficheiro visualizaçoes.txt
                nr_visualizacoes += 1

        visualizacoes.append(nr_visualizacoes)
        nr_visualizacoes = 0
        nomes_roteiros.append(nome_roteiro1)
    
    lbox_roteiros.delete(0, "end")
    k = 0
    if ordem: #Se a ordem escolhida for descendente

        for i in range(len(visualizacoes)):
            for j in range(i,-1, -1):
                if visualizacoes[i] < visualizacoes[j]:
                    k += 1

            lbox_roteiros.insert(k," " + nomes_roteiros[i])
            k = 0
        
    else: #Se a ordem escolhida for ascendente

        for i in range(len(visualizacoes)):
            for j in range(i,-1, -1):
                if visualizacoes[i] > visualizacoes[j]:
                    k += 1

            lbox_roteiros.insert(k," " + nomes_roteiros[i])
            k = 0
    
    #Para manter o roteiro selecionado a negrito na listbox
    indice = -1 # por defeito, nenhum item listbox está selecionado
    for roteiro in roteiros_filtrados:
        if nome_roteiro  == roteiro:
            indice = lbox_roteiros.get(0, "end").index(" "+ nome_roteiro)
    lbox_roteiros.select_set(indice)



def ordenarDescAscPontuacoes(lbox_roteiros,ordem, nome_roteiro,roteiros_filtrados):
    nr_roteiros = len(roteiros_filtrados)

    txt_roteiros = open("ficheiros/roteiros.txt", "r", encoding="utf-8")
    roteiros = txt_roteiros.readlines()
    txt_roteiros.close()

    txt_pontuacoes = open("ficheiros/pontuacoes.txt", "r", encoding="utf-8")
    linhas = txt_pontuacoes.readlines()
    txt_pontuacoes.close()

    #lista que armazena todos os números de visualizações
    pontuacoes = []

    #lista que armazena todos os ids dos roteiros
    nomes_roteiros = []

    total_pontuacoes = 0
    nr_pontuacoes = 0
    media = 0
    for i in range(nr_roteiros):
        campos = roteiros_filtrados[i].split(";")
        nome_roteiro1 = roteiros_filtrados[i]
        for roteiro in roteiros:
            campos = roteiro.split(";")
            if campos[1] == nome_roteiro1: #Se o nome do roteiro do ficheiro roteiros.txt é igual ao nome do roteiro iterado existente na lista roteiros_filtrados
                id_roteiro = campos[0][:1]
        for linha in linhas:
            campos1 = linha.split(";")
            id_roteiro1 = campos1[0]
            if id_roteiro == id_roteiro1: #se o id do roteiro do ficheiro roteiros.txt é igual ao id do roteiro do ficheiro visualizaçoes.txt
                total_pontuacoes += int(campos1[2])
                nr_pontuacoes += 1

        if nr_pontuacoes != 0:
            
            media = total_pontuacoes/nr_pontuacoes 
        pontuacoes.append(media)
        
        nomes_roteiros.append(nome_roteiro1)

        nr_pontuacoes = 0
        total_pontuacoes = 0
        media = 0
    
    lbox_roteiros.delete(0, "end")
    k = 0
    if ordem: #Se a ordem escolhida for descendente

        for i in range(len(pontuacoes)):
            for j in range(i,-1, -1):
                if pontuacoes[i] < pontuacoes[j]:
                    k += 1

            lbox_roteiros.insert(k," " + nomes_roteiros[i])
            k = 0
        
    else: #Se a ordem escolhida for asscendente

        for i in range(len(pontuacoes)):
            for j in range(i,-1, -1):
                if pontuacoes[i] > pontuacoes[j]:
                    k += 1

            lbox_roteiros.insert(k," " + nomes_roteiros[i])
            k = 0
    
    #Para manter o roteiro selecionado a negrito na listbox
    indice = -1 # por defeito, nenhum item listbox está selecionado
    for roteiro in roteiros_filtrados:
        if nome_roteiro  == roteiro:
            indice = lbox_roteiros.get(0, "end").index(" "+ nome_roteiro)
    lbox_roteiros.select_set(indice)   
    


def mostrarComentarios(nome_roteiro,linhas,comment_section):
    y_atualizado = 0

    for linha in linhas:
        campos = linha.split(";")
        if campos[0] == nome_roteiro:
            nome_utilizador = campos[1]
            comentario = campos[2][:-1]

            y_atualizado += 20

            #Label Nome do utilizador
            lbl_autor = Label(comment_section,text=nome_utilizador, relief="flat",font=("Helvetica 15 bold"), bg="#F3F6FB")
            lbl_autor.place(x=259,y=y_atualizado+78) 

            y_atualizado+= 40
            #Label comentario
            lbl_comentario = Label(comment_section,text=comentario, relief="flat",font=("Helvetica 11 bold"),bg="#F3F6FB", fg="#8A8A8A")
            lbl_comentario.place(x=259,y=y_atualizado+78) 
            y_atualizado+= 16


