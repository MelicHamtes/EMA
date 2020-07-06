import os
import platform
import tkinter
import sys
from tkinter import messagebox
from Banco_armazenamento.Banco_dados import Banco_dados
from Deck import Deck
from Flash_card import Flash_Card 
from InserirDeletarCards import Editar_cartoes
from Estudar import Estudar 

class Configuracoes_deck:
	def __init__(self, usuario):
		self.usuario = usuario
		self.janela_configuracoes = tkinter.Tk()
		self.janela_configuracoes.title('Decks')
		self.control = Deck()
		self.janela_configuracoes.geometry('200x100+350+200')
		self.janela_configuracoes.resizable(0,0)
		self.janela_configuracoes.protocol('WM_DELETE_WINDOW', lambda: sys.exit()) 

		if platform.system() == 'Linux':
			self.dir_path = os.path.dirname(os.path.realpath(__file__)) + '/Banco_armazenamento/db/Ema'
			bd = Banco_dados()
			bd.conectar()
			self.lista_decks = bd.listar_decks(self.usuario)
			#self.lista_decks = os.listdir(self.dir_path)
		elif platform.system() == 'Windows':
			self.dir_path = os.path.dirname(os.path.realpath(__file__)) + '\\Banco_armazenamento\\db\\Ema'
			bd = Banco_dados()
			bd.conectar()
			self.lista_decks = bd.listar_decks(self.usuario)
		    #self.lista_decks = os.listdir(self.dir_path)

		#print(self.lista_decks, type(self.lista_decks)) #Teste
		self.frame = tkinter.Frame(self.janela_configuracoes)
		self.frame.pack()
		self.mb =  tkinter.Menubutton ( self.frame, text = "Deck", relief = tkinter.RAISED )
		self.mb.pack(side=tkinter.LEFT)
		self.mb.menu  =  tkinter.Menu ( self.mb, tearoff = 0 )
		self.mb["menu"]  =  self.mb.menu

		self.mb.menu.add_command(label='Criar', command=self.janela_adicionar_decks)
		#self.bt1.place(x=20,y=10)

		self.bt2 = tkinter.Button(self.frame, text='Abrir Deck', command=self.janela_abrir_decks)
		#self.bt2.place(x=20,y=55)
		self.bt2.pack(side=tkinter.LEFT)
		self.mb.menu.add_command(label='Editar cards', command=self.janela_editar_decks)
		#self.bt3.place(x=97,y=10)

		self.mb.menu.add_command(label='Deletar', command=self.janela_deletar_decks)
		self.mb.menu.add_command(label='Renomear')
		#self.bt4.place(x=95,y=55)

		#self.bt5 = tkinter.Button(self.janela_configuracoes, text='<--', command=self.retornar, bd=0)
		#self.bt5.place(x=0,y=0)
		self.mb.pack()

		self.botao_return = tkinter.Button(text='<--', command= lambda: self.fechar_janela(self.janela_configuracoes))
		self.botao_return.pack(side=tkinter.LEFT)
		self.janela_configuracoes.mainloop()

	#def retornar(self):
	#	self.janela_configuracoes.destroy()
	
	# Fecha janela principal (esta classe) e em seguia a abre novamente para atualização dos banco de dados 	
	def atualizar(self):
		self.janela_configuracoes.destroy()
		deck = Configuracoes_deck(self.usuario) 

	# Janela de toplevel com entrada para adicionar um deck (banco de dados)
	def janela_adicionar_decks(self):
		self.bloquear_botoes()
		self.toplevel_1 = tkinter.Toplevel(self.janela_configuracoes)
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
		self.toplevel_2 = tkinter.Toplevel(self.janela_configuracoes)
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
		self.janela_configuracoes.destroy()
		deck_estudo = Estudar(self.usuario)
		config_deck = Configuracoes_deck(self.usuario)
	
	# Janela de toplevel para selecionar deck (banco de dados) e abrir janela na qual os cards serão modificados
	def janela_editar_decks(self):
		self.bloquear_botoes()
		self.toplevel_3 = tkinter.Toplevel(self.janela_configuracoes)
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
		self.toplevel_4 = tkinter.Toplevel(self.janela_configuracoes)
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
			bd.inserir_deck(self.control.deck, self.usuario)
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
			self.janela_configuracoes.destroy()
			idc = Editar_cartoes(item_selecionado_listbox)
			config_deck = Configuracoes_deck(self.usuario)
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



if __name__ ==  '__main__':
	dc = Configuracoes_deck()
	#dc2 = Deck_Estudo()


