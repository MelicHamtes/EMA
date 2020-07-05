import os
import platform
import tkinter
import sys
from tkinter import messagebox
from Banco_armazenamento.Banco_dados import Banco_dados
from Controlador_acesso import Controlador
from Flash_card import Flash_Card 
from InserirDeletarCards import Editar_cartoes

class Configuracoes_deck:
	def __init__(self):
		self.janela_deck = tkinter.Tk()
		self.janela_deck.title('Decks')
		self.control = Controlador()
		self.janela_deck.geometry('200x100+350+200')
		self.janela_deck.resizable(0,0)
		self.janela_deck.protocol('WM_DELETE_WINDOW', lambda: self.janela_deck.destroy()) 

		if platform.system() == 'Linux':
			self.dir_path = os.path.dirname(os.path.realpath(__file__)) + '/Banco_armazenamento/db/Ema'
			bd = Banco_dados()
			bd.conectar()
			self.lista_decks = bd.listar_decks()
			#self.lista_decks = os.listdir(self.dir_path)
		elif platform.system() == 'Windows':
			self.dir_path = os.path.dirname(os.path.realpath(__file__)) + '\\Banco_armazenamento\\db\\Ema'
			bd = Banco_dados()
			bd.conectar()
			self.lista_decks = bd.listar_decks()
		    #self.lista_decks = os.listdir(self.dir_path)

		#print(self.lista_decks, type(self.lista_decks)) #Teste
		self.frame = tkinter.Frame(self.janela_deck)
		self.frame.pack()
		self.mb =  tkinter.Menubutton ( self.frame, text = "Deck", relief = tkinter.RAISED )
		self.mb.pack(side=tkinter.LEFT)
		self.mb.menu  =  tkinter.Menu ( self.mb, tearoff = 0 )
		self.mb["menu"]  =  self.mb.menu

		self.mb.menu.add_command(label='Criar Deck', command=self.janela_adicionar_decks)
		#self.bt1.place(x=20,y=10)

		self.bt2 = tkinter.Button(self.frame, text='Abrir Deck', command=self.janela_abrir_decks)
		#self.bt2.place(x=20,y=55)
		self.bt2.pack(side=tkinter.LEFT)
		self.mb.menu.add_command(label='Editar cards', command=self.janela_editar_decks)
		#self.bt3.place(x=97,y=10)

		self.mb.menu.add_command(label='Deletar deck', command=self.janela_deletar_decks)
		#self.bt4.place(x=95,y=55)

		#self.bt5 = tkinter.Button(self.janela_deck, text='<--', command=self.retornar, bd=0)
		#self.bt5.place(x=0,y=0)
		self.mb.pack()
		self.janela_deck.mainloop()

	#def retornar(self):
	#	self.janela_deck.destroy()
	
	# Fecha janela principal (esta classe) e em seguia a abre novamente para atualização dos banco de dados 	
	def atualizar(self):
		self.janela_deck.destroy()
		deck = Configuracoes_deck() 

	# Janela de toplevel com entrada para adicionar um deck (banco de dados)
	def janela_adicionar_decks(self):
		self.bloquear_botoes()
		self.toplevel_1 = tkinter.Toplevel(self.janela_deck)
		self.toplevel_1.protocol('WM_DELETE_WINDOW', lambda: self.fechar_toplevel(self.toplevel_1)) 
		self.toplevel_1.minsize(300,50)
		self.toplevel_1.maxsize(300,50)
		self.toplevel_1.title('Criar deck')

		lb2 = tkinter.Label(self.toplevel_1, text='Nome:')
		lb2.pack(side=tkinter.LEFT)
		self.ent2 = tkinter.Entry(self.toplevel_1)
		self.ent2.pack(side=tkinter.LEFT)
		bt = tkinter.Button(self.toplevel_1, text='Adicionar', command=self.adicionar_decks)
		bt.pack(side=tkinter.RIGHT)

	# Janela de toplevel para selecionar deck (banco de dados) e abrir janela na qual os cards serão estudados (exbidos)
	def janela_abrir_decks(self):
		"""
		self.bloquear_botoes()
		self.toplevel_2 = tkinter.Toplevel(self.janela_deck)
		self.toplevel_2.protocol('WM_DELETE_WINDOW', self.fechar_toplevel_2) 
		self.toplevel_2.minsize(170,210)
		self.toplevel_2.maxsize(170,210)
		self.toplevel_2.title('Decks')
		self.listbox_1 = tkinter.Listbox(self.toplevel_2, font='-size 10', width=24, height=10, bd=0)
		self.listbox_1.pack()

		for i in range(0, len(self.lista_decks)):
			self.listbox_1.insert(i, self.lista_decks[i])

		bt = tkinter.Button(self.toplevel_2, text='Selecionar', command=self.item_selecionado_estudar)
		bt.pack(side=tkinter.BOTTOM)
		"""
		self.bt2['state'] = tkinter.DISABLED
		self.janela_deck.destroy()
		deck_estudo = Estudar()
		jd = Configuracoes_deck()
	
	# Janela de toplevel para selecionar deck (banco de dados) e abrir janela na qual os cards serão modificados
	def janela_editar_decks(self):
		self.bloquear_botoes()
		self.toplevel_3 = tkinter.Toplevel(self.janela_deck)
		self.toplevel_3.protocol('WM_DELETE_WINDOW', lambda: self.fechar_toplevel(self.toplevel_3)) 
		self.toplevel_3.minsize(170,210)
		self.toplevel_3.maxsize(170,210)
		self.toplevel_3.title('Decks')
		self.listbox_2 = tkinter.Listbox(self.toplevel_3, font='-size 10', width=24, height=10, bd=0)
		self.listbox_2.pack()

		for i in range(0, len(self.lista_decks)):
			self.listbox_2.insert(i, self.lista_decks[i])

		bt = tkinter.Button(self.toplevel_3, text='Selecionar', command=self.item_selecionado_editar)
		bt.pack(side=tkinter.BOTTOM)

	def janela_deletar_decks(self):
		self.bloquear_botoes()
		self.toplevel_4 = tkinter.Toplevel(self.janela_deck)
		self.toplevel_4.protocol('WM_DELETE_WINDOW', lambda: self.fechar_toplevel(self.toplevel_4)) 
		self.toplevel_4.minsize(170,210)
		self.toplevel_4.maxsize(170,210)
		self.toplevel_4.title('Decks')
		self.listbox_3 = tkinter.Listbox(self.toplevel_4, font='-size 10', width=24, height=10, bd=0)
		self.listbox_3.pack()

		for i in range(0, len(self.lista_decks)):
			self.listbox_3.insert(i, self.lista_decks[i])

		bt = tkinter.Button(self.toplevel_4, text='Selecionar', command=self.item_selecionado_excluir)
		bt.pack(side=tkinter.BOTTOM)


	# Faz ligação ao banco de dados e adiciona um deck (banco de dados)
	def adicionar_decks(self):
		try:
			nome_deck = self.ent2.get()
			print(nome_deck)
			self.control.deck = nome_deck
			print(self.control.deck)
			# Fazer ligação ao banco de dados
			bd = Banco_dados()
			if self.control.deck == None:
				raise Exception('Vazio') 
			bd.conectar()
			bd.inserir_deck(self.control.deck)
			self.atualizar()
			bd.fechar_banco()
		except (Exception):
			messagebox.showerror('Erro','Nada foi escrito')

	def fechar_toplevel(self, toplevel):
		toplevel.destroy()
		self.mb['state'] = tkinter.NORMAL
		#self.bt1['state'] = tkinter.NORMAL
		self.bt2['state'] = tkinter.NORMAL
		#self.bt3['state'] = tkinter.NORMAL
		#self.bt4['state'] = tkinter.NORMAL

	# Item selecionado irá abrir a janela de estudo
	"""
	def item_selecionado_estudar(self):
		item_selecionado_listbox = self.listbox_1.curselection()
		item_selecionado_listbox = self.listbox_1.get(item_selecionado_listbox[0])
		self.fechar_toplevel(self.toplevel_2)
		flash_card = Flash_Card(item_selecionado_listbox)
	"""
	# Item selecionado irá abrir a janela de edição de cards
	def item_selecionado_editar(self):
		try:
			item_selecionado_listbox = self.listbox_2.curselection()
			item_selecionado_listbox = self.listbox_2.get(item_selecionado_listbox[0])
			self.fechar_toplevel(self.toplevel_3)
			self.janela_deck.destroy()
			idc = Editar_cartoes(item_selecionado_listbox)
			jd = Configuracoes_deck()
		except(IndexError):
			messagebox.showerror('Erro', 'Nenhum deck foi selecionado')

	def item_selecionado_excluir(self):
		try:
			item_selecionado_listbox = self.listbox_3.curselection()
			item_selecionado_listbox = self.listbox_3.get(item_selecionado_listbox[0])
			path_remove = self.dir_path + item_selecionado_listbox
			bd = Banco_dados()
			bd.conectar()
			bd.deletar_deck(item_selecionado_listbox)
			bd.fechar_banco()
			self.atualizar()
		except(IndexError):
			messagebox.showerror('Erro','Nenhum deck foi selecionado')

	def bloquear_botoes(self):
		self.mb['state'] = tkinter.DISABLED
		#self.bt1['state'] = tkinter.DISABLED
		self.bt2['state'] = tkinter.DISABLED
		#self.bt3['state'] = tkinter.DISABLED
		#self.bt4['state'] = tkinter.DISABLED	

	def fechar_janela(self, janela):
		self.valor = False
		janela.destroy()

"""
Classe será chamada sempre que se quiser abrir os cards para estudo; classe no botão do MENU_ESTUDAR
e ABRIR em CONF. CARDS
"""
class Estudar:
	def __init__(self):
		self.janela_estudo = tkinter.Tk()
		self.janela_estudo.geometry('300x200')
		self.janela_estudo.resizable(0,0)
		self.janela_estudo.title('Estudar')
		self.janela_estudo.protocol('WM_DELETE_WINDOW', lambda: self.fechar_janela(self.janela_estudo))

		self.modo = ''
		self.numero_cards = 0

		if platform.system() == 'Linux':
			self.dir_path = os.path.dirname(os.path.realpath(__file__)) + '/Banco_armazenamento/db/Ema'
			bd = Banco_dados()
			bd.conectar()
			self.lista_decks = bd.listar_decks()
		elif platform.system() == 'Windows':
			self.dir_path = os.path.dirname(os.path.realpath(__file__)) + '\\Banco_armazenamento\\db\\Ema'
			bd = Banco_dados()
			bd.conectar()
			self.lista_decks = bd.listar_decks()

		var = int()
		self.lb1 = tkinter.Label(self.janela_estudo, text='Selecione o modo:', font='Arial, 10')
		self.lb1.place(x=0,y=0)

		self.rb1 = tkinter.Radiobutton(self.janela_estudo, text='Padrão', variable=var , value=1, command= self.selecionar_modo_1)
		self.rb1.place(y=20)
		self.rb2 = tkinter.Radiobutton(self.janela_estudo, text='Especificar número de cartões', variable=var, value=2,command=self.selecionar_modo_2)
		self.rb2.place(y=40)

		self.lb2 = tkinter.Label(self.janela_estudo, text='Selecione o deck:', font='Arial, 10')
		self.lb2.place(y=100)

		self.bt1 = tkinter.Button(self.janela_estudo, text='Selecionar', command=self.selecionar_deck)
		self.bt1.place(y=120)

		self.bt2 = tkinter.Button(self.janela_estudo, text='Iniciar', command=self.iniciar)

		self.lb3 = tkinter.Label(self.janela_estudo, font='Arial, 9')
		self.janela_estudo.mainloop()

	def selecionar_modo_1(self):
		self.modo = 'padrão'

	def selecionar_modo_2(self):
		self.modo = 'numero de cards'
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
		self.numero_cards = int(self.ent_modo_2.get())
		self.fechar_toplevel(self.toplevel_modo_2)

	def selecionar_deck(self):
		self.bt1['state'] = tkinter.DISABLED
		self.bt2['state'] = tkinter.DISABLED
		self.toplevel_selecionar = tkinter.Toplevel(self.janela_estudo)
		self.toplevel_selecionar.protocol('WM_DELETE_WINDOW', lambda: self.fechar_toplevel(self.toplevel_selecionar)) 
		self.toplevel_selecionar.minsize(170,210)
		self.toplevel_selecionar.maxsize(170,210)
		self.toplevel_selecionar.title('Decks')
		self.listbox = tkinter.Listbox(self.toplevel_selecionar, font='-size 10', width=24, height=10, bd=0)
		self.listbox.pack()

		for i in range(0, len(self.lista_decks)):
			self.listbox.insert(i, self.lista_decks[i])

		bt = tkinter.Button(self.toplevel_selecionar, text='Selecionar', command=self.item_selecionado_deck)
		bt.pack(side=tkinter.BOTTOM)


	def item_selecionado_deck(self):
		try:
			item_selecionado_listbox = self.listbox.curselection()
			self.item_selecionado_listbox = self.listbox.get(item_selecionado_listbox[0])

			self.lb3['text'] = 'Deck selecionado: ' + self.item_selecionado_listbox
			self.lb3.place(y=120)
			self.bt2.place(x=180, y=120)
			self.bt1['text'] = 'Trocar'
			self.bt1.place(x=180, y=150)
			self.fechar_toplevel(self.toplevel_selecionar)
		except(IndexError):
			messagebox.showerror('Erro','Nenhum deck foi selecionado')
		

	def iniciar(self):
		if self.modo == 'padrão':
			self.janela_estudo.destroy()
			fc = Flash_Card(self.item_selecionado_listbox,self.modo)
			deck_estudo = Estudar()
		elif self.modo == 'numero de cards':
			self.janela_estudo.destroy()
			fc = Flash_Card(self.item_selecionado_listbox, self.modo, self.numero_cards)
			deck_estudo = Estudar()

	def fechar_toplevel(self, toplevel):
		toplevel.destroy()
		self.bt1['state'] = tkinter.NORMAL
		self.bt2['state'] = tkinter.NORMAL

	def fechar_janela(self, janela):
		self.valor = False
		janela.destroy()


if __name__ ==  '__main__':
	dc = Deck()
	#dc2 = Deck_Estudo()


