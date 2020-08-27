import tkinter
from tkinter import messagebox
from Banco_armazenamento.Banco_dados import Banco_dados
from Deck import Deck
import sys

class Editar_cartoes:
	def __init__(self, nome_deck):
		self.janela = tkinter.Tk()
		self.janela.title('Configurações de card')
		self.janela.geometry("460x190+850+150")
		self.janela.resizable(0,0)
		self.janela.protocol('WM_DELETE_WINDOW', lambda: self.janela.destroy()) 


		# Chama da classe controladora de dados 
		self.control = Deck()
		self.control.deck = nome_deck
		bd = Banco_dados()
		bd.conectar()
		self.codigo_deck = bd.puxar_codigo_deck(nome_deck)

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

		#self.btM=tkinter.Button(framebt,text="Mostar Cards",width=10,height=1, command=self.mostrar_deck)
		#self.btM.pack(side=tkinter.LEFT)

		btL=tkinter.Button(framebt,text="Limpar",width=10,height=1, command=self.limpar_entries)
		btL.pack(side=tkinter.RIGHT)

		framebt.pack(expand=1,fill=tkinter.BOTH)
		fr.pack(side=tkinter.LEFT)


		frameBot=tkinter.LabelFrame(fram,text="Cartãoº")

		btADIC=tkinter.Button(frameBot,text="Adicionar", command=self.adicionar)
		btADIC.pack(side=tkinter.BOTTOM,expand=1,fill=tkinter.BOTH)

		btDelet=tkinter.Button(frameBot,text="Deletar", command=self.remover)
		btDelet.pack(side=tkinter.BOTTOM,expand=1,fill=tkinter.BOTH)

		btALt=tkinter.Button(frameBot,text="Alterar",command=self.alterar)
		btALt.pack(side=tkinter.BOTTOM,expand=1,fill=tkinter.BOTH)

		frameBot.pack(side=tkinter.RIGHT,anchor=tkinter.N)
		fram.pack(anchor=tkinter.CENTER)
		self.mostrar_deck()
		self.janela.mainloop()

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
			bd = Banco_dados()
			bd.conectar()
			bd.inserir_card(self.control.frente, self.control.verso, self.codigo_deck)
			self.mostrar_deck()
			self.limpar_entries()
			bd.fechar_banco()
			#print('Sucesso') # TESTE
		except (AttributeError):
			self.fechar_toplevel()
			f = self.ent1.get(1.0, tkinter.END)	
			v = self.ent2.get(1.0, tkinter.END)
			self.control.frente = f
			self.control.verso = v
			#print(f,v) # TESTE
			bd = Banco_dados()
			bd.conectar()
			bd.inserir_card(self.control.frente, self.control.verso, self.codigo_deck)
			bd.fechar_banco()
			self.mostrar_deck()
			self.limpar_entries()
			#print('Sucesso') # TESTE
		except (Exception):
			messagebox.showerror('Botão: Adicionar','ERRO: Frente ou verso estão vazios')

	# método removedor de cards
	def remover(self):
		try:
			f = self.ent1.get(1.0, tkinter.END)
			self.control.frente = f
			bd = Banco_dados()
			bd.conectar()
			c = bd.puxar_codigo_card(self.control.frente)
			bd.deletar_card(c)
			self.fechar_toplevel()
			self.mostrar_deck()
			self.limpar_entries()
			bd.fechar_banco()
			#print('Sucesso') # TESTE
		except (TypeError):
			messagebox.showerror('Botão: Remover', 'ERRO: o código não corresponde, possiveis erros:\n1- verifique se o valor é um número\n2- verifique se a caixa não está vazia\n3- verifique se o codigo existe.')
		except (AttributeError):
			self.fechar_toplevel()
			bd = Banco_dados()
			bd.conectar()
			f = self.ent1.get(1.0, tkinter.END)
			c = bd.puxar_codigo_card(self.control.frente)
			bd.deletar_card(c)
			self.limpar_entries()
			bd.fechar_banco()
			self.mostrar_deck()
			#print('Sucesso') # TESTE


	# método alterador de cards
	def alterar(self):
		try:
			f = self.ent1.get(1.0, tkinter.END)
			v = self.ent2.get(1.0, tkinter.END)
			self.control.frente = f
			self.control.verso = v

			if self.control.frente == '' or self.control.verso == '':
				raise Exception('Vazio')

			bd = Banco_dados()
			bd.conectar()
			#self.control.codigo = c
			if self.frente_antigo:
				c = bd.puxar_codigo_card(self.frente_antigo)
				bd.alterar_card(c, self.control.frente, self.control.verso)
			self.fechar_toplevel()
			self.atualizar()
			self.mostrar_deck()
			self.limpar_entries()
			bd.fechar_banco()
			#print('Sucesso') # TESTE
		except (Exception):
			messagebox.showerror('Botão: Alterar', 'ERRO: o código não corresponde, possiveis erros:\n1- verifique se o valor é um número\n2- verifique se a caixa não está vazia\n3- verifique se o codigo existe.')
		except (AttributeError):
			self.fechar_toplevel()
			f = self.ent1.get(1.0, tkinter.END)
			v = self.ent2.get(1.0, tkinter.END)
			self.control.frente = f
			self.control.verso = v
			bd = Banco_dados()
			bd.conectar()
			c = bd.puxar_codigo_card(self.frente_antigo)
			bd.alterar_card(c, self.control.frente, self.control.verso)
			self.mostrar_deck()
			self.limpar_entries()
			bd.fechar_banco()
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
		self.janela.geometry('460x190+550+150')
		self.toplevel = tkinter.Toplevel(self.janela)
		self.toplevel.group(self.janela)
		self.toplevel.protocol('WM_DELETE_WINDOW', lambda: messagebox.showinfo('Não','bobão, não pode fechar')) # Reescreve o método de fechar janela (x)
		self.toplevel.minsize(400,300)
		self.toplevel.maxsize(400,300)
		#self.btM['state'] = tkinter.DISABLED	

		# Chamada de banco de dados 
		self.bd = Banco_dados(self.control.deck)
		self.bd.conectar()
		self.codigo_deck = self.bd.puxar_codigo_deck(self.control.deck)

		self.listbox = tkinter.Listbox(self.toplevel, font='-size 10', width=40, height=30, bd=0)
		self.listbox.bind('<Button-1>', self.card_selecionado)
		self.listbox.pack()
		
		try:
			self.deck = self.bd.puxar_deck(self.codigo_deck)
			deck_keys = list(self.deck.keys())
			i = 0
			i_2 = 1
			for chave, valor in self.deck.items():
				cod = self.bd.puxar_codigo_card(deck_keys[i])
				a = str(deck_keys[i])+':'+ str(self.deck[chave])	
				self.listbox.insert(i, a)
				i_2 += 1
				i += 1
		except:
			self.listbox.insert(1,'ERRO: Não é possível exibir')

	def fechar_toplevel(self):
		self.toplevel.destroy()
		self.janela.geometry('460x190+550+150')
		#self.janela.geometry('400x200+100+100')
		#	self.btM['state'] = tkinter.NORMAL
		self.deck = self.bd.puxar_deck(self.codigo_deck)
		self.frente_antigo = ''

	def card_selecionado(self, *args):
		self.janela.geometry("460x190+350+150")
		self.limpar_entries()
		card_codigo = self.listbox.curselection()
		card = self.listbox.get(card_codigo[0])
		for i in range(len(card)):
			if card[i] == ':':
				i_2 = i + 1
				self.frente_antigo = card[:i]
				self.verso_antigo = card[i_2:]
				self.ent1.insert(1.0, self.frente_antigo)
				self.ent2.insert(1.0, self.verso_antigo)

		self.janela.lift()
		
	def atualizar(self):
		pass
		
if __name__ == '__main__':
	idc = IDC('teste')
