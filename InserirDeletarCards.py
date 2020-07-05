import tkinter
from tkinter import messagebox
from Banco_armazenamento.Banco_dados import Banco_dados
from Deck import Deck
import sys

class Editar_cartoes:
	def __init__(self, nome_deck):
		self.janela = tkinter.Tk()
		self.janela.title('Configurações de card')
		self.janela.geometry('400x200+100+100')
		self.janela.resizable(0,0)

		# Chama da classe controladora de dados 
		self.control = Deck()
		self.control.deck = nome_deck

		# Chamada de banco de dados 
		self.bd = Banco_dados(self.control.deck)
		self.bd.conectar()
		self.codigo_deck = self.bd.puxar_codigo_deck(nome_deck)

		# Frame de organição dos botoes
		self.btf = tkinter.Frame(self.janela)
		self.btf.pack(side=tkinter.LEFT)
		
		# label do frente
		self.lb1 = tkinter.Label(self.janela, text='Frente:')
		self.lb1.place(x=18,y=58)

		# label do verso
		self.lb2 = tkinter.Label(self.janela, text='Verso:')
		self.lb2.place(x=20,y=123)

		self.lb3 =tkinter. Label(self.janela, text='Código:')
		self.lb3.place(x=70,y=12)

		# Entrada do frente
		self.ent1 = tkinter.Text(self.janela, width = 22, height=3)
		self.ent1.place(x=70,y=38)
		
		# Entrada de verso
		self.ent2 = tkinter.Text(self.janela, width=22, height = 3)
		self.ent2.place(x=70, y=108)

		self.ent3 = tkinter.Entry(self.janela, width=5)
		self.ent3.place(x=130,y=10)
		
		# Botão de adicionar card
		self.bt1 = tkinter.Button(self.janela, text='Adicionar', command=self.adicionar, width=7)
		self.bt1.place(x=290,y=60)
		
		self.bt2 = tkinter.Button(self.janela, text='Alterar', command=self.alterar, width=7)
		self.bt2.place(x=290,y=100)

		# Botão de remover card
		self.bt3 = tkinter.Button(self.janela, text='Remover', command=self.remover, width=7)
		self.bt3.place(x=290,y=140)

		# Botão de aviso sobre como remover cards
		self.bt4 = tkinter.Button(self.janela, text='*', width=1, bd=0,	 command=self.adendo)
		self.bt4.place(x=373,y=142)

		# Botão que pesquisa cards
		self.bt5 = tkinter.Button(self.janela, text='Pesquisar', command=self.puxar, width=7)
		self.bt5.place(x=290, y=20)

		# Botão que mostra cards existentes em determinado deck
		self.bt6 = tkinter.Button(self.janela, text='Mostrar cards', command=self.mostrar_deck, bd=0)
		self.bt6.place(x=20, y=170)

		self.bt7 = tkinter.Button(self.janela, text='limpar', command=self.limpar_entries, bd=0)
		self.bt7.pack(side=tkinter.BOTTOM)

		self.janela.mainloop()

	# método que puxa valores, dada a frente do card
	def puxar(self):
		c = self.ent3.get()
		try:
			self.control.codigo = c
			codigo,frente, verso = self.bd.puxar_card(self.control.codigo)
			
			if self.ent1.get(1.0,tkinter.END) != '' or  self.ent2.get(1.0, END) != '':
				self.limpar_entries()

			self.ent1.insert(1.0, frente)
			self.ent2.insert(1.0, verso)
			self.ent3.insert(0, codigo)
		except (TypeError):
			messagebox.showerror('Botão: Pesquisar', 'ERRO: o código não corresponde, possiveis erros:\n1- verifique se o valor é um número\n2- verifique se a caixa não está vazia\n3- verifique se o codigo existe.')


	# método adicionador de cards
	def adicionar(self):
		try:
			if self.control.frente == '' or self.control.verso == '':
				raise Exception('Vazio')
			
			self.fechar_toplevel()
			
			f = self.ent1.get(1.0, tkinter.END)	
			v = self.ent2.get(1.0, tkinter.END)
			self.control.frente = f
			self.control.verso = v
			#print(f,v) # TESTE
			
			self.bd.inserir_card(self.control.frente, self.control.verso, self.codigo_deck)
			self.mostrar_deck()
			self.limpar_entries()
			#print('Sucesso') # TESTE
		except (AttributeError):
			f = self.ent1.get(1.0, tkinter.END)	
			v = self.ent2.get(1.0, tkinter.END)
			self.control.frente = f
			self.control.verso = v
			#print(f,v) # TESTE
			self.bd.inserir_card(self.control.frente, self.control.verso, self.codigo_deck)
			self.limpar_entries()
			#print('Sucesso') # TESTE
		except (Exception):
			messagebox.showerror('Botão: Adicionar','ERRO: Frente ou verso estão vazios')

	# método removedor de cards
	def remover(self):
		try:
			c = self.ent3.get()	
			self.control.codigo = c
			self.bd.deletar_card(self.control.codigo)
			self.fechar_toplevel()
			self.mostrar_deck()
			self.limpar_entries()
			#print('Sucesso') # TESTE
		except (TypeError):
			messagebox.showerror('Botão: Remover', 'ERRO: o código não corresponde, possiveis erros:\n1- verifique se o valor é um número\n2- verifique se a caixa não está vazia\n3- verifique se o codigo existe.')
		except (AttributeError):
			c = self.ent3.get()	
			self.control.codigo = c
			self.bd.deletar_card(self.control.codigo)
			self.limpar_entries()
			#print('Sucesso') # TESTE


	# método alterador de cards
	def alterar(self):
		try:	
			f = self.ent1.get(1.0, tkinter.END)
			v = self.ent2.get(1.0, tkinter.END)
			c = self.ent3.get()
			self.control.frente = f
			self.control.verso = v
			self.control.codigo = c
			if self.control.frente == '' or self.control.verso == '':
				raise Exception('Vazio')
			self.bd.alterar_card(self.control.codigo, self.control.frente, self.control.verso)
			self.fechar_toplevel()
			self.mostrar_deck()
			self.limpar_entries()
			#print('Sucesso') # TESTE
		except (TypeError):
			messagebox.showerror('Botão: Alterar', 'ERRO: o código não corresponde, possiveis erros:\n1- verifique se o valor é um número\n2- verifique se a caixa não está vazia\n3- verifique se o codigo existe.')
		except (AttributeError):
			f = self.ent1.get(1.0, tkinter.END)
			v = self.ent2.get(1.0, tkinter.END)
			c = self.ent3.get()
			self.control.frente = f
			self.control.verso = v
			self.control.codigo = c
			self.bd.alterar_card(self.control.codigo, self.control.frente, self.control.verso)
			self.limpar_entries()
			#print('Sucesso') # TESTE
		except (Exception):
			messagebox.showerror('Botão: Alterar','ERRO: Frente ou verso estão vazios')


		
	# método de aviso sobre remoção de cards
	def adendo(self):
		tkinter.messagebox.showinfo('Adendo', '*Para remover ou pesquisar um card, insira somente o codigo do mesmo*')

	def limpar_entries(self):
		self.ent1.delete(1.0, tkinter.END)
		self.ent2.delete(1.0, tkinter.END)
		self.ent3.delete(0,tkinter.END)
 	
	def mostrar_deck(self):
		self.janela.geometry('400x200+500+500')
		self.toplevel = tkinter.Toplevel(self.janela)
		self.toplevel.protocol('WM_DELETE_WINDOW', self.fechar_toplevel) # Reescreve o método de fechar janela (x)
		self.toplevel.minsize(400,300)
		self.toplevel.maxsize(400,300)
		self.bt6['state'] = tkinter.DISABLED	

		self.listbox = tkinter.Listbox(self.toplevel, font='-size 10', width=40, height=30, bd=0)
		self.listbox.bind('<Button-1>', self.card_selecionado)
		self.listbox.pack()
		
		try:
			deck = self.bd.puxar_deck(self.codigo_deck)
			deck_keys = list(deck.keys())
			print(deck)

			i = 0
			i_2 = 1
			for chave, valor in deck.items():
				cod = self.bd.puxar_codigo_card(deck_keys[i])
				a = str(i) + ' ' + str(deck_keys[i])+':'+ str(deck[chave])	
				self.listbox.insert(i, a)
				i_2 += 1
				i += 1
		except:
			self.listbox.insert(1,'ERRO: Não é possível exibir')

	def fechar_toplevel(self):
		self.toplevel.destroy()
		self.janela.geometry('400x200+100+100')
		del self.toplevel
		self.bt6['state'] = tkinter.NORMAL


	def card_selecionado(self, *args):
		self.janela.geometry('400x200+100+100')
		self.limpar_entries()
		card_codigo = self.listbox.curselection()
		card = self.listbox.get(card_codigo[0])
		card = card.replace(card[0],'')
		card = card.replace(card[0],'')
		for i in range(len(card)):
			if card[i] == ':':
				i_2 = i + 1
				frente = card[:i]
				verso = card[i_2:]
				print(frente, verso)
				self.ent1.insert(1.0, frente)
				self.ent2.insert(1.0, verso)
		print(card_codigo)


		
if __name__ == '__main__':
	idc = IDC('teste')
