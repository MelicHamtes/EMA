#-*-coding:utf8-*-
from tkinter import *
from tkinter import messagebox
from Banco_armazenamento.Banco_dados import Banco_dados
from Usuario import Usuario
from Menu import Menu

class Application:
    def __init__(self):
        self.master = Tk()
        self.master.resizable(0,0)
        self.master.title('Login')
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(self.master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(self.master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(self.master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(self.master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.quintoContainer = Frame(self.master)
        self.quintoContainer["padx"] = 20
        self.quintoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Dados do usuário")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomeLabelLogin = Label(self.segundoContainer,text="Login", font=self.fontePadrao)
        self.nomeLabelLogin.pack(side=LEFT)

        self.nomeLogin = Entry(self.segundoContainer)
        self.nomeLogin["width"] = 30
        self.nomeLogin["font"] = self.fontePadrao
        self.nomeLogin.pack(side=LEFT)

        self.senhaLabelLogin = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao)
        self.senhaLabelLogin.pack(side=LEFT)

        self.senhaLogin = Entry(self.terceiroContainer)
        self.senhaLogin["width"] = 30
        self.senhaLogin["font"] = self.fontePadrao
        self.senhaLogin["show"] = "*"
        self.senhaLogin.pack(side=LEFT)

        self.autenticarLogin = Button(self.quartoContainer)
        self.autenticarLogin["text"] = "Autenticar"
        self.autenticarLogin["font"] = ("Calibri", "8")
        self.autenticarLogin["width"] = 15   
        self.autenticarLogin["command"] = self.verificaSenha
        self.autenticarLogin.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

        self.Cadastro = Label(self.quintoContainer,text="Ainda não cadastrado? Clique aqui->")
        self.Cadastro['font'] = self.fontePadrao
        self.Cadastro.pack(side=LEFT)
        self.BtC = Button(self.quintoContainer,text="Cadastrar-se", width= 8, command=self.cadastrar_toplevel)
        self.BtC['font'] = ("Calibri", "8")
        self.BtC.pack(side=LEFT)

        self.master.mainloop()

    #Método verificar senha
    def verificaSenha(self):
        usuario = self.nomeLogin.get()
        senha = self.senhaLogin.get()
        print(usuario)
        print(senha)
        self.bd = Banco_dados()
        self.bd.conectar()
        login = self.bd.puxar_login()
        self.bd.fechar_banco()

        for index, index2 in login.items():
            if usuario != '' and senha != '':
                if index == usuario and index2[0] == senha:
                    self.Menu()
                    print('Logado')
                elif index2[1] == usuario and index2[0] == senha:
                     self.Menu()    
                else:       
                    messagebox.showerror('Login:','Login e/ou senha incorretos')
            elif usuario == '' and senha == '':
                messagebox.showerror('Erro:','O login e senha estão vazios')         
            elif usuario == '':
                messagebox.showerror('Erro:','O login está vazio')
            elif senha == '':
                messagebox.showerror('Erro:',' A senha está vazio')    

    def Menu(self):
        self.master.destroy()
        menu = Menu()

    def cadastrar_toplevel(self):
        self.autenticarLogin['state'] = DISABLED
        self.master.withdraw()
        self.toplevel = Toplevel(self.master)
        self.toplevel.protocol('WM_DELETE_WINDOW', lambda: self.sair())
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(self.toplevel)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(self.toplevel)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(self.toplevel)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(self.toplevel)
        self.quartoContainer["padx"] = 20
        self.quartoContainer['pady'] = 0
        self.quartoContainer.pack()

        self.quintoContainer = Frame(self.toplevel)
        self.quintoContainer["padx"] = 20
        self.quintoContainer.pack()

        self.sextoContainer = Frame(self.toplevel)
        self.sextoContainer["padx"] = 30
        self.sextoContainer.pack()

        self.setimoContainer = Frame(self.toplevel)
        self.setimoContainer["pady"] = 20
        self.setimoContainer.pack()

        self.oitavoContainer = Frame(self.toplevel)
        self.oitavoContainer["padx"] = 20
        self.oitavoContainer.pack()

        self.nonoContainer = Frame(self.toplevel)
        self.nonoContainer["padx"] = 40
        self.nonoContainer.pack()

        self.bt1 = Button(self.segundoContainer, text='*', width=0, height=0, bd=0)
        self.bt1.pack(side=RIGHT)

        self.bt2 = Button(self.terceiroContainer, text='*', width=0, height=0, bd=0)
        self.bt2.pack(side=RIGHT)

        self.bt3 = Button(self.quartoContainer, text='*', width=0, height=0, bd=0)
        self.bt3.pack(side=RIGHT)

        self.bt4 = Button(self.quintoContainer, text='*', width=0, height=0, bd=0)
        self.bt4.pack(side=RIGHT)

        self.bt5 = Button(self.sextoContainer, text='*', width=0, height=0, bd=0)
        self.bt5.pack(side=RIGHT)



        self.titulo = Label(self.primeiroContainer, text=" Cadastrar Dados do usuário")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomeLabel = Label(self.segundoContainer,text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.senhaLabel = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)

        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 29
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        self.repita_senhaLable = Label(self.quartoContainer, text='Senha *', font=self.fontePadrao)
        self.repita_senhaLable.pack(side=LEFT)

        self.repitaSenha = Entry(self.quartoContainer)
        self.repitaSenha["width"] = 28
        self.repitaSenha["font"] = self.fontePadrao
        self.repitaSenha['show'] = '*'
        self.repitaSenha.pack(side=LEFT)

        self.email = Label(self.quintoContainer, text='E-mail', font=self.fontePadrao)
        self.email.pack(side=LEFT)

        self.emailEntry = Entry(self.quintoContainer)
        self.emailEntry["width"] = 29
        self.emailEntry["font"] = self.fontePadrao
        self.emailEntry.pack(side=LEFT)

        self.username = Label(self.sextoContainer, text='Username', font=self.fontePadrao)
        self.username.pack(side=LEFT)

        self.usernameEntry = Entry(self.sextoContainer)
        self.usernameEntry["width"] = 26
        self.usernameEntry["font"] = self.fontePadrao
        self.usernameEntry.pack(side=LEFT)
      
        self.autenticar = Button(self.setimoContainer, command=self.cadastrar)
        self.autenticar["text"] = "Cadastrar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar.pack(side=BOTTOM)

    def cadastrar(self):
        nome = self.nome.get()
        senha = self.senha.get()
        email = self.emailEntry.get()
        username = self.usernameEntry.get()
        self.usuario_control = Usuario() 
        self.usuario_control.nome = nome
        self.usuario_control.senha = senha
        self.usuario_control.email = email
        self.usuario_control.username = username

        try:
            if self.usuario_control.nome == 'Erro: nome não pode conter números' or 'Erro: vazio':
                raise Exception(self.usuario_control.nome)
            if self.usuario_control.senha == 'Erro: número de caracteres insuficientes' or 'Erro: vazio':
                raise Exception()
        except Exception as error:
            messagebox.showerror('Erro', error)

    def sair(self):
        self.master.destroy()
        app = Application()

App = Application()
