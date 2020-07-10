import os
import platform
import tkinter
import sys
from tkinter import messagebox
from Banco_armazenamento.Banco_dados import Banco_dados
from Deck import Deck 
from InserirDeletarCards import Editar_cartoes
from Estudar import Estudar 

class Configuracoes_deck:
	def __init__(self, usuario=None):
		self.usuario = usuario
		self.janela_configuracoes = tkinter.Tk()
		self.janela_configuracoes.title('Decks')
		self.control = Deck()
		self.janela_configuracoes.resizable(0,0)
		self.janela_configuracoes.geometry('+550+350')
		self.janela_configuracoes.protocol('WM_DELETE_WINDOW', lambda: self.janela_configuracoes.destroy()) 

		if platform.system() == 'Linux':
			self.dir_path = os.path.dirname(os.path.realpath(__file__)) + '/Banco_armazenamento/db/Ema'
			bd = Banco_dados()
			bd.conectar()
			self.lista_decks = bd.listar_decks(self.usuario)
			bd.fechar_banco()

		elif platform.system() == 'Windows':
			self.dir_path = os.path.dirname(os.path.realpath(__file__)) + '\\Banco_armazenamento\\db\\Ema'
			bd = Banco_dados()
			bd.conectar()
			self.lista_decks = bd.listar_decks(self.usuario)
			bd.fechar_banco()

		self.frame = tkinter.Frame(self.janela_configuracoes)
		self.frame.pack(anchor=tkinter.CENTER)
		self.mb =  tkinter.Menubutton ( self.frame, text = "Deck", relief = tkinter.RAISED )
		self.mb.pack(side=tkinter.LEFT)
		self.mb.menu  =  tkinter.Menu ( self.mb, tearoff = 0 )
		self.mb["menu"]  =  self.mb.menu

		self.mb.menu.add_command(label='Criar', command=self.janela_adicionar_decks)

		self.bt2 = tkinter.Button(self.frame, text='Abrir Deck', command=self.janela_abrir_decks)
		self.bt2.pack(side=tkinter.LEFT)
		
		self.mb.menu.add_command(label='Editar cards', command=self.janela_editar_decks)
		self.mb.menu.add_command(label='Deletar', command=self.janela_deletar_decks)
		self.mb.menu.add_command(label='Renomear', command=self.janela_renomear_deck)
		self.mb.pack()

		self.janela_configuracoes.mainloop()

	# Janela de toplevel com entrada para adicionar um deck (banco de dados)
	def janela_adicionar_decks(self):
		#self.bloquear_botoes()
		#self.toplevel_1 = tkinter.Toplevel(self.janela_configuracoes)
		#self.toplevel_1.protocol('WM_DELETE_WINDOW', lambda: self.fechar_toplevel(self.toplevel_1)) 
		#self.toplevel_1.title('Criar deck')
		#self.toplevel_1.lift(self.janela_configuracoes)
		self.teste_criação()
		fram_toplevel_criar = tkinter.Frame(self.janela_configuracoes)
		fram_toplevel_criar.pack()
		lb2 = tkinter.Label(fram_toplevel_criar, text='Nome:')
		lb2.pack(side=tkinter.LEFT)

		self.ent2 = tkinter.Entry(fram_toplevel_criar)
		self.ent2.pack(side=tkinter.LEFT)

		bt = tkinter.Button(fram_toplevel_criar, text='Adicionar', command=self.adicionar_decks)
		bt.pack(side=tkinter.RIGHT)

	def teste_criação(self):
		self.janela_configuracoes.protocol('WM_DELETE_WINDOW', lambda: self.atualizar())
		self.mb.forget()
		self.bt2.forget()
		self.frame.forget()

	# Janela de toplevel para selecionar deck (banco de dados) e abrir janela na qual os cards serão estudados (exbidos)
	def janela_abrir_decks(self):
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

	def janela_renomear_deck(self):
		self.bloquear_botoes()
		self.toplevel_5 = tkinter.Toplevel(self.janela_configuracoes)
		self.toplevel_5.protocol('WM_DELETE_WINDOW', lambda: self.fechar_toplevel(self.toplevel_5)) 
		self.toplevel_5.minsize(170,210)
		self.toplevel_5.maxsize(170,210)
		self.toplevel_5.title('Decks')
		self.listbox_4 = tkinter.Listbox(self.toplevel_5, font='-size 10', width=24, height=10, bd=0)
		self.listbox_4.pack()

		for i in range(0, len(self.lista_decks)):
			self.listbox_4.insert(i, self.lista_decks[i])

		bt = tkinter.Button(self.toplevel_5, text='Selecionar', command=self.item_selecionado_renomear)
		bt.pack(side=tkinter.BOTTOM)
		self.bloquear_botoes()

	# Faz ligação ao banco de dados e adiciona um deck (banco de dados)
	def adicionar_decks(self):
		try:
			nome_deck = self.ent2.get()
			self.control.deck = nome_deck

			if self.verificar_nome_deck(self.control.deck) == False:
				raise TypeError('Deck com o mesmo nome já existente')
			elif self.control.deck == 'Erro: deck está vazio':
				raise Exception('Vazio') 

			bd = Banco_dados()
			bd.conectar()
			bd.inserir_deck(self.control.deck, self.usuario)
			bd.fechar_banco()
			self.atualizar()

		except (TypeError):
			messagebox.showerror('Erro','Já existe um deck com esse nome')
		except (Exception):
			messagebox.showerror('Erro','Nada foi escrito')	


	# Item selecionado irá abrir a janela de estudo
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
			resposta = messagebox.askquestion('Deletar baralho', 'Deseja mesmo deletar?')
			if resposta.lower() == 'no':
				self.atualizar()
			else:
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

	def item_selecionado_renomear(self):
		try:
			item_selecionado_listbox = self.listbox_4.curselection()
			item_selecionado_listbox = self.listbox_4.get(item_selecionado_listbox[0])

			self.fechar_toplevel(self.toplevel_5)
			#self.toplevel_6 = tkinter.Toplevel(self.janela_configuracoes)
			#self.toplevel_6.protocol('WM_DELETE_WINDOW', lambda: self.fechar_toplevel(self.toplevel_6)) 
			#self.toplevel_6.title('Renomear deck')
			self.teste_criação()
			fram_toplevel_renomear = tkinter.Frame(self.janela_configuracoes)
			fram_toplevel_renomear.pack()

			lb2 = tkinter.Label(fram_toplevel_renomear, text='Novo nome:')
			lb2.pack(side=tkinter.LEFT)

			self.ent3 = tkinter.Entry(fram_toplevel_renomear)
			self.ent3.pack(side=tkinter.LEFT)

			bt = tkinter.Button(fram_toplevel_renomear, text='Adicionar', command=lambda:self.item_selecionado_renomear_2(item_selecionado_listbox))
			bt.pack(side=tkinter.RIGHT)

		except(IndexError):
			messagebox.showerror('Erro', 'Nenhum deck foi selecionado')

	def item_selecionado_renomear_2(self, item_selecionado_listbox):
		try:
			resposta = messagebox.askquestion('Renomear baralho', 'Deseja mesmo renomear?')
			if resposta.lower() == 'no':
				self.atualizar()
			else:
				bd = Banco_dados()
				bd.conectar()
				codigo = bd.puxar_codigo_deck(item_selecionado_listbox)
				novo_nome = self.ent3.get()
				self.control.deck = novo_nome
				if self.verificar_nome_deck(self.control.deck) == False:
					raise TypeError('Nome existente')
				elif self.control.deck == 'Erro: deck está vazio':
					raise Exception('Vazio')
				bd.renomear_deck(self.control.deck, codigo)
				bd.fechar_banco()
				self.atualizar()
		except (TypeError):
			messagebox.showerror('Erro','Já existe um deck com esse nome' )
		except (Exception):
			messagebox.showerror('Erro','Deck está vazio')


	def verificar_nome_deck(self, nome_deck):
		bd = Banco_dados()
		bd.conectar()
		nome_decks = bd.listar_decks(self.usuario)
		bd.fechar_banco()

		for i in nome_decks:
			if i == nome_deck:
				return False
		return True

	def bloquear_botoes(self):
		self.mb['state'] = tkinter.DISABLED
		self.bt2['state'] = tkinter.DISABLED

	def fechar_toplevel(self, toplevel):
		toplevel.destroy()
		self.mb['state'] = tkinter.NORMAL
		self.bt2['state'] = tkinter.NORMAL

	def atualizar(self):
		self.janela_configuracoes.destroy()
		deck = Configuracoes_deck(self.usuario) 

if __name__ ==  '__main__':
	dc = Configuracoes_deck()
	#dc2 = Deck_Estudo()


