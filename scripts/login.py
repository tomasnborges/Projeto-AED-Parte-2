from tkinter import messagebox

#Verificar se o email e a password coincidem com o email e a password da conta de algum utilizador já registado
def verificarConta(e,email,password):
    utilizadores_txt = open( "ficheiros\\utilizadores.txt", "r", encoding="utf-8")
    linhas = utilizadores_txt.readlines()
    utilizadores_txt.close()
    for linha in linhas:
        campos = linha.split(";")
        if email.get() == campos[1] and password.get() == campos[2]:
            username_autenticado = campos[0] 
            ultimo_index = len(campos[3])-1
            tipo_utilizxador = campos[3][0:ultimo_index]
            return [username_autenticado,tipo_utilizxador]
    messagebox.showerror(title="Insucesso", message="Dados incorretos")
    return False
    
#Função que regista uma conta nova
def registarConta(e,username,conf_password,email,password,entry_conf_password,entry_username,username_line,conf_password_line,btn_tenho_conta):
    username = username.get()
    password = password.get()
    conf_password = conf_password.get()
    email = email.get()
    if email.count("@") == 0: #Se o email não conter um "@"
        messagebox.showerror(title="Insucesso", message="O Email Não É Válido")
        return False
    if password != conf_password: #Se as duas passwords não coincidireem uma com a outra
        messagebox.showerror(title="Insucesso", message="As Passwords Não Coincidem")
        return False
    utilizadores_txt = open("ficheiros\\utilizadores.txt", "r+", encoding="utf-8")
    linhas = utilizadores_txt.readlines()
    for linha in linhas:
        campos = linha.split(";")
        if username == campos[0]:
            messagebox.showerror(title="Insucesso", message="Nome de Utilizador já Existe")
            utilizadores_txt.close()
            return False
        if email == campos[1]:
            messagebox.showerror(title="Insucesso", message="Email já existe")
            utilizadores_txt.close()
            return False
    messagebox.showinfo(title="Sucesso!", message="Conta Criada Com Sucesso" )
    conta_info = "\n" + username + ";" + email + ";" + password + ";" + "user"
    utilizadores_txt.write(conta_info)
    utilizadores_txt.close()
    """ colocarFormLogIn(entry_conf_password,entry_username,username_line,conf_password_line,btn_tenho_conta) ----- ERRADO """
    return True
