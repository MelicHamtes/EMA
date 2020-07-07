import tkinter
from tkinter import messagebox
from Banco_armazenamento.Banco_dados import Banco_dados
from Deck import Deck
import sys

class Editar_cartoes:
	def __init__(self, nome_deck):
		self.janela = tkinter.Tk()
		self.janela.title('Configurações de card')
		self.janela.geometry("460x190+350+150")
		self.janela.resizable(0,0)

		# Chama da classe controladora de dados 
		self.control = Deck()
		self.control.deck = nome_deck

		fram=tkinter.Frame(self.janela)
		fr=tkinter.Frame(fram)
		frameF=tkinter.LabelFrame(fr)
		lb1 = tkinter.Label(frameF, text='Frente:')
		lb1.pack(side=tkinter.LEFT)
		self.ent1 = tkinter.Text(frameF, width = 30, height=4)
		self.ent1.pack()
		frameF.pack()

		frameV= tkinter.LabelFrame(fr)
		lb2 =tkinter.Label(frameV, text='Verso: ')
		lb2.pack(side=tkinter.LEFT)
		self.ent2 =tkinter.Text(frameV, width=30, height = 4)
		self.ent2.pack()
		frameV.pack()

		framebt=tkinter.LabelFrame(fr)
		self.btM=tkinter.Button(framebt,text="Mostar Cards",width=10,height=1, command=self.mostrar_deck)
		self.btM.pack(side=tkinter.LEFT)
		btL=tkinter.Button(framebt,text="Limpar",width=10,height=1, command=self.limpar_entries)
		btL.pack(side=tkinter.RIGHT)
		framebt.pack(expand=1,fill=tkinter.BOTH)
		fr.pack(side=tkinter.LEFT)


		frameBot=tkinter.LabelFrame(fram,text="Cardº")
		lbS=tkinter.Label(frameBot,text="aqui ficara o card selecionado",font=("Arial","7","bold"))
		lbS.pack(side=tkinter.TOP,anchor=tkinter.NW,expand=1,fill=tkinter.BOTH)


		btADIC=tkinter.Button(frameBot,text="Adicionar", command=self.adicionar)
		btADIC.pack(side=tkinter.BOTTOM,expand=1,fill=tkinter.BOTH)

		btDelet=tkinter.Button(frameBot,text="Deletar", command=self.remover)
		btDelet.pack(side=tkinter.BOTTOM,expand=1,fill=tkinter.BOTH)

		btALt=tkinter.Button(frameBot,text="Alterar",command=self.alterar)
		btALt.pack(side=tkinter.BOTTOM,expand=1,fill=tkinter.BOTH)

		frameBot.pack(side=tkinter.RIGHT,anchor=tkinter.N)
		fram.pack(anchor=tkinter.CENTER)
		
		self.janela.mainloop()

	# método que puxa valores, dada a frente do card
	'''
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
	'''
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
			f = self.ent1.get(1.0, tkinter.END)
			self.control.frente = f
			c = self.bd.puxar_codigo_card(self.control.frente)
			self.bd.deletar_card(c)
			self.fechar_toplevel()
			self.mostrar_deck()
			self.limpar_entries()
			#print('Sucesso') # TESTE
		except (TypeError):
			messagebox.showerror('Botão: Remover', 'ERRO: o código não corresponde, possiveis erros:\n1- verifique se o valor é um número\n2- verifique se a caixa não está vazia\n3- verifique se o codigo existe.')
		except (AttributeError):
			f = self.ent1.get(1.0, tkinter.END)
			c = self.bd.puxar_codigo_card(self.control.frente)
			self.bd.deletar_card(c)
			self.limpar_entries()
			#print('Sucesso') # TESTE


	# método alterador de cards
	def alterar(self):
		#try:	
		f = self.ent1.get(1.0, tkinter.END)
		v = self.ent2.get(1.0, tkinter.END)
		self.control.frente = f
		self.control.verso = v
		#self.control.codigo = c
		c = self.bd.puxar_codigo_card(self.frente_deck)
		print(c)
		if self.control.frente == '' or self.control.verso == '':
			raise Exception('Vazio')
		self.bd.alterar_card(self.control.codigo, self.control.frente, self.control.verso)
		self.fechar_toplevel()
		self.mostrar_deck()
		self.limpar_entries()
			#print('Sucesso') # TESTE
		#except (TypeError):
			#messagebox.showerror('Botão: Alterar', 'ERRO: o código não corresponde, possiveis erros:\n1- verifique se o valor é um número\n2- verifique se a caixa não está vazia\n3- verifique se o codigo existe.')
		#except (AttributeError):
		f = self.ent1.get(1.0, tkinter.END)
		v = self.ent2.get(1.0, tkinter.END)
		self.control.frente = f
		self.control.verso = v
		c = self.bd.puxar_codigo_card(self.frente_deck)
		print(c)
		self.bd.alterar_card(c, self.control.frente, self.control.verso)
		self.fechar_toplevel()
		self.mostrar_deck()
		self.limpar_entries()
		#print('Sucesso') # TESTE
		#except (Exception):
			#messagebox.showerror('Botão: Alterar','ERRO: Frente ou verso estão vazios')


		
	# método de aviso sobre remoção de cards
	def adendo(self):
		tkinter.messagebox.showinfo('Adendo', '*Para remover ou pesquisar um card, insira somente o codigo do mesmo*')

	def limpar_entries(self):
		self.ent1.delete(1.0, tkinter.END)
		self.ent2.delete(1.0, tkinter.END)
		#self.ent3.delete(0,tkinter.END)
 	
	def mostrar_deck(self):
		self.janela.geometry('400x200+500+500')
		self.toplevel = tkinter.Toplevel(self.janela)
		self.toplevel.protocol('WM_DELETE_WINDOW', self.fechar_toplevel) # Reescreve o método de fechar janela (x)
		self.toplevel.minsize(400,300)
		self.toplevel.maxsize(400,300)
		self.btM['state'] = tkinter.DISABLED	

		# Chamada de banco de dados 
		self.bd = Banco_dados(self.control.deck)
		self.bd.conectar()
		self.codigo_deck = self.bd.puxar_codigo_deck(self.control.deck)


		self.listbox = tkinter.Listbox(self.toplevel, font='-size 10', width=40, height=30, bd=0)
		self.listbox.bind('<Button-1>', self.card_selecionado)
		self.listbox.pack()
		
		try:
			self.deck = self.bd.puxar_deck(self.codigo_deck)
			print(self.deck)
			deck_keys = list(self.deck.keys())
			i = 0
			i_2 = 1
			for chave, valor in self.deck.items():
				cod = self.bd.puxar_codigo_card(deck_keys[i])
				a = str(i) + ' ' + str(deck_keys[i])+':'+ str(self.deck[chave])	
				self.listbox.insert(i, a)
				i_2 += 1
				i += 1
		except:
			self.listbox.insert(1,'ERRO: Não é possível exibir')

	def fechar_toplevel(self):
		self.toplevel.destroy()
		self.janela.geometry('400x200+100+100')
		del self.toplevel
		self.btM['state'] = tkinter.NORMAL
		self.deck = self.bd.puxar_deck(self.codigo_deck)

	def card_selecionado(self, *args):
		self.janela.geometry('400x200+100+100')
		self.limpar_entries()
		card_codigo = self.listbox.curselection()
		card = self.listbox.get(card_codigo[0])
		self.frente_deck = ''
		card = card.replace(card[0],'')
		card = card.replace(card[0],'')
		for i in range(len(card)):
			if card[i] == ':':
				i_2 = i + 1
				frente = card[:i]
				verso = card[i_2:]
				self.frente_deck = self.frente_deck.replace(card[i_2:],'')
				print(frente, verso)
				self.ent1.insert(1.0, frente)
				self.ent2.insert(1.0, verso)
		print(card_codigo)
		self.fechar_toplevel()
		self.mostrar_deck()
		
		
if __name__ == '__main__':
	idc = IDC('teste')
