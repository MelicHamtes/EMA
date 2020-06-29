from tkinter import *
from Banco_armazenamento.Banco_dados import Banco_dados

class Tabela_deck:
	def __init__(self, deck=None):
		self.janela_2 = Tk()
		self.janela_2.geometry('400x400')
		self.listb = Listbox(self.janela_2, font='-size 10', width=40, height=30, bd=0)
		self.listb.pack()
		# Mudar conexão para banco de dados conzisente com a escolha do usuario
		# deck =None irá aqui-.
		self.bd = Banco_dados('teste')

		self.deck = self.bd.puxar_deck()
		self.deck_keys = list(self.deck.keys())

		self.puxar_deck()
		self.janela_2.mainloop()

	def puxar_deck(self):
		self.i = 0
		self.i_2 = 1
		for chave, valor in self.deck.items():
			cod = self.bd.puxar_codigo(self.deck_keys[self.i])
			a = str(cod) + '- ' + str(self.deck_keys[self.i])+':'+ str(self.deck[chave])
			self.listb.insert(self.i_2, a)
			self.i_2 += 1
			self.i += 1
