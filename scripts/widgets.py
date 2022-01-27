#Função que muda automaticamente as imagens na janela de log-in a cada 3 segundos
def mudarImagem(window,i,canvas,image_id, *imagens):
    if i==6:
        i=1
    if i==1:
        canvas.itemconfig(image_id,image=imagens[0])  
    elif i==2:
        canvas.itemconfig(image_id,image=imagens[1]) 
    elif i==3:
        canvas.itemconfig(image_id,image=imagens[2]) 
    elif i==4:
        canvas.itemconfig(image_id,image=imagens[3])
    elif i==5:
        canvas.itemconfig(image_id,image=imagens[4])
    i+=1
    #Mudar a imagem automaticamente sem usar o time.sleep mas sim a método "after" do tkinter - site:https://www.geeksforgeeks.org/python-after-method-in-tkinter/
    window.after(3000,lambda :mudarImagem(window,i,canvas,image_id, *imagens)) #Depois de 2000 ms, o programa vai chamar novamente a função

#Como removemos a title_bar original do tkinter, as funções nativas de minimizar, maximizar e de mover a janela deixam de existir 
# por isso, tivemos que criar uma função que faz mais ou menos esse trabalho : inspirado -> https://stackoverflow.com/questions/29186327/tclerror-cant-iconify-override-redirect-flag-is-set
def minimizar(window):
    window.update_idletasks()
    window.overrideredirect(False)
    window.state('iconic')
    verificarJanelaAberta(window)

#Função que move a janela
def moverWindow(event,window):
    deltax = event.x - startX
    deltay = event.y - startY
    x = window.winfo_x() + deltax
    y = window.winfo_y() + deltay
    window.geometry(f"+{x}+{y}")

#Função que deteta as posições iniciais do cursor quando clicamos com o rato por cima da PanedWindow que permitirá a janela mover-se
def começarMoverWindow(event):
    global startX, startY
    startX = event.x #posição x inicial do cursor 
    startY = event.y #posição y inicial do cursor 

#Criamos esta função porque descobrimos que quando removemos a title bar original do Tkinter, não podemos mais minimizar o programa
#Para podermos voltar a minimizar temos que definir overrideredirect para False. Se voltarmos a abrir a aplicação minimizada
#aperecer-nos-á a title bar original. Portanto, criamos esta função que, a cada 1000 miliseegundos vai verificar se a aplicação minimizada
#foi aberta. Se foi aberta, então vai voltar a remover a title_bar original.
def verificarJanelaAberta(window):
    if 'normal' == window.state():
        window.overrideredirect(True)
        return
    window.after(1000,lambda:verificarJanelaAberta(window)) 
        
#https://stackoverflow.com/questions/49888623/tkinter-hovering-over-button-color-change
def on_enter(e):
     e.widget.configure(fg='black') 

def on_leave(e):
    e.widget.configure(fg='white') 

def on_estrela(e,estrela,*widgets):
    for widget in widgets:
        widget.configure(image = estrela) 
    

#Função que muda o texto "Email" da entry email para "" e configura a cor da letra
def mudarTextoEmail(event,entry_email,email,btn_entrar,minimize_button):
    entry_email.configure(fg = "black")
    email.set("")
    btn_entrar.unbind("<Tab>")  #Remove o event handler <Tab> para o bind não ser disparado mais nenhuma vez
    #Damos unbind porque só queremos que esta função seja chamada apenas uma vez, ou seja, seja chamda quando clicamos pela primeira vez, 
    # ou com o tab ou com a tecla direita do rato, na entry "Email". Se o utilizador clicar novamente, esta função não será chamada.
    minimize_button.unbind("<Tab>") 
    entry_email.unbind('<ButtonPress-1>')

#Função que muda o texto "Nome de Utilizador" da entry username para "" e configura a cor da letra
def mudarTextoUsername(e, entry_username, username,entry_conf_password):
    entry_username.configure(fg = "black")
    username.set("")
    entry_username.unbind('<ButtonPress-1>')
    entry_conf_password.unbind("<Tab>")

#Função que muda o texto "Password" da entry password para "" e configura o atributo show e a cor da letra
def mudarTextoPasword(event,entry_password,password,entry_email):
    entry_password.configure(fg = "black")
    password.set("")
    entry_password.configure(show="*")
    entry_email.unbind("<Tab>")  
    entry_password.unbind('<ButtonPress-1>')

def mudarTextoConfPassword(event, entry_conf_password,conf_password,entry_password):
    entry_conf_password.configure(fg = "black")
    conf_password.set("")
    entry_conf_password.config(show="*")
    entry_password.unbind("<Tab>")  
    entry_conf_password.unbind('<ButtonPress-1>')
    entry_password.unbind("<Tab>")

#Mudar o layout do botao 
def mudarLayoutBotao(e,btn_criar_conta,img_btn_registar_hover,img_btn_entrar_hover):
    if e.widget == btn_criar_conta:
        e.widget.configure(image = img_btn_registar_hover) 
    else:
        e.widget.configure(image = img_btn_entrar_hover) 

#Repor o layout do botao
def reporLayoutBotao(e,btn_criar_conta,img_btn_registar,img_btn_entrar):
    if e.widget == btn_criar_conta:
        e.widget.configure(image = img_btn_registar) 
    else:
        e.widget.configure(image = img_btn_entrar) 