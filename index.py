#TODO
"""
Catálogo - Bernardo, Monge, Tomás
Admin - Bernardo, Monge, Tomás
Top de Most rated - Bernardo, Monge
Notificaçoes - Monge
Favoritos - Bernardo
 """

#Feito
""" 
Login e Registo - Tomás
 """

from cmath import log
from faulthandler import disable
from operator import truediv
from os import stat
from tkinter import *
from tkinter import ttk
from tkinter import font
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter.ttk import Combobox
import datetime

#Nossos múdulos
from scripts.widgets import *
from scripts.login import *
from scripts.catalogo import * 

#Antes, a função colocarFormLogin era chamada dentro da função registarConta, que se encontra no módulo login.py.
#Não podemos chamar uma função que esteja declarada no ficheiro index.py, dentro de uma função que esteja declarada no ficheiro login.py
#Senão teríamos que importar o index.py para o ficheiro login.py que, por sua vez, é importado para o index.py. Isso dá erro
#Função que erifica se os dados de registo são válidos. Se sim, então o utilizador será redireionado para a àrea de log-in para poder autenticar.
def verificarDadosRegisto(e,username,conf_password,email,password,entry_conf_password,entry_username,username_line,conf_password_line,btn_tenho_conta):
    ir_para_login = registarConta(e,username,conf_password,email,password,entry_conf_password,entry_username,username_line,conf_password_line,btn_tenho_conta)
    if ir_para_login :
        colocarFormLogIn(entry_conf_password,entry_username,username_line,conf_password_line,btn_tenho_conta)

def verificarDadosLogin(event,email,password):
    global username_autenticado, tipo_utilizador_autenticado
    ir_para_catalogo = verificarConta(event,email,password)
    if ir_para_catalogo:
        username_autenticado = ir_para_catalogo[0]
        tipo_utilizador_autenticado=ir_para_catalogo[1]
        log_in_frame.withdraw()
        janela_principal = Toplevel()
        app_width = 1366
        app_height = 768
        x = (screen_width/2) - (app_width/2)
        y = (screen_height/2) - (app_height/2)
        janela_principal.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(app_width,app_height,x,y))
        janela_principal.configure(bg = "#fff")
        janela_principal.geometry("1366x768")
        janela_principal.focus_force()
        janela_principal.grab_set()
        janela_principal.resizable(0,0)
        janela_principal.protocol('WM_DELETE_WINDOW', lambda:fecharAplicaçao(window))  # root is your root window
        mostrarJanelaPrincipal(janela_principal)

#Função que esconde os widgets do log-in e adiciona widgets de registo de conta
def colocarFormRegisto():
    msg2.place_forget()
    btn_entrar.place_forget()
    btn_registate.place_forget()
    window.focus_set() #Nenhum widget fica focado

    #Mudar o titulo "Gestor de Roteiros" para "Registo"
    msg_title.configure(text= "Registo") 
    msg_title.place(x=742,y=178)

    #Entry Confirmar Password 
    conf_password = StringVar()
    conf_password.set("Confirmar Password")
    entry_conf_password = Entry(window, width=20, textvariable=conf_password, font=("Helvetica 16"), bg="white", border=0, fg="#ABABAB")
    entry_conf_password.place(x=685,y=468,height=35,width=245)

    #Linha da entry de confirmar a password
    conf_password_line = PanedWindow(window,width=245,height=1,bd=-2, bg="#707070")
    conf_password_line.place(x=685, y=503) 

    #Entry Nome de Utilizador 
    username = StringVar()
    username.set("Nome de Utilizador")
    entry_username = Entry(window, width=20, textvariable=username, font=("Helvetica 16"), bg="white", border=0, fg="#ABABAB")
    entry_username.place(x=685,y=258,height=35,width=245)

    #Linha da entry do username
    username_line = PanedWindow(window,width=245,height=1,bd=-2, bg="#707070")
    username_line.place(x=685, y=293) 

    #Email
    email.set("Email")
    entry_email.configure(fg = "#ABABAB")
    entry_email.place(x=685,y=328,height=35,width=245)
    email_line.place(x=685, y=363)

    #Password
    password.set("Password")
    entry_password.configure(fg = "#ABABAB")
    entry_password.configure(show = "")
    entry_password.place(x=685,y=398,height=35,width=245)
    password_line.place(x=685, y=433)

    entry_username.bind('<ButtonPress-1>', lambda event: mudarTextoUsername(event, entry_username,username,entry_conf_password)) #Porquê "lambda event:" ? https://stackoverflow.com/questions/42509045/tkinter-typeerror-missing-1-required-positional-argument
    entry_conf_password.bind('<Tab>',lambda event: mudarTextoUsername(event, entry_username,username, entry_conf_password))
    entry_conf_password.bind('<ButtonPress-1>', lambda event: mudarTextoConfPassword(event, entry_conf_password,conf_password,entry_password))
    entry_password.bind("<Tab>",lambda event: mudarTextoConfPassword(event, entry_conf_password,conf_password,entry_password))  
    entry_email.bind('<Tab>', lambda event:mudarTextoPasword(event,entry_password,password,entry_email))
    minimize_button.bind("<Tab>", lambda event:mudarTextoEmail(event,entry_email,email,btn_entrar,minimize_button)) 
    entry_email.bind('<ButtonPress-1>', lambda event:mudarTextoEmail(event,entry_email,email,btn_entrar,minimize_button))
    entry_password.bind('<ButtonPress-1>', lambda event:mudarTextoPasword(event,entry_password,password,entry_email))

    #Botão "Criar conta"
    btn_criar_conta.configure(command = lambda e=0:verificarDadosRegisto(e,username,conf_password,email,password,entry_conf_password,entry_username,username_line,conf_password_line,btn_tenho_conta))
    btn_criar_conta.place(x=727,y=540)
    btn_criar_conta.bind("<ButtonPress-1>", lambda event:mudarLayoutBotao(event,btn_criar_conta,img_btn_registar_hover,img_btn_entrar_hover)) 
    btn_criar_conta.bind("<ButtonRelease-1>", lambda event:reporLayoutBotao(event,btn_criar_conta,img_btn_registar,img_btn_entrar))

    #Botão"Já tenho conta" 
    btn_tenho_conta = Button(window,text="Já tenho conta",relief=SUNKEN, borderwidth=0,bg="white", activebackground="white",bd=-5, fg="black",font=("Helvetica 11 bold"), command=lambda:colocarFormLogIn(entry_conf_password,entry_username,username_line,conf_password_line,btn_tenho_conta))
    btn_tenho_conta.place(x=750,y=607)

    window.bind("<Return>", lambda e:registarConta(e,username,conf_password,email,password,entry_conf_password,entry_username,username_line,conf_password_line,btn_tenho_conta)) # Evento que é disparado quando clicamos no enter
#Função que devolve o número de notificações que o utilizador tem por ler
def verNumeroNotificacoes():
    txt_nots = open("ficheiros/notificaçoes.txt", "r", encoding="utf-8")
    linhas = txt_nots.readlines()
    txt_nots.close()
    nr_nots_por_ler = 0
    for linha in linhas:
        campos = linha.split(";")
        if campos[0] == username_autenticado:
            if campos[1].count("/n\\") != 0:
                nr_nots_por_ler +=1
    return nr_nots_por_ler


#Função que esconde os widgets do registo e coloca novamente os widgets de log-in
def colocarFormLogIn(entry_conf_password,entry_username,username_line,conf_password_line,btn_tenho_conta):
    btn_criar_conta.place_forget()
    entry_conf_password.place_forget()
    entry_username.place_forget()
    username_line.place_forget()
    conf_password_line.place_forget()
    btn_tenho_conta.place_forget()

    msg2.place(x=691,y=565)
    btn_entrar.place(x=727,y=435)
    entry_email.place(x=685,y=293,height=35,width=245)
    email_line.place(x=685, y=328) 
    entry_password.place(x=685,y=363,height=35,width=245)
    password_line.place(x=685, y=398)
    btn_registate.place(x=840,y=558)

    #Mudar o titulo "Registo" novamente para "Gestor de Roteiros"
    msg_title.configure(text= "Gestor de Roteiros") 
    msg_title.place(x=667,y=178)

    window.bind("<Return>",lambda event:verificarDadosLogin(event,email,password)) 

#Função que abre a janela principal
def mostrarJanelaPrincipal(janela_principal):
    #Canvas que contêm a imagem de background da janela principal
    ctn_canvas = Canvas(janela_principal,width=1366, height=768,relief="flat", bd=-2)
    ctn_canvas.place(x=0,y=0)
    ctn_canvas.create_image(683,384,image=img_bg_home)

    #Menu   
    # atributo tearoff="off" remove as dashed lines de cada menu de uma opção cascade
    barra_menu = Menu(janela_principal)
    #Opção "Home"
    barra_menu.add_command(label="Home", command="noaction")
    #Opção "Catálogo"
    barra_menu.add_command(label="Catálogo", command=lambda:prepararCatalogo(janela_principal,barra_menu,"",""))
    #Opção "Top de Most Rated"
    barra_menu.add_command(label="Top De Most Rated", command=lambda:prepararTopMostRated(janela_principal,barra_menu))
    #Opção "Favoritos"
    barra_menu.add_command(label="Favoritos",command=lambda:prepararFavoritos(janela_principal,barra_menu))
    #Opção "Notificações"
    nr_nots = verNumeroNotificacoes()
    barra_menu.add_command(label="Notificações({0})" .format(nr_nots), command=lambda:prepararNotificacoes(janela_principal,barra_menu))
    if tipo_utilizador_autenticado == "admin":
        #Opção "Admin"
        barra_menu.add_command(label="Admin", command=lambda:prepararAdmin(janela_principal,barra_menu))
    #Opção "Sair da Conta"
    barra_menu.add_command(label="Sair da Conta", command=lambda:fecharJanela(janela_principal,log_in_frame))
    janela_principal.configure(menu=barra_menu)

    #Message "Boa tarde/Bom dia/Boa noite [nome do utilizador]"
    msg_boas_vindas = Message(janela_principal,width=282,text="", bd=-3,bg="#F3F6FB", font=("Helvetica 19 bold"))
    msg_boas_vindas.place(x=353,y=42)
    data = datetime.datetime.now()
    saudarUtilizador(data,username_autenticado,msg_boas_vindas)
    
    #PanedWindow para as tendências/últimas novidades
    pw_tendencias = PanedWindow(janela_principal,width=636,height=291,bd=-2, bg="white")
    pw_tendencias.place(x=365, y=131) 

    #Label "Tendências"
    lbl_tendebcias = Label(pw_tendencias,text='Tendências', relief="flat",font=("Helvetica 16 bold"), bg="white")
    lbl_tendebcias.place(x=10,y=8) 

    #Label "Destinos para a Páscoa!"
    lbl_tendebcias_desc = Label(pw_tendencias,text='Destinos para a Páscoa!', relief="flat",font=("Helvetica 13 bold"), bg="white", fg="#7E7E7E")
    lbl_tendebcias_desc.place(x=10,y=60) 

    #Canvas do ovo de páscoa
    ctn_canvas_ovo = Canvas(pw_tendencias,width=20, height=50,relief="flat", bd=-2, bg="white")
    ctn_canvas_ovo.place(x=205,y=45)
    ctn_canvas_ovo.create_image(10,25,image=ovo_pascoa)


    #Botão da imagem de Melgaço
    btn_procurar= Button(pw_tendencias,image=melgaco,bg="white", activebackground="white",relief=SUNKEN,borderwidth=0,command=lambda:prepararCatalogo(janela_principal,barra_menu,"Guia e roteiro para visitar Melgaço","2")) 
    btn_procurar.place(x=10,y=85)

    #PanedWindow para os outros roteiros
    pw_outros = PanedWindow(janela_principal,width=636,height=264,bd=-2, bg="white")
    pw_outros.place(x=365, y=457) 
    
    #Label "Outros"
    lbl_tendebcias = Label(pw_outros,text='Outros', relief="flat",font=("Helvetica 16 bold"), bg="white")
    lbl_tendebcias.place(x=10,y=8) 

    #Botão da imagem de Onde comer Bem no porto
    btn_procurar= Button(pw_outros,image=onde_comer,bg="white", activebackground="white",relief=SUNKEN,borderwidth=0,command=lambda:prepararCatalogo(janela_principal,barra_menu,"Onde comer bem no Porto","1")) 
    btn_procurar.place(x=10,y=60)

from tkinter import *
from PIL import Image,ImageTk

#Função que escreve Bom dia/boa tarde/boa noite e o nome do utilizador
def saudarUtilizador(data,username_autenticado,msg_boas_vindas):
    if (int(data.strftime("%H")) >= 18 and int(data.strftime("%H")) <= 23) or (int(data.strftime("%H")) >= 0 and int(data.strftime("%H")) < 6) :#Boa noite
         msg_boas_vindas.configure(text="Boa noite {0}" .format(username_autenticado))
    elif int(data.strftime("%H")) >= 12 and int(data.strftime("%H")) < 18 : #Boa tarde
        msg_boas_vindas.configure(text="Boa tarde {0}" .format(username_autenticado))
    else: #Bom dia
        msg_boas_vindas.configure(text="Bom dia {0}" .format(username_autenticado))

# Função que permite o utilizador avaliar os roteiros
def darAvaliacao(pontuacao,username_autenticado,id_roteiro):
    txt_pontuacoes = open("ficheiros/pontuacoes.txt", "r", encoding="utf-8")
    linhas = txt_pontuacoes.readlines()
    txt_pontuacoes.close()
    ja_avaliou = 0

    for linha in linhas:
        campos = linha.split(";")
        if campos[0] == id_roteiro:
            if not ja_avaliou :
                if campos[1] == username_autenticado:
                    ja_avaliou = 1
                    pontuacao_dada = campos[2]


    if ja_avaliou :

        txt_pontuacoes = open("ficheiros/pontuacoes.txt", "w", encoding="utf-8")
        txt_pontuacoes.write("") 
        txt_pontuacoes.close()
        i = 0
        while i < (len(linhas)): # para cada utilizador existente na aplicação que ja marcou pelo menos um roteiro como favorito #
            campos = linhas[i].split(";")
            if campos[0] != id_roteiro or campos[1] != username_autenticado:
                
                txt_favoritos = open("ficheiros/pontuacoes.txt", "a", encoding="utf-8")
                txt_favoritos.write(linhas[i]) 
                txt_favoritos.close()
            i+=1

        if pontuacao_dada[:-1] == pontuacao:
            return

    txt_pontuacoes = open("ficheiros/pontuacoes.txt", "a", encoding="utf-8")
    txt_pontuacoes.write(id_roteiro + ";" + username_autenticado + ";" + pontuacao +  "\n")
    txt_pontuacoes.close()


#Função que permite fazer scroll no catálogo com a tecla do meio do rato, inspirado no site:https://stackoverflow.com/questions/42830690/trouble-with-mousewheel-scrollbars-in-tkinter
def on_mousewheel(event,my_canvas):
    shift = (event.state & 0x1) != 0
    scroll = -1 if event.delta > 0 else 1
    if shift:
        my_canvas.xview_scroll(scroll, "units")
    else:
        my_canvas.yview_scroll(scroll, "units")

#Função que mostra um especifico roteiro
def mostrarRoteiro(txt,nome_roteiro):
    txt.configure(state="normal") 
    posiçao_inicial = 0
    txt_file = open("ficheiros/roteiros.txt", "r", encoding="utf-8")
    linhas = txt_file.readlines()
    txt.delete("1.0", "end")
    txt_file.close()
    for linha in linhas:
        campos = linha.split(";")  #campo[0] = nome da imagem associada na descrição, campo[1] = titulo, campo[2] = descrição e imagem associada (opcional), campo[3] = Introdução
        if nome_roteiro == campos[1]:
            txt.insert('end', campos[1]+'\n\n', "titulo")
            if campos[2][-18:] == '(imagem associada)':
                txt.insert('end', campos[2][:-18] + "\n", "descrição")
                global imagem #Preciso de chamar a variável, correspondente à imagem, globalmente.
                #Se for chamada localmente, a variável é consideada como "lixo" :https://stackoverflow.com/questions/40879329/image-wont-appear-on-my-tkinter-text-widget
                imagem = ImageTk.PhotoImage(file="imagens\\{0}.jpg" .format(campos[0][0])) 
                txt.image_create("end", image=imagem) #inserir a imagem no widget Text: https://www.youtube.com/watch?v=bdKxTH7Y-38
                txt.insert('end', "\n\n")
            else:
                txt.insert('end', campos[2] + "\n", "descrição")
            # întrodução
            verificarNovaLinha(campos[3],txt,posiçao_inicial)
            txt.insert('end', "\n", "descrição")
            fazerLoopCampos(campos,txt) #campo[4] = nome do local a visitar a vermelho
                                        #campo[5] = descrição do local a visitar
                                        #campo[6] = foto do local/fotos do local (obrigatorio) 
                                        #campo[7] = nome de outro local a visitar a vermelho
                                        #campo[8] = ...
            txt.configure(state="disabled") 


#Função que insere uma nova linha na Text widget sempre que detetar "/n" no ficheiro de texto
def verificarNovaLinha(campo,txt,posiçao_inicial):
    if campo.count('/n') != 0:
        campo1 = ""
        posiçao = campo.find('/n') #procurar a posição do próximo "/n" . Escrever "/n" em vez de "\n" para o programa encontrar o index correto da zona que queremos criar uma nova linha
        campo1 = campo[posiçao_inicial:posiçao] 
        #Há frases que podem ter que estar mais destacadas, por isso, se o programa detetar uma frase entre "/d", vai destacar essa frase
        if campo1.count('/d') != 0:
            campo2 = ""
            posiçao = campo.find('/d') #procurar a posição do próximo "/n" . Escrever "/n" em vez de "\n" para o programa encontrar o index correto da zona que queremos criar uma nova linha
            proxima_posiçao = campo.find('/d', posiçao+1) #procurar a posição do próximo "/n" . Escrever "/n" em vez de "\n" para o programa encontrar o index correto da zona que queremos criar uma nova linha
            campo2 = campo[posiçao+2:proxima_posiçao] 
            txt.insert('end', campo2 , "destacado")
            campo1 = campo[proxima_posiçao+2:]
        else:
            txt.insert('end', campo1  + "\n", "descrição")
            campo1 = campo[posiçao+2:]

        return verificarNovaLinha(campo1,txt,posiçao_inicial)

    else:
        txt.insert('end', campo + "\n", "descrição")
        return True
        


def fazerLoopCampos(campos,txt):
    nr_campos = len(campos)-4
    indice = 4
    nr_lugares_a_visitar = 0

    global imagens_roteiros
    imagens_roteiros = []
    
    while nr_campos != 0:
        nr_campos -= 3
        nr_lugares_a_visitar +=1

    for i in range(0,nr_lugares_a_visitar):
        imagens_roteiros.append(ImageTk.PhotoImage(file="imagens\\{0}.jpg" .format(campos[0][0]+ "_" + str(i+1))))
        txt.insert('end', campos[indice]  + "\n\n", "local_a_visitar")
        indice +=1
        txt.insert('end', campos[indice]  + "\n\n", "descrição")
        indice += 1
        imagem = imagens_roteiros[i]        
        txt.image_create("end", image=imagem) 
        txt.insert('end', "\n\n\n")
        indice +=1


def prevenirDefault(e,txt):
    return "break" # == ignore ler documento https://docs.huihoo.com/tkinter/an-introduction-to-tkinter-1997/intro06.htm

def fecharJanela(janela,log_in_frame):
    janela.destroy()
    log_in_frame.update()
    log_in_frame.deiconify()

def fecharAplicaçao(window):
    """ primeiro experimentamos 
    janela_principal.quit() : demora demasiado tempo para fechar totalmente a aplicação
    depois experimentamos
    window.quit() : Demora pouco tempo para fechar mas ainda demora
    window.destroy() é a forma mais rápida de obrigar o programa a fechar totalmente a aplicação"""
    window.destroy()

# Função que mostra a média das avaliações de um roteiro
def mostrarPontuacao(btn_estrela1,btn_estrela2,btn_estrela3,btn_estrela4,btn_estrela5):
    txt_pontuacoes = open("ficheiros/pontuacoes.txt", "r", encoding="utf-8")
    linhas = txt_pontuacoes.readlines()
    txt_pontuacoes.close()

    soma = 0
    total_pontuacoes = 0
    for linha in linhas:
        campos = linha.split(";")
        if campos[0] == id_roteiro:
            total_pontuacoes +=1
            soma += int(campos[2])
            
    if total_pontuacoes != 0:
        media = soma/total_pontuacoes
        if 4.5 < media and media <= 5:
            btn_estrela1.config(image = estrela)
            btn_estrela2.config(image = estrela)
            btn_estrela3.config(image = estrela)
            btn_estrela4.config(image = estrela)
            btn_estrela5.config(image = estrela)
        elif  4 < media and media <= 4.5:
            btn_estrela1.config(image = estrela)
            btn_estrela2.config(image = estrela)
            btn_estrela3.config(image = estrela)
            btn_estrela4.config(image = estrela)
            btn_estrela5.config(image = estrela_meia)
        elif 3.5 < media and media <= 4:
            btn_estrela1.config(image = estrela)
            btn_estrela2.config(image = estrela)
            btn_estrela3.config(image = estrela)
            btn_estrela4.config(image = estrela)
            btn_estrela5.config(image = estrela_vazia)
        elif 3 < media and media <= 3.5:
            btn_estrela1.config(image = estrela)
            btn_estrela2.config(image = estrela)
            btn_estrela3.config(image = estrela)
            btn_estrela4.config(image = estrela_meia)
            btn_estrela5.config(image = estrela_vazia)
        elif 2.5 < media and media <= 3:
            btn_estrela1.config(image = estrela)
            btn_estrela2.config(image = estrela)
            btn_estrela3.config(image = estrela)
            btn_estrela4.config(image = estrela_vazia)
            btn_estrela5.config(image = estrela_vazia)
        elif 2 < media and media <= 2.5:
            btn_estrela1.config(image = estrela)
            btn_estrela2.config(image = estrela)
            btn_estrela3.config(image = estrela_meia)
            btn_estrela4.config(image = estrela_vazia)
            btn_estrela5.config(image = estrela_vazia)
        elif 1.5 < media and media <= 2:
            btn_estrela1.config(image = estrela)
            btn_estrela2.config(image = estrela)
            btn_estrela3.config(image = estrela_vazia)
            btn_estrela4.config(image = estrela_vazia)
            btn_estrela5.config(image = estrela_vazia)
        elif 1 < media and media <= 1.5:
            btn_estrela1.config(image = estrela)
            btn_estrela2.config(image = estrela_meia)
            btn_estrela3.config(image = estrela_vazia)
            btn_estrela4.config(image = estrela_vazia)
            btn_estrela5.config(image = estrela_vazia)
        elif 0.5 < media and media <= 1:
            btn_estrela1.config(image = estrela)
            btn_estrela2.config(image = estrela_vazia)
            btn_estrela3.config(image = estrela_vazia)
            btn_estrela4.config(image = estrela_vazia)
            btn_estrela5.config(image = estrela_vazia)
        elif 0 < media and media <= 0.5:
            btn_estrela1.config(image = estrela_meia)
            btn_estrela2.config(image = estrela_vazia)
            btn_estrela3.config(image = estrela_vazia)
            btn_estrela4.config(image = estrela_vazia)
            btn_estrela5.config(image = estrela_vazia)
        else:
            btn_estrela1.config(image = estrela_vazia)
            btn_estrela2.config(image = estrela_vazia)
            btn_estrela3.config(image = estrela_vazia)
            btn_estrela4.config(image = estrela_vazia)
            btn_estrela5.config(image = estrela_vazia)
    else:
        btn_estrela1.config(image = estrela_vazia)
        btn_estrela2.config(image = estrela_vazia)
        btn_estrela3.config(image = estrela_vazia)
        btn_estrela4.config(image = estrela_vazia)
        btn_estrela5.config(image = estrela_vazia)

#Função que mostra o número de visualizações
def mostrarNumeroVisualizacoes(nr_visualizacoes):
    global username_autenticado, id_roteiro
    # primeiro vamos ver verificar o utilizador já viu o roteiro, senão vamos adicioná-lo à lista de quem já viu o roteiro no ficheiro visualizacoes.txt
    txt_vusualizacoes = open("ficheiros/visualizacoes.txt", "r", encoding="utf-8")
    linhas = txt_vusualizacoes.readlines()
    txt_vusualizacoes.close()

    nr_visualizadores = 0
    ja_viu = 0
    for linha in linhas:
        campos = linha.split(";")
        if campos[0] == id_roteiro:
            nr_visualizadores += 1
            if not ja_viu :
                if campos[1][:-1] == username_autenticado:
                    ja_viu = 1
    if not ja_viu:
        txt_vusualizacoes = open("ficheiros/visualizacoes.txt", "a", encoding="utf-8")
        txt_vusualizacoes.write(id_roteiro + ";" + username_autenticado + "\n")
        nr_visualizadores += 1
        txt_vusualizacoes.close()
    nr_visualizacoes.set("{0} Visualizações" .format(nr_visualizadores))
        


def desmarcarFavorito(coracao_btn,todos_btn,favoritos_btn,lbox_roteiros):
    global username_autenticado,id_roteiro
    txt_favoritos = open("ficheiros/favoritos.txt", "r", encoding="utf-8")
    favoritos = txt_favoritos.readlines()
    txt_favoritos.close()

    string_username = ""
    
    i= 0
    while i < (len(favoritos)): # para cada utilizador existente na aplicação que ja marcou pelo menos um roteiro como favorito #
        campos = favoritos[i].split(";")
        if username_autenticado == campos[0]:
            string_username2 = favoritos[i][1:]
            string_username1 = string_username2.replace(";{0}" .format(id_roteiro), "")
            string_username = string_username1.replace("\n", "")
            string_username = favoritos[i][0] + string_username
            if string_username[-1] == ";":
                string_username = string_username[:-1]
            break   
        i+=1    

    preciso_remover = 0
    j = 0
    while j < (len(favoritos)): # para cada utilizador existente na aplicação que ja marcou pelo menos um roteiro como favorito #
        campos = favoritos[j].split(";")

        if preciso_remover == 1 and j == 0:
            txt_favoritos = open("ficheiros/favoritos.txt", "w", encoding="utf-8")
            txt_favoritos.write("") 
            txt_favoritos.close()

        if campos[0] == username_autenticado and preciso_remover == 0: #se o programa encontra-se na linha que contêm o nome do utilizador autenticado)
            preciso_remover = 1
            j = -1

        elif campos[0] != username_autenticado and preciso_remover == 1:
            txt_favoritos = open("ficheiros/favoritos.txt", "a", encoding="utf-8")
            txt_favoritos.write(favoritos[j]) 
            txt_favoritos.close()
        j+=1    

    if string_username.count(";") != 0:
        txt_favoritos = open("ficheiros/favoritos.txt", "a", encoding="utf-8")
        txt_favoritos.write(string_username + "\n") 
        txt_favoritos.close()    
                
    coracao_btn.config(image = coracao_vazio, command=lambda:marcarFavorito(coracao_btn,todos_btn,favoritos_btn,lbox_roteiros))

    if a_ver_que_lista == "favoritos":
        verFavoritos(todos_btn,favoritos_btn,lbox_roteiros)


def marcarFavorito(coracao_btn,todos_btn,favoritos_btn,lbox_roteiros):
    global username_autenticado, id_roteiro
    txt_favoritos = open("ficheiros/favoritos.txt", "r", encoding="utf-8")
    favoritos = txt_favoritos.readlines()
    txt_favoritos.close()

    string_username = ""
    ja_tem_favoritos = 0

    i= 0
    while i < (len(favoritos)): # para cada utilizador existente na aplicação que ja marcou pelo menos um roteiro como favorito #
        campos = favoritos[i].split(";")
        if ja_tem_favoritos == 1 and i == 0:
            txt_favoritos = open("ficheiros/favoritos.txt", "w", encoding="utf-8")
            txt_favoritos.write("") 
            txt_favoritos.close()

        if campos[0] == username_autenticado and ja_tem_favoritos == 0: #se o programa encontra-se na linha que contêm o nome do utilizador autenticado)
            ja_tem_favoritos = 1
            string_username = favoritos[i].replace("\n", "")
            i = -1
        elif campos[0] != username_autenticado and ja_tem_favoritos == 1:
            txt_favoritos = open("ficheiros/favoritos.txt", "a", encoding="utf-8")
            txt_favoritos.write(favoritos[i]) 
            txt_favoritos.close()
        i+=1

    # txt_favoritos = open("ficheiros/favoritos.txt", "a", encoding="utf-8") não chamar localmente, porque o computador demora mais tempo a marcar o roteiro como favorito
    if ja_tem_favoritos:
        txt_favoritos = open("ficheiros/favoritos.txt", "a", encoding="utf-8")
        txt_favoritos.write(string_username + ";" + id_roteiro + "\n")
        txt_favoritos.close()
    else:
        txt_favoritos = open("ficheiros/favoritos.txt", "a", encoding="utf-8")
        txt_favoritos.write(username_autenticado + ";" + id_roteiro + "\n")
        txt_favoritos.close()

                
    coracao_btn.config(image = coracao,command=lambda:desmarcarFavorito(coracao_btn,todos_btn,favoritos_btn,lbox_roteiros))

    if a_ver_que_lista == "favoritos":
        verFavoritos(todos_btn,favoritos_btn,lbox_roteiros)

def verFavoritos(todos_btn,favoritos_btn,lbox_roteiros):
    global a_ver_que_lista
    a_ver_que_lista = "favoritos"
    todos_btn.config(fg="#7E7E7E")
    favoritos_btn.config(fg="black")
    txt_favoritos = open("ficheiros/favoritos.txt", "r", encoding="utf-8")
    linhas = txt_favoritos.readlines()
    txt_favoritos.close()

    procurarRoteiro(pesquisa,lbox_roteiros)


def verTodos(todos_btn,favoritos_btn,lbox_roteiros):
    global a_ver_que_lista
    a_ver_que_lista = "todos"
    favoritos_btn.config(fg="#7E7E7E")
    todos_btn.config(fg="black")

    procurarRoteiro(pesquisa,lbox_roteiros)
    
def mudarCanvas(e,txt,lbox_roteiros,main_frame,janela_principal,barra_menu,imagem_clicada):
    global roteiro_selecionado, nome_roteiro,id_roteiro
    altura = 0
    if imagem_clicada:
        txt_file = open("ficheiros/roteiros.txt", "r", encoding="utf-8")
        linhas = txt_file.readlines()
        txt.delete("1.0", "end")
        txt_file.close()
        for linha in linhas:
            campos = linha.split(";") 
            if nome_roteiro == campos[1]:
                altura = campos[0][2:]

        imagem_clicada = 0

    else:
        try:
            lbox_roteiros.get(lbox_roteiros.curselection())
        except:
                return
        txt_file = open("ficheiros/roteiros.txt", "r", encoding="utf-8")
        linhas = txt_file.readlines()
        txt.delete("1.0", "end")
        txt_file.close()
        for linha in linhas:
            campos = linha.split(";") 
            if lbox_roteiros.get(lbox_roteiros.curselection()) == " " + campos[1]:
                nome_roteiro = campos[1] 
                id_roteiro = campos[0][0:1]
                altura = campos[0][2:]
    
    main_frame.destroy()

    roteiro_selecionado = True
    
    mostrarCatalogo(janela_principal,barra_menu,altura,imagem_clicada)

def procurarRoteiro(pesquisa,lbox_roteiros):
    global roteiros_filtrados
    roteiro_pesquisado = pesquisa.get().lower()

    txt_roteiros = open("ficheiros/roteiros.txt", "r", encoding="utf-8")
    roteiros = txt_roteiros.readlines()
    txt_roteiros.close()

    txt_favoritos = open("ficheiros/favoritos.txt", "r", encoding="utf-8")
    favoritos = txt_favoritos.readlines()
    txt_favoritos.close()
    
    txt_roteiros_categorias = open("ficheiros/roteiro-categoria.txt", "r", encoding="utf-8")
    roteiros_categorias =  txt_roteiros_categorias.readlines()
    txt_roteiros_categorias.close()

    categorias_selecionadas = []
    i = 0
    for categoria in categoria_selected: # iterar cada categoria existente
        if categoria.get() == 1: #se, por exemplo, 1 (id de Praias)está selecionado
            categorias_selecionadas.append(categorias_nomes[i])
        i+=1
    
    roteiros_filtrados = []
    
    lbox_roteiros.delete(0, "end")

    if a_ver_que_lista == "todos":
        for linha in roteiros: # para cada roteiro existente no ficheiro roteiros.txt
            campos = linha.split(";")
            roteiro = campos[1].lower()
            if roteiro.count(roteiro_pesquisado): #Se a palavra/frase que procuramos está contida na string do nome desse roteiro
                for roteiro in roteiros_categorias: # para cada roteiro existente no ficheiro roteiros-categorias.txt
                    campos1 = roteiro.split(";")
                    if campos1[0] == campos[1]: #Se o nome do roteiro iterado e que se encontra no ficheiro roteiro-categoria.txt é igual ao nome do roteiro iterado e que se encontra no ficheiro roteiros.txt
                        if len(categorias_selecionadas) == 0: #Se não foi selecionado nenhuma categoria
                            lbox_roteiros.insert("end"," "+ campos[1]) #então inserimos todos os roteiros
                            roteiros_filtrados.append(campos[1])
                        else:   # se o utilizador selecionou categoria(s)
                            nr_categorias = len(campos1)
                            valido = 0
                            for j in range(1,nr_categorias):
                                for categoria in categorias_selecionadas:
                                    if campos1[j] == categoria:
                                        valido +=1
                            if valido == len(categorias_selecionadas):
                                lbox_roteiros.insert("end"," "+ campos[1]) # inserir os roteiros que apresentam essa(s) categoria(s)
                                roteiros_filtrados.append(campos[1])
    else:
        for favorito in favoritos: # para cada utilizador existente na aplicação que ja marcou pelo menos um roteiro como favorito #
            campos = favorito.split(";")
            roteiro = campos[1].lower()
            nr_favoritos = len(campos) #quantos roteiros o utilizador tem como favoritos 
            if campos[0] == username_autenticado: #se o programa encontra-se na linha que contêm o nome do utilizador autenticado)
                for x in range(1,nr_favoritos): #iterar o id de cada roteiro marcado como favorito pelo utilizador autenticado 


                   for roteiro in roteiros: # para cada roteiro existente no ficheiro roteiros.txt
                       campos1 = roteiro.split(";")
                       if campos1[0][0:1] == campos[x].replace("\n",""): #se o id do roteiro iterado no ficheiro roteiros.txt é igual ao id do roteiro marcado como favorito 
                           if roteiro.count(roteiro_pesquisado): #Se a palavra/frase que procuramos está contida na string do nome desse roteiro
                               for roteiro1 in roteiros_categorias: # para cada roteiro existente no ficheiro roteiros-categorias.txt
                                   campos2 = roteiro1.split(";")
                                   if campos2[0] == campos1[1]: #Se o nome do roteiro iterado e que se encontra no ficheiro roteiro-categoria.txt é igual ao nome do roteiro iterado e que se encontra no ficheiro roteiros.txt
                                       if len(categorias_selecionadas) == 0: #Se não foi selecionado nenhuma categoria
                                           lbox_roteiros.insert("end"," "+ campos1[1]) #então inserimos todos os roteiros
                                           roteiros_filtrados.append(campos1[1])
                                       else:   # se o utilizador selecionou categoria(s)
                                           nr_categorias = len(campos2)
                                           valido = 0
                                           for j in range(1,nr_categorias):
                                               for categoria in categorias_selecionadas:
                                                   if campos2[j] == categoria:
                                                       valido +=1
                                           if valido == len(categorias_selecionadas):
                                               lbox_roteiros.insert("end"," "+ campos1[1]) # inserir os roteiros que apresentam essa(s) categoria(s)
                                               roteiros_filtrados.append(campos1[1])

    # para manter o roteiro selecionado a escuro    
    global nome_roteiro                       
    i = 0
    indice1 = -1
    for roteiro in roteiros_filtrados:
        if nome_roteiro  == roteiro:
            indice1 = i
        i+=1
    lbox_roteiros.select_set(indice1)
        

#Destruir os widgets da janela principal e mostrar o catalogo
def prepararCatalogo(janela_principal,barra_menu,nome_roteiro_escolhido1,id_roteiro_escolhido1):
    imagem_clicada = 0
    if nome_roteiro_escolhido1 != "":
        imagem_clicada = 1
        global nome_roteiro,id_roteiro
        nome_roteiro = nome_roteiro_escolhido1
        id_roteiro = id_roteiro_escolhido1

    fundo_branco = PanedWindow(janela_principal ,width=1366,height=768,bg="white") 
    fundo_branco.place(x=0,y=0)
    altura = 768
    mostrarCatalogo(janela_principal,barra_menu,altura,imagem_clicada)
    
def prepararFavoritos(janela_principal,barra_menu):
    mostrarFavoritos(janela_principal,barra_menu)

def prepararTopMostRated(janela_principal,barra_menu):
    mostrarTop(janela_principal,barra_menu)

def prepararNotificacoes(janela_principal,barra_menu):
    mostrarNotificacoes(janela_principal,barra_menu)

def prepararAdmin(janela_principal,barra_menu):
    mostrarAdmin(janela_principal,barra_menu)

#Destruir os widgets do catalogo e mostrar a janela principal
def prepararJanelaPrincipal(janela_principal,*widgets):

    # dar reset aos filtros 
    pesquisa.set("")
    global  categoria_selected
    categoria_selected = []

    for widget in widgets:
        widget.destroy()
    mostrarJanelaPrincipal(janela_principal)

roteiro_selecionado = False 

a_ver_que_lista = "todos"

categoria_selected = [] #lista que armazena valores booleanos que mostram se uma categoria está ou não selecionada
categorias_nomes = []  #lista que guarda os nomes das categorias

def mostrarNotificacoes(janela_principal,barra_menu):
    notificacoes_janela = Toplevel()
    app_width = 800
    app_height = 500
    x = (screen_width/2) - (app_width/2)
    y = (screen_height/2) - (app_height/2)
    notificacoes_janela.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(app_width,app_height,x,y))
    notificacoes_janela.configure(bg = "#fff")
    notificacoes_janela.focus_force()
    notificacoes_janela.grab_set()

    #Label "Notificações"
    lbl_notificacoes = Label(notificacoes_janela,text='Notificações', relief="flat",font=("Helvetica 17"), bg="white")
    lbl_notificacoes.place(x=44,y=20) 

    #Listbox da esquerda
    lbox_roteiros1 = Listbox(notificacoes_janela,relief="flat",bd=-2, bg="#F3F6FB",fg="#7E7E7E",font=('Helvetica', 11,"bold"), activestyle="none",highlightthickness=0,selectbackground='#F3F6FB',selectforeground='black')
    lbox_roteiros1.place(x=44,y=119,height=262,width=243)

    #Botão "Consultar"
    btn_consultar= Button(notificacoes_janela,image=consultar_img,bg="white", activebackground="white",relief=SUNKEN,borderwidth=0, font=("Helvetica 16 bold"),command="noaction")  
    btn_consultar.place(x=88,y=407)

    #Text notificação
    txt_notificacao = Text(notificacoes_janela, wrap='word', bg="black", fg="white",cursor="arrow",selectbackground="#09d8be",bd=-2) #Para mudar o cursor, documento https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/cursors.html
    txt_notificacao.place(x=341,y=100,width=354, height=301)


def mostrarAdmin(janela_principal,barra_menu):
    admin_janela = Toplevel()
    app_width = 1024
    app_height = 500
    x = (screen_width/2) - (app_width/2)
    y = (screen_height/2) - (app_height/2)
    admin_janela.configure(bg = "#fff")
    admin_janela.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(app_width,app_height,x,y))
    
    admin_janela.focus_force()
    admin_janela.grab_set()

    #Label "Nova categoria"
    lbl_opcoes = Label(admin_janela,text='Nova categoria', relief="flat",font=("Helvetica 12"), bg="white", fg="black")
    lbl_opcoes.place(x=44,y=20) 

    #Entry adicionar nova categoria
    entry_pesquisa = Entry(admin_janela, textvariable=pesquisa, relief="flat", bg="#F3F6FB", font=("Helvetica 13"))
    entry_pesquisa.place(x=173,y=20,height=30,width=205)

    #Entry para o título
    entry_titulo = Entry(admin_janela, textvariable=pesquisa, relief="flat", bg="#F3F6FB", font=("Helvetica 13"))
    entry_titulo.place(x=607,y=55,height=30,width=205)

    #Botão "Adicionar categoria"
    btn_add= Button(admin_janela,text= "Adicionar categoria",bg="white", activebackground="white", font=("Helvetica 16 bold"),command="noaction")  
    btn_add.place(x=44,y=100)

    #Botão "Remover roteiro"
    btn_add= Button(admin_janela,text= "Remover roteiro",bg="white", activebackground="white", font=("Helvetica 16 bold"),command="noaction")  
    btn_add.place(x=300,y=222)

    #Botão "Editar roteiro"
    btn_add= Button(admin_janela,text= "Editar roteiro",bg="white", activebackground="white", font=("Helvetica 16 bold"),command="noaction")  
    btn_add.place(x=300,y=273)

    #Botão "Associar imagem"
    btn_add= Button(admin_janela,text= "Associar imagem",bg="white", activebackground="white", font=("Helvetica 16 bold"),command="noaction")  
    btn_add.place(x=650,y=193)

    #Botão "Adicionar roteiro"
    btn_add= Button(admin_janela,text= "Adicionar roteiro",bg="white", activebackground="white", font=("Helvetica 16 bold"),command="noaction")  
    btn_add.place(x=650,y=457)

    #Label "Roteiros"
    lbl_opcoes = Label(admin_janela,text='Nova categoria', relief="flat",font=("Helvetica 12"), bg="white", fg="blue")
    lbl_opcoes.place(x=44,y=180) 

    #Label "Título"
    lbl_opcoes = Label(admin_janela,text="Título", relief="flat",font=("Helvetica 12"), bg="white", fg="blue")
    lbl_opcoes.place(x=549,y=57) 

    #Text descriçao
    txt_notificacao = Text(admin_janela, wrap='word', bg="#F3F6FB",cursor="arrow",selectbackground="#09d8be",bd=-2) #Para mudar o cursor, documento https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/cursors.html
    txt_notificacao.place(x=609,y=96,width=257, height=89)

    #Text texto
    txt_notificacao = Text(admin_janela, wrap='word', bg="#F3F6FB",cursor="arrow",selectbackground="#09d8be",bd=-2) #Para mudar o cursor, documento https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/cursors.html
    txt_notificacao.place(x=609,y=238,width=257, height=182)


    #Label "Descrição"
    lbl_opcoes = Label(admin_janela,text="Descrição", relief="flat",font=("Helvetica 12"), bg="white", fg="blue")
    lbl_opcoes.place(x=512,y=96) 

    #Listbox da esquerda
    lbox_roteiros1 = Listbox(admin_janela,relief="flat",bd=-2, bg="#F3F6FB",fg="#7E7E7E",font=('Helvetica', 11,"bold"), activestyle="none",highlightthickness=0,selectbackground='#F3F6FB',selectforeground='black')
    lbox_roteiros1.place(x=44,y=201,height=262,width=243)

    #Label "Desenvolvimento"
    lbl_opcoes = Label(admin_janela,text="Desenvolvimento", relief="flat",font=("Helvetica 12"), bg="white", fg="blue")
    lbl_opcoes.place(x=500,y=208) 




def mostrarTop(janela_principal,barra_menu):
    top_janela = Toplevel()
    app_width = 800
    app_height = 500
    x = (screen_width/2) - (app_width/2)
    y = (screen_height/2) - (app_height/2)
    top_janela.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(app_width,app_height,x,y))
    top_janela.configure(bg = "#fff")
    top_janela.focus_force()
    top_janela.grab_set()

    #Label "Roteiors mais vistos"
    lbl_roteirosvistos = Label(top_janela,text='Roteiros mais vistos', relief="flat",font=("Helvetica 17"), bg="white")
    lbl_roteirosvistos.place(x=44,y=20) 

    #Label "Escolha uma das opções"
    lbl_opcoes = Label(top_janela,text='Escolha uma das opções', relief="flat",font=("Helvetica 12"), bg="white", fg="blue")
    lbl_opcoes.place(x=44,y=100) 

    #Radiobuttons
    val_categoria = StringVar()
    val_categoria.set('Todas') #já devemos ter um valor da radiobutton selecionada

    txt_categorias = open("ficheiros\\categorias.txt", "r", encoding="utf-8")
    linhas = txt_categorias.readlines()
    txt_categorias.close()

    categorias_nomes1 = [] # lista que vai inicializar os radiobuttons
    categorias = []
    i = 0
    categorias.append( Radiobutton(top_janela, text="Todas", value="Todas", variable=val_categoria, bg="white",command='noaction', activebackground="white"))
    categorias[0].place(x = 25, y = 150 + i*25)
    for categoria in linhas:
        categorias_nomes1.append(categoria[0:-1]) # -1 == len(lista)-1, ignoramos o último index porque é um espaço 
        categorias.append( Radiobutton(top_janela, text=categorias_nomes1[i], value=categorias_nomes1[i], variable=val_categoria, bg="white",command='noaction', activebackground="white"))
        categorias[i].bind("<Button-1>", lambda e: mostrarTopCategoria(e, categorias_nomes[i],val_categoria))
        categorias[i].place(x = 44, y = 150 + i*25)
        i+=1

    #treeview
    table = ttk.Treeview(top_janela,columns = ("Lugar", "Roteiro"), show = "headings")
    table.column("Lugar", width=100,anchor="c")
    table.column("Roteiro", width=250,anchor="c")
    table.heading("Lugar", text="Lugar")
    table.heading("Roteiro", text="Roteiro")
    table.place(x=350,y=100, height=300)


def mostrarTopCategoria(e, categoria,val_categoria):
    categoria_escolhida = val_categoria.get()
    txt_roteiro_categoria = open("ficheiros/roteiro-categoria.txt", "r", encoding="utf-8")
    linhas = txt_roteiro_categoria.readlines()
    txt_roteiro_categoria.close()

    txt_vusualizacoes = open("ficheiros/visualizacoes.txt", "r", encoding="utf-8")
    linhas1 = txt_vusualizacoes.readlines()
    txt_vusualizacoes.close()

    txt_roteiros = open("ficheiros/roteiros.txt", "r", encoding="utf-8")
    linhas2 = txt_roteiros.readlines()
    txt_roteiros.close()


    
    nr_visualizaçoes = 0
    if categoria_escolhida != "Todas":
        for linha in linhas:
            campos = linha.split(";")
            nr_categorias = len(campos)
            for x in range(1,nr_categorias):
                if campos[x] == categoria_escolhida: # coincidir a categoria
                    for linha2 in linhas2:
                        campos2 = linha2.split(";")
                        if campos2[1] == campos[0]:  # coincidir o nome
                            for linha1 in linhas1:
                                campos1 = linha1.split(";")
                                if campos1[0] == campos2[0][:1]: # coincidir o id
                                    nr_visualizaçoes += 1



def mostrarFavoritos(janela_principal,barra_menu):
    favoritos_janela = Toplevel()
    app_width = 800
    app_height = 500
    x = (screen_width/2) - (app_width/2)
    y = (screen_height/2) - (app_height/2)
    favoritos_janela.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(app_width,app_height,x,y))
    favoritos_janela.configure(bg = "#fff")
    favoritos_janela.focus_force()
    favoritos_janela.grab_set()

    #Label "Favoritos"
    lbl_roteirosvistos = Label(favoritos_janela,text='Favoritos', relief="flat",font=("Helvetica 17"), bg="white")
    lbl_roteirosvistos.place(x=25,y=20) 

    #Listbox da esquerda
    lbox_roteiros1 = Listbox(favoritos_janela,relief="flat",bd=-2, bg="#F3F6FB",fg="#7E7E7E",font=('Helvetica', 11,"bold"), activestyle="none",highlightthickness=0,selectbackground='#F3F6FB',selectforeground='black')
    lbox_roteiros1.place(x=44,y=119,height=262,width=243)

    #Listbox da direita
    lbox_roteiros2 = Listbox(favoritos_janela,relief="flat",bd=-2, bg="#F3F6FB",fg="#7E7E7E",font=('Helvetica', 11,"bold"), activestyle="none",highlightthickness=0,selectbackground='#F3F6FB',selectforeground='black') 
    lbox_roteiros2.place(x=512,y=+119,height=262,width=243)
    
    #Botão "Feito"
    btn_entrar= Button(favoritos_janela,image=feito_img,bg="white", activebackground="white",relief=SUNKEN,borderwidth=0, font=("Helvetica 16 bold"),command="noaction") 
    btn_entrar.place(x=322,y=230)

    #Botão "Remover"
    btn_entrar= Button(favoritos_janela,image=remover_img,bg="white", activebackground="white",relief=SUNKEN,borderwidth=0, font=("Helvetica 16 bold"),command="noaction")  
    btn_entrar.place(x=88,y=407)

    #Label "Roteiros ainda não feitos"
    lbl1 = Label(favoritos_janela,text="Roteiros ainda não feitos", relief="flat",font=("Helvetica 12"), bg="white", fg="blue")
    lbl1.place(x=44,y=100) 

    #Label "Roteiros feitos"
    lbl2 = Label(favoritos_janela,text="Roteiros feitos", relief="flat",font=("Helvetica 12"), bg="white", fg="blue")
    lbl2.place(x=512,y=100) 




#Função que mostra o catálogo
def mostrarCatalogo(janela_principal,barra_menu,altura,imagem_clicada):
    #reconfigurar o comando da opção "Catálogo" da barra de menu
    barra_menu.entryconfigure("Catálogo", command="noaction")
    main_frame = Frame(janela_principal, bd=-2, bg="white")
    main_frame.pack(fill = BOTH, expand = 1)
    #Adicionar uma scrollbar https://www.youtube.com/watch?v=0WafQCaok6g
    my_canvas = Canvas(main_frame, bg="white", bd=-2)
    my_canvas.pack(side=LEFT,fill=BOTH,expand=1 )
    my_canvas.unbind_all("<MouseWheel>")

    my_scrollbar= Scrollbar(main_frame,orient=VERTICAL,command=my_canvas.yview)
    
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    
    second_frame = Frame(my_canvas, bg="white")
    my_canvas.create_window((0,0),window=second_frame,anchor="nw")

    #Este panedwindow define as dimensões da janela do catálogo, dimensões essas que vão variando dependo do roteiro que escolhemos. 
    #Roteiro grande = Height deste paned window maior. Roteiro pequeno = Height deste paned window menor
    catalogo = PanedWindow(second_frame ,width=1366,height=altura,bg="white") 
    catalogo.pack(side=TOP,fill=X) 
    #Text roteiro escolhido
    txt = Text(second_frame, wrap='word', bg="white", fg="black",cursor="arrow",selectbackground="#09d8be",bd=-2) #Para mudar o cursor, documento https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/cursors.html
    txt.place(x=435,y=66,width=497, height=7608)

    #tags que vão nos ajudar a mudar a cor da letra, o tamanho da letra ... na widget Text
    txt.tag_configure("titulo", justify='center', font="Helvetixa 20 bold")

    txt.tag_configure("descrição", font="Helvetixa 12")

    txt.tag_configure("local_a_visitar", font="Helvetixa 17", foreground="#E24841")

    txt.tag_configure("destacado", font="Helvetixa 17", foreground="#585858")
    
    txt.bind("<Double-Button-1>", lambda e: prevenirDefault(e,txt)) #Prevenir a ação que seja realizada, por defieto, pelo programa que é marcar a primeira linha do texto a azul

    #Entry pesquisa
    
    entry_pesquisa = Entry(second_frame, textvariable=pesquisa, relief="flat", bg="#F3F6FB", font=("Helvetica 13"))
    entry_pesquisa.place(x=47,y=30,height=27,width=205)

    #47,75 posição da primeira categoria
    #Praias
    # Gastronomia
    # Saúde e Bem-estar
    # Culturais
    # Natureza
    # Vinhos
    #Checkbutton
    txt_categorias = open("ficheiros\\categorias.txt", "r", encoding="utf-8")
    linhas = txt_categorias.readlines()
    txt_categorias.close()

    global categoria_selected, categorias_nomes
    reset_checkbuttons = 0
    if len(categoria_selected) == len(linhas):  #Se a lista já contêm todas as categorias existentes
        reset_checkbuttons = 1 #então não vai ser preciso da reset às checkbuttons

    categorias = [] # lista que vai inicializar as checkbuttons
    i = 0
    ultimo_y = 0
    for categoria in linhas:
        if reset_checkbuttons == 0:
            categorias_nomes.append(categoria[0:-1]) # -1 == len(lista)-1, ignoramos o último index porque é um espaço 
            categoria_selected.append(IntVar()) 
            categoria_selected[i].set(0)
        categorias.append(Checkbutton(second_frame, text=categorias_nomes[i], variable = categoria_selected[i],bg = "white", relief=FLAT,activebackground="white", highlightthickness = 0,command="noaction"))
        categorias[i].place(x = 47, y = 75 + i*25)
        ultimo_y = 75 + i*25
        i+=1


    #Label "Visualizações"
    lbl_visualizaçoes = Label(second_frame,text='Visualizações:', relief="flat",font=("Helvetica 11"), bg="white")
    lbl_visualizaçoes.place(x=47,y=ultimo_y+40) 
    

    #Label "Pontuação"
    lbl_pontuaçao = Label(second_frame,text='Pontuação:', relief="flat",font=("Helvetica 11"), bg="white")
    lbl_pontuaçao.place(x=47,y=ultimo_y+80)
    
    global img_seta_cima, img_seta_baixo
    img_seta_cima= Image.open("imagens/seta-para-cima.png")
    resize_img_seta_cima = img_seta_cima.resize((10,8),Image.ANTIALIAS) 
    img_seta_cima= ImageTk.PhotoImage(resize_img_seta_cima)

    img_seta_baixo = Image.open("imagens/seta-para-baixo.png")
    resize_img_seta_baixo= img_seta_baixo.resize((10,8),Image.ANTIALIAS) 
    img_seta_baixo= ImageTk.PhotoImage(resize_img_seta_baixo)

    #Listbox com os títulos dos roteiros existentes
    lbox_roteiros = Listbox(second_frame,relief="flat",bd=-2, bg="white",fg="#7E7E7E",font=('Helvetica', 11,"bold"), activestyle="none",highlightthickness=0,selectbackground='white',selectforeground='black') #documentação sobre listbox:https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/listbox.html
    lbox_roteiros.place(x=47,y=ultimo_y+150,height=401,width=318)

    if imagem_clicada :
        e = 0
        mudarCanvas(e,txt,lbox_roteiros,main_frame,janela_principal,barra_menu,imagem_clicada)
        return # se não tivéssemos o return, a função mostrarCatalogo() ia estar a correr duas vezes.

    lbox_roteiros.bind("<<ListboxSelect>>", lambda e: mudarCanvas(e,txt,lbox_roteiros,main_frame,janela_principal,barra_menu,imagem_clicada))
    
    #Botões seta - visualisações
    btn_seta_cima_visualicacoes= Button(second_frame,image=img_seta_cima,bg="white", activebackground="white",relief=SUNKEN,borderwidth=0,command=lambda:ordenarDescAscVisualizacoes(lbox_roteiros,0,nome_roteiro,roteiros_filtrados))
    btn_seta_cima_visualicacoes.place(x=150,y=ultimo_y+40)

    btn_seta_baixo_visualicacoes= Button(second_frame,image=img_seta_baixo,bg="white", activebackground="white",relief=SUNKEN,borderwidth=0,command=lambda:ordenarDescAscVisualizacoes(lbox_roteiros,1,nome_roteiro,roteiros_filtrados))
    btn_seta_baixo_visualicacoes.place(x=150,y=ultimo_y+50)

    #Botões seta - pontuação
    btn_seta_cima_pontuacao= Button(second_frame,image=img_seta_cima,bg="white", activebackground="white",relief=SUNKEN,borderwidth=0,command="noaction")
    btn_seta_cima_pontuacao.place(x=130,y=ultimo_y+80)

    btn_seta_baixo_pontuacao= Button(second_frame,image=img_seta_baixo,bg="white", activebackground="white",relief=SUNKEN,borderwidth=0,command="noaction")
    btn_seta_baixo_pontuacao.place(x=130,y=ultimo_y+90)

    #PanedWindow que divide o botão "Todos" do "Favoritos"
    title_bar = PanedWindow(second_frame,width=0,height=21,bd=-2, bg="#707070")
    title_bar.place(x=109, y=ultimo_y+120) 

    
    
    # botão "Favoritos"
    favoritos_btn = Button(second_frame, text='Favoritos', relief=SUNKEN, borderwidth=0,bd=-2, activebackground="white", font=("Helvetica", 12, "bold"), bg="white",fg="#7E7E7E",command=lambda:verFavoritos(todos_btn,favoritos_btn,lbox_roteiros))
    favoritos_btn.place(x=120,y=ultimo_y+120)

    # botão "Todos"
    todos_btn = Button(second_frame, text='Todos', relief=SUNKEN, borderwidth=0,bd=-2, activebackground="white", font=("Helvetica", 12, "bold"), bg="white",fg="black",command=lambda:verTodos(todos_btn,favoritos_btn,lbox_roteiros))
    todos_btn.place(x=42,y=ultimo_y+120)

    if a_ver_que_lista == "todos":
        verTodos(todos_btn,favoritos_btn,lbox_roteiros)
    else:
        verFavoritos(todos_btn,favoritos_btn,lbox_roteiros)

    #Botão para procurar/filtrar
    global img_procurar
    img_procurar= Image.open("imagens/search.png")
    resize_img_procurar = img_procurar.resize((20,20),Image.ANTIALIAS) 
    img_procurar= ImageTk.PhotoImage(resize_img_procurar)
    btn_procurar= Button(second_frame,image=img_procurar,bg="white", activebackground="white",relief=SUNKEN,borderwidth=0,command=lambda:procurarRoteiro(pesquisa,lbox_roteiros)) 
    btn_procurar.place(x=255,y=30)
    """  #PanedWindow teste3
    title_bar = PanedWindow(second_frame,width=47,height=58,bd=-2, bg="red")
    title_bar.place(x=0, y=0) 
    #PanedWindow teste3
    title_bar = PanedWindow(second_frame,width=205,height=29,bd=-2, bg="red")
    title_bar.place(x=47, y=102) 
    #PanedWindow teste3
    title_bar = PanedWindow(second_frame,width=205,height=33,bd=-2, bg="red")
    title_bar.place(x=47, y=145)  """

    #PanedWindow Secção dos Comentários
    comment_section = PanedWindow(second_frame,width=1366,height=110,bd=-2, bg="#F3F6FB")
    comment_section.pack(side=BOTTOM)   

    #Label "Comentários"
    lbl_comentarios = Label(comment_section,text='Comentários (0)', relief="flat",font=("Helvetica 16"), bg="#F3F6FB",bd = -2)
    lbl_comentarios.place(x=259,y=5) 

    #Entry para adicionar um comentário
    comentario = StringVar()
    comentario.set("Comentar")
    entry_comentario = Entry(comment_section, textvariable=comentario, font=("Helvetica 12"), bg="white", border=0, fg="#ABABAB")
    entry_comentario.place(x=259,y=50,height=25,width=848)

    
    #PanedWindow teste3
    # title_bar = PanedWindow(comment_section,width=259,height=60,bd=-2, bg="red")
    # title_bar.place(x=0, y=0) 

    #reconfigurar o comando da opção "Home" da barra de menu
    barra_menu.entryconfigure("Home", command=lambda:prepararJanelaPrincipal(janela_principal,comment_section,lbl_pontuaçao,lbl_visualizaçoes,entry_pesquisa,txt,main_frame,my_canvas,second_frame))
    global roteiro_selecionado
    if(roteiro_selecionado):

        my_scrollbar.pack(side=RIGHT, fill=Y)
        my_canvas.bind_all("<MouseWheel>", lambda event: on_mousewheel(event,my_canvas)) #Para conseguirmos fazer scroll com a tecla do meio do rato
        roteiro_selecionado = False
        
        txt_roteiros = open("ficheiros/roteiros.txt", "r", encoding="utf-8")
        roteiros = txt_roteiros.readlines()
        txt_roteiros.close()

        txt_favoritos = open("ficheiros/favoritos.txt", "r", encoding="utf-8")
        favoritos = txt_favoritos.readlines()
        txt_favoritos.close()
        roteiro_favorito = 0
        #coraçao
        for favorito in favoritos: # para cada utilizador existente na aplicação que ja marcou pelo menos um roteiro como favorito #
            campos = favorito.split(";")
            roteiro = campos[1].lower()
            nr_favoritos = len(campos) #quantos roteiros o utilizador tem como favoritos 
            if campos[0] == username_autenticado: #se o programa encontra-se na linha que contêm o nome do utilizador autenticado)
                for x in range(1,nr_favoritos): #iterar o id de cada roteiro marcado como favorito pelo utilizador autenticado
                    for roteiro in roteiros: # para cada roteiro existente no ficheiro roteiros.txt
                        campos1 = roteiro.split(";")
                        if campos1[0][0:1] == campos[x].replace("\n",""): #se o id do roteiro iterado no ficheiro roteiros.txt é igual ao id do roteiro marcado como favorito 
                            if nome_roteiro == campos1[1]:
                                roteiro_favorito = 1
        if roteiro_favorito : 
            coracao_btn =Button(second_frame,relief=SUNKEN, image=coracao, borderwidth=0,activebackground="white",activeforeground="lightblue",fg="white", font=("Helvetica 25 bold"), bg="white", command =lambda:desmarcarFavorito(coracao_btn,todos_btn,favoritos_btn,lbox_roteiros))
        else:
            coracao_btn =Button(second_frame,relief=SUNKEN, image=coracao_vazio, borderwidth=0,activebackground="white",activeforeground="lightblue",fg="white", font=("Helvetica 25 bold"), bg="white", command =lambda:marcarFavorito(coracao_btn,todos_btn,favoritos_btn,lbox_roteiros))

        coracao_btn.place(x=1000,y=130)

        
        # numero de visualizações
        nr_visualizacoes = StringVar()
        lbl_visualizacoes = Label(second_frame,textvariable=nr_visualizacoes, relief="flat",font=("Helvetica 13"), bg="white",bd = -2)
        mostrarNumeroVisualizacoes(nr_visualizacoes)
        lbl_visualizacoes.place(x=1050,y=97) 

        # pontuações
        btn_estrela1 = Button(second_frame,relief=SUNKEN, image=estrela, borderwidth=0,activebackground="white",activeforeground="lightblue",fg="white", font=("Helvetica 25 bold"), bg="white", command =lambda:darAvaliacao("1",username_autenticado,id_roteiro))
        btn_estrela1.place(x=1046,y=65) 
        btn_estrela2 = Button(second_frame,relief=SUNKEN, image=estrela, borderwidth=0,activebackground="white",activeforeground="lightblue",fg="white", font=("Helvetica 25 bold"), bg="white", command =lambda:darAvaliacao("2",username_autenticado,id_roteiro))
        btn_estrela2.place(x=1070,y=65)  
        btn_estrela3 = Button(second_frame,relief=SUNKEN, image=estrela, borderwidth=0,activebackground="white",activeforeground="lightblue",fg="white", font=("Helvetica 25 bold"), bg="white", command =lambda:darAvaliacao("3",username_autenticado,id_roteiro))
        btn_estrela3.place(x=1094,y=65) 
        btn_estrela4 = Button(second_frame,relief=SUNKEN, image=estrela, borderwidth=0,activebackground="white",activeforeground="lightblue",fg="white", font=("Helvetica 25 bold"), bg="white", command =lambda:darAvaliacao("4",username_autenticado,id_roteiro))
        btn_estrela4.place(x=1118,y=65) 
        btn_estrela5 = Button(second_frame,relief=SUNKEN, image=estrela, borderwidth=0,activebackground="white",activeforeground="lightblue",fg="white", font=("Helvetica 25 bold"), bg="white", command =lambda:darAvaliacao("5",username_autenticado,id_roteiro))
        btn_estrela5.place(x=1142,y=65) 

        btn_estrela1.bind("<Enter>", lambda e: on_estrela(e,estrela,btn_estrela1))
        btn_estrela1.bind("<Leave>", lambda _: mostrarPontuacao(btn_estrela1,btn_estrela2,btn_estrela3,btn_estrela4,btn_estrela5))

        btn_estrela2.bind("<Enter>", lambda e: on_estrela(e,estrela,btn_estrela2,btn_estrela1))
        btn_estrela2.bind("<Leave>", lambda _: mostrarPontuacao(btn_estrela1,btn_estrela2,btn_estrela3,btn_estrela4,btn_estrela5))
        
        btn_estrela3.bind("<Enter>", lambda e: on_estrela(e,estrela,btn_estrela3,btn_estrela2,btn_estrela1))
        btn_estrela3.bind("<Leave>", lambda _: mostrarPontuacao(btn_estrela1,btn_estrela2,btn_estrela3,btn_estrela4,btn_estrela5))

        btn_estrela4.bind("<Enter>", lambda e: on_estrela(e,estrela,btn_estrela4,btn_estrela3,btn_estrela2,btn_estrela1))
        btn_estrela4.bind("<Leave>", lambda _: mostrarPontuacao(btn_estrela1,btn_estrela2,btn_estrela3,btn_estrela4,btn_estrela5))

        btn_estrela5.bind("<Enter>", lambda e: on_estrela(e,estrela,btn_estrela5,btn_estrela4,btn_estrela3,btn_estrela2,btn_estrela1))
        btn_estrela5.bind("<Leave>", lambda _: mostrarPontuacao(btn_estrela1,btn_estrela2,btn_estrela3,btn_estrela4,btn_estrela5))

        mostrarPontuacao(btn_estrela1,btn_estrela2,btn_estrela3,btn_estrela4,btn_estrela5)

        mostrarRoteiro(txt,nome_roteiro)
    
    else:
        #Message "Consulte um roteiro"
        msg_roteiro = Message(second_frame,width=400,text="Nenhum roteiro selecionado", bg="white", font=("Helvetica 21 bold"), fg="#B0B0B0")
        msg_roteiro.place(x=484,y=348)


    
    
#-----------------\\----------------------------------------------
#Janela de log-in, inspirado no site: https://www.behance.net/gallery/134237737/Sign-up-Daily-UI?tracking_source=search_projects_recommended%7Cregistration
#e https://www.behance.net/gallery/126019893/Sign-in-form-for-a-yacht-club-website?tracking_source=search_projects_recommended%7Cregistration
window=Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
app_width = 1024
app_height = 768
x = (screen_width/2) - (app_width/2)
y = (screen_height/2) - (app_height/2)
window.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(app_width,app_height,x,y))
window.overrideredirect (True) #Remove a titlebar, porque vamos criar uma customizada
#Colocar a cor de fundo da janela de log-in para branco
window.configure(bg = "#fff")
log_in_frame = window #guarda a designação da janela inicial

username_autenticado = ""
tipo_utilizador_autenticado = "" #Variáveis que vão armazenar o username do utilizador que se autenticou e o tipo de utilizador
#Paned Window que permitirá que o utilizador clique nele e movimente a janela 
pw_formulario = PanedWindow(window,width=434,height=768,bd=-2,relief="raised", bg="white")
pw_formulario .place(x=590, y=0)

# botão para fechar/destruir a janela
close_button = Button(window, text='X', relief=SUNKEN, borderwidth=0, activebackground="white",activeforeground="lightblue", font=("Helvetica 18"), bg="white",fg="white",command=window.destroy)
close_button.place(x=980,y=0)

#botão para minimizar a janela
minimize_button=Button(window, text = "-",relief=SUNKEN, borderwidth=0,activebackground="white",activeforeground="lightblue",fg="white", font=("Helvetica 25 bold"), bg="white", command = lambda:minimizar(window))
minimize_button.place(x=950,y=-15)

close_button.bind("<Enter>", on_enter)
minimize_button.bind("<Enter>", on_enter)
close_button.bind("<Leave>", on_leave)
minimize_button.bind("<Leave>", on_leave)

#Três formas diferentes de chamar o evento "bind" que foram aprendidas pela resposta de Bryan Oakley no site https://stackoverflow.com/questions/4055267/tkinter-mouse-drag-a-window-without-borders-eg-overridedirect1
pw_formulario.bind('<B1-Motion>', lambda event:moverWindow(event,window)) # Evento que vai sendo disparado á medida que vamos movendo o rato, com a tecla do lado esquerdo do rato (i.e, a tecla Button-1) pressionado 
pw_formulario.bind("<ButtonPress-1>", começarMoverWindow) # Evento que é disparado quando clicamos sobre a title_bar
window.bind("<Return>", lambda event:verificarDadosLogin(event,email,password)) # Evento que é disparado quando clicamos no enter

#Message "Gestor de Roteiros"
msg_title = Message(window,width=400,text="Gestor de Roteiros", bg="white", font=("Helvetica 21 bold"))
msg_title.place(x=667,y=178)

#Message "Não tens uma conta?"
msg2 = Message(window,width=282,text="Não tens uma conta?", bd=-5,bg="white", font=("Helvetica 11 bold"))
msg2.place(x=691,y=565)

#Botao "Regista-te!"
btn_registate = Button(window,text="Regista-te!",relief=SUNKEN, borderwidth=0,bg="white", activebackground="white",bd=-5, fg="#29A9FF",font=("Helvetica 11 bold"), command=colocarFormRegisto)
btn_registate.place(x=840,y=558)

""" 
USEM ESTES PANEDWINDOWS PARA DISPOR OS WIDGETS DE FORMA IGUAL COMO ESTÃO DISPOSTOS NO PROTOTIPO
#PanedWindow teste3
title_bar = PanedWindow(window,width=165,height=15,bd=-2, bg="red")
title_bar.place(x=590, y=615) 

#PanedWindow teste3
title_bar = PanedWindow(window,width=184,height=2,bd=-2, bg="#29A9FF")
title_bar.place(x=590, y=363)  

#PanedWindow teste3
title_bar = PanedWindow(window,width=2,height=2,bd=-2, bg="#29A9FF")
title_bar.place(x=590, y=433)   """

#Botão "Entrar"
img_btn_entrar= PhotoImage(file="imagens/Entrar.png")
img_btn_entrar_hover = PhotoImage(file="imagens/Entrar_hover.png")
btn_entrar= Button(window,image=img_btn_entrar,bg="white", activebackground="white",relief=SUNKEN,borderwidth=0, font=("Helvetica 16 bold"),command=lambda event=0:verificarDadosLogin(event,email,password)) #Não vamos fazer nada com o argumento "e", acrescentamos este argumento (como podiamos ter escrito outra coisa como argumento), porqeu esta função também é chamada num bind (o bind implicitamente passa o argumento de evento) 
btn_entrar.place(x=727,y=435)

#Botão "Criar Conta"
img_btn_registar= PhotoImage(file="imagens/Criar_conta.png")
img_btn_registar_hover = PhotoImage(file="imagens/Criar_conta_hover.png")
btn_criar_conta= Button(window,image=img_btn_registar,bg="white", activebackground="white",relief=SUNKEN,borderwidth=0, font=("Helvetica 16 bold")) 

#resumo dos eventos mais usados em tkinter https://stackoverflow.com/questions/32289175/list-of-all-tkinter-events 
btn_entrar.bind("<ButtonPress-1>", lambda event:mudarLayoutBotao(event,btn_criar_conta,img_btn_registar_hover,img_btn_entrar_hover)) 
btn_entrar.bind("<ButtonRelease-1>", lambda event:reporLayoutBotao(event,btn_criar_conta,img_btn_registar,img_btn_entrar)) 

#Entry Email --- Mudar a altura e a largura da entry: https://stackoverflow.com/questions/24501606/tkinter-python-entry-height
email = StringVar()
email.set("Email")
entry_email = Entry(window, width=20, textvariable=email, font=("Helvetica 16"), bg="white", border=0, fg="#ABABAB")
entry_email.place(x=685,y=293,height=35,width=245)

#Linha da entry do email
email_line = PanedWindow(window,width=245,height=1,bd=-2, bg="#707070")
email_line.place(x=685, y=328) 

#Entry Password
password = StringVar()
password.set("Password")
entry_password = Entry(window, width=20, textvariable=password, font=("Helvetica 16"), bg="white", border=0,fg="#ABABAB")
entry_password.place(x=685,y=363,height=35,width=245)

#Linha da entry da password
password_line = PanedWindow(window,width=245,height=1,bd=-2, bg="#707070")
password_line.place(x=685, y=398) 

entry_email.bind('<ButtonPress-1>', lambda event:mudarTextoEmail(event,entry_email,email,btn_entrar,minimize_button))
entry_password.bind('<ButtonPress-1>', lambda event:mudarTextoPasword(event,entry_password,password,entry_email))
entry_email.bind('<Tab>', lambda event:mudarTextoPasword(event,entry_password,password,entry_email))
btn_entrar.bind("<Tab>", lambda event:mudarTextoEmail(event,entry_email,email,btn_entrar,minimize_button)) 

#Redimensionar as cinco imagens que vão aparecer na janela de log-in
log_in_img1= Image.open("imagens/praia.jpg")
log_in_img2= Image.open("imagens/termas.jpg")
log_in_img3= Image.open("imagens/castelo.jpg")
log_in_img4= Image.open("imagens/moinhos_de_rei.jpg")
log_in_img5= Image.open("imagens/pasteis.jpg")
resize_img1 = log_in_img1.resize((590,768),Image.ANTIALIAS) 
resize_img2 = log_in_img2.resize((590,768),Image.ANTIALIAS) 
resize_img3 = log_in_img3.resize((590,768),Image.ANTIALIAS) 
resize_img4 = log_in_img4.resize((590,768),Image.ANTIALIAS) 
resize_img5 = log_in_img5.resize((590,768),Image.ANTIALIAS) 
log_in_img1= ImageTk.PhotoImage(resize_img1)
log_in_img2= ImageTk.PhotoImage(resize_img2)
log_in_img3= ImageTk.PhotoImage(resize_img3)
log_in_img4= ImageTk.PhotoImage(resize_img4)
log_in_img5= ImageTk.PhotoImage(resize_img5)
#imagem de background da pagina principal
img_bg_home= Image.open("imagens/bg_pagina_principal.jpg")
resize = img_bg_home.resize((1366,768),Image.ANTIALIAS) #tHE IMAGE WILL HAVE 200 widh and 200 height
img_bg_home= ImageTk.PhotoImage(resize)
#Canvas que mostra a imagem do log-in
ctn_canvas = Canvas(window,relief="flat", bd=-2,height=768,width=590)
ctn_canvas.place(x=0,y=0)
image_id = ctn_canvas.create_image(295,384,image=log_in_img1)
i = 1
mudarImagem(window,i,ctn_canvas,image_id, log_in_img1, log_in_img2, log_in_img3, log_in_img4, log_in_img5)


# variaveis globais que armazenam imagens usadas na janela principal ------------------
pesquisa = StringVar()

ovo_pascoa= Image.open("imagens/ovo_pascoa.png")
resize_ovo_pascoa = ovo_pascoa.resize((16,20),Image.ANTIALIAS)
ovo_pascoa =  ImageTk.PhotoImage(resize_ovo_pascoa)

melgaco= Image.open("imagens/2.jpg")
resize_melgaco = melgaco.resize((200,180),Image.ANTIALIAS)
melgaco =  ImageTk.PhotoImage(resize_melgaco)

onde_comer= Image.open("imagens/1.jpg")
resize_onde_comer = onde_comer.resize((200,180),Image.ANTIALIAS)
onde_comer =  ImageTk.PhotoImage(resize_onde_comer)

coracao_vazio= Image.open("imagens/coraçao-branco.png")
resize_coracao_vazio = coracao_vazio.resize((20,20),Image.ANTIALIAS)
coracao_vazio =  ImageTk.PhotoImage(resize_coracao_vazio)

coracao= Image.open("imagens/coraçao.png")
resize_coracao = coracao.resize((20,20),Image.ANTIALIAS)
coracao =  ImageTk.PhotoImage(resize_coracao)

estrela= Image.open("imagens/estrela_amarela.png")
resize_estrela = estrela.resize((25,25),Image.ANTIALIAS)
estrela =  ImageTk.PhotoImage(resize_estrela)

estrela_vazia= Image.open("imagens/estrela_vazia.png")
resize_estrela_vazia = estrela_vazia.resize((25,25),Image.ANTIALIAS)
estrela_vazia =  ImageTk.PhotoImage(resize_estrela_vazia)

estrela_meia= Image.open("imagens/estrela_meia.png")
resize_estrela_meia = estrela_meia.resize((25,25),Image.ANTIALIAS)
estrela_meia =  ImageTk.PhotoImage(resize_estrela_meia)

consultar_img= Image.open("imagens/Consultar.jpg")
resize_consultar_img = consultar_img.resize((159,43),Image.ANTIALIAS)
consultar_img =  ImageTk.PhotoImage(resize_consultar_img)

consultar_img_hover= Image.open("imagens/Consultar_hover.jpg")
resize_consultar_img_hover = consultar_img_hover.resize((159,43),Image.ANTIALIAS)
consultar_img_hover =  ImageTk.PhotoImage(resize_consultar_img_hover)

feito_img= Image.open("imagens/Feito.jpg")
resize_feito_img = feito_img.resize((159,43),Image.ANTIALIAS)
feito_img =  ImageTk.PhotoImage(resize_feito_img)

feito_img_hover= Image.open("imagens/Feito_hover.jpg")
resize_feito_img_hover = feito_img_hover.resize((159,43),Image.ANTIALIAS)
feito_img_hover =  ImageTk.PhotoImage(resize_feito_img_hover)

remover_img= Image.open("imagens/Remover.jpg")
resize_remover_img = remover_img.resize((159,43),Image.ANTIALIAS)
remover_img=  ImageTk.PhotoImage(resize_remover_img)

remover_img_hover= Image.open("imagens/Remover_hover.jpg")
resize_remover_img_hover = remover_img_hover.resize((159,43),Image.ANTIALIAS)
remover_img_hover =  ImageTk.PhotoImage(resize_remover_img_hover)

#Nome do roteiro selecionado para ler
nome_roteiro = ""

roteiros_filtrados = []

window.mainloop()
