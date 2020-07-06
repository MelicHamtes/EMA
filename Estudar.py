import os
import platform
import tkinter
from tkinter import messagebox
from Banco_armazenamento.Banco_dados import Banco_dados
from Flash_card import Flash_Card 

"""
Classe será chamada sempre que se quiser abrir os cards para estudo; classe no botão do MENU_ESTUDAR
e ABRIR em CONF. CARDS
"""
class Estudar:
	def __init__(self, usuario):
		self.usuario = usuario
		self.janela_estudo = tkinter.Tk()
		self.janela_estudo.geometry("400x230+350+150")
		#self.janela_estudo.resizable(0,0)
		self.janela_estudo.title('Estudar')
		self.janela_estudo.protocol('WM_DELETE_WINDOW', lambda: self.fechar_janela(self.janela_estudo))

		self.modo = ''
		self.numero_cards = 0

		if platform.system() == 'Linux':
			self.dir_path = os.path.dirname(os.path.realpath(__file__)) + '/Banco_armazenamento/db/Ema'
			bd = Banco_dados()
			bd.conectar()
			self.lista_decks = bd.listar_decks(self.usuario)
		elif platform.system() == 'Windows':
			self.dir_path = os.path.dirname(os.path.realpath(__file__)) + '\\Banco_armazenamento\\db\\Ema'
			bd = Banco_dados()
			bd.conectar()
			self.lista_decks = bd.listar_decks(self.usuario)

		var = int()

		fram=tkinter.Frame(self.janela_estudo)
		fram.pack(anchor=tkinter.NW)

		frameS=tkinter.Frame(fram,width=170,height=210)
		frameS.pack(side=tkinter.LEFT)

		self.listbox=tkinter.Listbox(frameS)
		self.listbox.pack()
		self.selecionar_deck()

		self.btOP=tkinter.Button(frameS,text="Selecionar",command=self.item_selecionado_deck)
		self.btOP.pack(expand=1,fill=tkinter.BOTH)



		self.frOpcao=tkinter.Frame(fram,width=170,height=210)

		frDeck=tkinter.LabelFrame(self.frOpcao,text="Deck Selecionado")
		self.lbD=tkinter.Label(frDeck,text="Nome:\nCards:")
		self.lbD.pack(side=tkinter.LEFT)
		self.lbD1=tkinter.Label(frDeck,text="ppg\n30",font=("Arial","8","bold"))
		self.lbD1.pack()
		frDeck.pack(anchor=tkinter.NW)

		var= True
		labSelect=tkinter.LabelFrame(self.frOpcao,text="Selecione o modo")
		labSelect.pack()
		rb1 = tkinter.Radiobutton(labSelect, text='Padrão', variable=var , value=1,command=self.selecionar_modo_1 )
		rb1.pack(anchor=tkinter.NW)
		rb1.select()
		rb2 = tkinter.Radiobutton(labSelect, text='Especificar número de cartões', variable=var, value=2,command=self.botao_selecionar_modo_2)
		rb2.pack(anchor=tkinter.NW)

		self.frNC= tkinter.LabelFrame(self.frOpcao)
		lbN= tkinter.Label(self.frNC,text="Nº")
		lbN.pack(side=tkinter.LEFT)
		self.entN=tkinter.Entry(self.frNC)
		self.entN.pack(side=tkinter.LEFT)
		self.frNC.pack()
		self.frNC.pack_forget()

		self.frOpcao.pack(side=tkinter.LEFT)
		self.frOpcao.pack_forget()

		self.btOPen=tkinter.Button(fram,text="Abrir",width=10,height=1, command=self.iniciar)
		self.btOPen.pack()
		self.btOPen.pack_forget()
	 
	def selecionar_modo_1(self):
		self.modo = 'padrão'
		self.frNC.pack_forget()

	def selecionar_modo_2(self):
		self.toplevel_modo_2 = tkinter.Toplevel(self.janela_estudo)
		self.toplevel_modo_2.geometry('120x40')
		self.toplevel_modo_2.resizable(0,0)
		lb_modo_2 = tkinter.Label(self.toplevel_modo_2, text='nº')
		lb_modo_2.pack(side=tkinter.LEFT)
		
		bt = tkinter.Button(self.toplevel_modo_2, text='ok', command=self.botao_selecionar_modo_2)
		bt.pack(side=tkinter.RIGHT)

		self.ent_modo_2 = tkinter.Entry(self.toplevel_modo_2, width=7)
		self.ent_modo_2.pack(side=tkinter.RIGHT)

	def botao_selecionar_modo_2(self):
		self.modo = 'numero de cards'
		self.frNC.pack(anchor=tkinter.NW)

	def selecionar_deck(self):
		#self.bt1['state'] = tkinter.DISABLED
		#self.bt2['state'] = tkinter.DISABLED
		#self.toplevel_selecionar = tkinter.Toplevel(self.janela_estudo)
		#self.toplevel_selecionar.protocol('WM_DELETE_WINDOW', lambda: self.fechar_toplevel(self.toplevel_selecionar)) 
		#self.toplevel_selecionar.minsize(170,210)
		#self.toplevel_selecionar.maxsize(170,210)
		#self.toplevel_selecionar.title('Decks')
		#self.listbox = tkinter.Listbox(self.toplevel_selecionar, font='-size 10', width=24, height=10, bd=0)
		#self.listbox.pack()

		for i in range(0, len(self.lista_decks)):
			self.listbox.insert(i, self.lista_decks[i])

		#bt = tkinter.Button(self.toplevel_selecionar, text='Selecionar', command=self.item_selecionado_deck)
		#bt.pack(side=tkinter.BOTTOM)


	def item_selecionado_deck(self):
		try:
			self.frOpcao.pack()
			self.btOPen.pack(side=tkinter.BOTTOM)

			item_selecionado_listbox = self.listbox.curselection()
			self.item_selecionado_listbox = self.listbox.get(item_selecionado_listbox[0])
			self.lbD1['text'] = ""
			self.lbD1['text'] = self.item_selecionado_listbox

			#self.lb3['text'] = 'Deck selecionado: ' + self.item_selecionado_listbox
			#self.lb3.place(y=120)
			#self.bt2.place(x=180, y=120)
			#self.bt1['text'] = 'Trocar'
			#self.bt1.place(x=180, y=150)
			#self.fechar_toplevel(self.toplevel_selecionar)
		except(IndexError):
			messagebox.showerror('Erro','Nenhum deck foi selecionado')
		

	def iniciar(self):
		if self.modo == 'padrão':
			self.janela_estudo.destroy()
			fc = Flash_Card(self.item_selecionado_listbox,self.modo)
			deck_estudo = Estudar(self.usuario)
		elif self.modo == 'numero de cards':
			self.numero_cards = int(self.entN.get())
			self.janela_estudo.destroy()
			fc = Flash_Card(self.item_selecionado_listbox, self.modo, self.numero_cards)
			deck_estudo = Estudar(self.usuario)

	def fechar_toplevel(self, toplevel):
		toplevel.destroy()
		self.bt1['state'] = tkinter.NORMAL
		self.bt2['state'] = tkinter.NORMAL

	def fechar_janela(self, janela):
		self.valor = False
		janela.destroy()

if __name__ == '__main__':
	app = Estudar()


