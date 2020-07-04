#-*-coding:utf8-*-
from tkinter import *

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

        self.nomeLabel = Label(self.segundoContainer,text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.senhaLabel = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)

        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Autenticar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 15   
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

        self.Cadastro = Label(self.quintoContainer,text="Ainda não cadastrado? Clique aqui->")
        self.Cadastro['font'] = self.fontePadrao
        self.Cadastro.pack(side=LEFT)
        self.BtC = Button(self.quintoContainer,text="Cadastrar-se", width= 8, command=self.cadastrar)
        self.BtC['font'] = ("Calibri", "8")
        self.BtC.pack(side=LEFT)

        self.master.mainloop()

    #Método verificar senha
    def verificaSenha(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "usuariodevmedia" and senha == "dev":
            self.mensagem["text"] = "Autenticado"
        else:
            self.mensagem["text"] = "Erro na autenticação"

    def cadastrar(self):
        self.autenticar['state'] = DISABLED
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


        self.titulo = Label(self.primeiroContainer, text=" Cadastrar Dados do usuário")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomeLabel = Label(self.segundoContainer,text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 34
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)

        self.senhaLabel = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)

        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 34
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        self.repita_senhaLable = Label(self.quartoContainer, text='Senha *', font=self.fontePadrao)
        self.repita_senhaLable.pack(side=LEFT)

        self.repitaSenha = Entry(self.quartoContainer)
        self.repitaSenha["width"] = 33
        self.repitaSenha["font"] = self.fontePadrao
        self.repitaSenha['show'] = '*'
        self.repitaSenha.pack(side=LEFT)

        self.email = Label(self.quintoContainer, text='E-mail', font=self.fontePadrao)
        self.email.pack(side=LEFT)

        self.emailEntry = Entry(self.quintoContainer)
        self.emailEntry["width"] = 34
        self.emailEntry["font"] = self.fontePadrao
        self.emailEntry.pack(side=LEFT)

        self.username = Label(self.sextoContainer, text='Username', font=self.fontePadrao)
        self.username.pack(side=LEFT)

        self.usernameEntry = Entry(self.sextoContainer)
        self.usernameEntry["width"] = 31
        self.usernameEntry["font"] = self.fontePadrao
        self.usernameEntry.pack(side=LEFT)
      
        self.autenticar = Button(self.setimoContainer, command=self.sair)
        self.autenticar["text"] = "Cadastrar"
        self.autenticar["font"] = ("Calibri", "8")
        self.autenticar["width"] = 12
        self.autenticar.pack(side=BOTTOM)

    def sair(self):
        self.master.destroy()
        app = Application()


App = Application()
