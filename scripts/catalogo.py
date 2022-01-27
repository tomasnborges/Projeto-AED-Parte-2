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
    if ordem: #Se a ordem escolhida for ascendente

        for i in range(len(visualizacoes)):
            for j in range(i,-1, -1):
                if visualizacoes[i] < visualizacoes[j]:
                    k += 1

            lbox_roteiros.insert(k," " + nomes_roteiros[i])
            k = 0
        
    else: #Se a ordem escolhida for desscendente

        for i in range(len(visualizacoes)):
            for j in range(i,-1, -1):
                if visualizacoes[i] > visualizacoes[j]:
                    k += 1

            lbox_roteiros.insert(k," " + nomes_roteiros[i])
            k = 0
    
    #Para manter o roteiro selecionado a negrito na listbox
    for roteiro in roteiros_filtrados:
        if nome_roteiro  == roteiro:
            indice = lbox_roteiros.get(0, "end").index(" "+ nome_roteiro)
    lbox_roteiros.select_set(indice)

        