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
		self.janela_estudo.geometry("400x210+450+250")
		#self.janela_estudo.resizable(0,0)
		self.janela_estudo.title('Estudar')
		self.janela_estudo.protocol('WM_DELETE_WINDOW', lambda: self.fechar_janela(self.janela_estudo))

		self.modo = ''
		self.numero_cards = 0

		if platform.system() == 'Linux':
			bd = Banco_dados()
			bd.conectar()
			self.lista_decks = bd.listar_decks(self.usuario)
			bd.fechar_banco()

		elif platform.system() == 'Windows':
			bd = Banco_dados()
			bd.conectar()
			self.lista_decks = bd.listar_decks(self.usuario)
			bd.fechar_banco()

		var = int()

		fram=tkinter.Frame(self.janela_estudo)
		fram.pack(anchor=tkinter.NW)

		frameS=tkinter.Frame(fram,width=170,height=210)
		frameS.pack(side=tkinter.LEFT)

		self.listbox = tkinter.Listbox(frameS)
		self.listbox.pack()
		self.selecionar_deck()

		self.btOP=tkinter.Button(frameS,text="Selecionar",command=self.item_selecionado_deck)
		self.btOP.pack(expand=1,fill=tkinter.BOTH)


		self.frOpcao=tkinter.Frame(fram,width=170,height=210)
		self.frDeck=tkinter.LabelFrame(self.frOpcao,text="Deck Selecionado")
		#self.lbD=tkinter.Label(self.frDeck,text="", font=("Arial","8","bold"))
		#self.lbD.pack()
		self.lbd1=tkinter.Label(self.frDeck,text="Nenhum deck selecionado",font=("Arial","8","bold"))
		self.lbd1.pack()
		self.frDeck.pack(anchor=tkinter.NW)

		var=int()
		labSelect=tkinter.LabelFrame(self.frOpcao,text="Selecione o modo")
		labSelect.pack()
		rb1 = tkinter.Radiobutton(labSelect, text='Padrão', variable=var , value=1,command=self.selecionar_modo_1 )
		rb1.pack(anchor=tkinter.NW)
		#rb1.select()
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
		self.frOpcao.pack()
		self.btOPen.pack(side=tkinter.BOTTOM)

		self.janela_estudo.mainloop()
	 
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
		for i in range(0, len(self.lista_decks)):
			self.listbox.insert(i, self.lista_decks[i])

	def item_selecionado_deck(self):
		try:
			
			item_selecionado_listbox = self.listbox.curselection()
			self.item_selecionado_listbox = self.listbox.get(item_selecionado_listbox[0])

			bd = Banco_dados()
			bd.conectar()
			codigo = bd.puxar_codigo_deck(self.item_selecionado_listbox)
			deck = bd.puxar_deck(codigo)
			self.n_deck = len(deck.keys()) 
			self.lbd1['text'] = 'Nome: ' + self.item_selecionado_listbox + '\n' + 'Cards: ' + str(self.n_deck)

		except(IndexError):
			messagebox.showerror('Erro','Nenhum deck foi selecionado')
		
	def iniciar(self):
		try:
			if self.modo == 'padrão':
				if self.n_deck == 0:
					raise IndexError('sem cards')
				self.janela_estudo.destroy()
				fc = Flash_Card(self.item_selecionado_listbox,self.modo)
				deck_estudo = Estudar(self.usuario)
			elif self.modo == 'numero de cards':
				if self.n_deck == 0:
					raise IndexError('sem cards')
				self.numero_cards = int(self.entN.get())
				self.janela_estudo.destroy()
				fc = Flash_Card(self.item_selecionado_listbox, self.modo, self.numero_cards)
				deck_estudo = Estudar(self.usuario)
			elif self.item_selecionado_listbox == '':
				pass
			elif self.modo ==  '':
				messagebox.showerror('Erro', 'Nenhum modo selecionado')
		except (AttributeError):
			messagebox.showerror('Erro','Nenhum baralho foi selecionado')
		except (IndexError):
			messagebox.showerror('Erro', 'Não há nenhum card no baralho')

	def fechar_toplevel(self, toplevel):
		toplevel.destroy()
		self.bt1['state'] = tkinter.NORMAL
		self.bt2['state'] = tkinter.NORMAL

	def fechar_janela(self, janela):
		self.valor = False
		janela.destroy()


if __name__ == '__main__':
	app = Estudar()


