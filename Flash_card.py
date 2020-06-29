import tkinter
from random import choice
from Banco_armazenamento.Banco_dados import Banco_dados
import sys 

"""
# Dicionário padrão

conjunto_padrão = {
	'1':'informção numero_1',
	'2':'informção numero_2',
	'3':'informção numero_3',
	'4':'informção numero_4',
	'5':'informção numero_5',
	'6':'informção numero_6',
	'7':'informção numero_7',
	'8':'informção numero_8',
	'9':'informção numero_9',
	'10':'informção numero_10',
}
"""

class Flash_Card():
	def __init__(self, nome_conjunto, modo, n_cards=None):
		self.janela = tkinter.Tk()
		self.janela.title('teste_EMA')
		self.janela.geometry('400x300')
		self.janela.resizable(0,0)
		self.bd = Banco_dados(nome_conjunto)
		self.bd.conectar()
		self.numero_deck = self.bd.puxar_codigo_deck(nome_conjunto)
		self.conjunto_padrão = self.bd.puxar_deck(self.numero_deck)

		self.lb1= tkinter.Label(self.janela)
		self.lb1.pack(side=tkinter.TOP)
		self.lb2 = tkinter.Label(self.janela)
		self.lb2.place(x=130, y=130)
		self.bt1 = tkinter.Button(self.janela, text='começar', command=self.iniciar)
		self.bt1.place(x=100, y=250)
		self.bt2 = tkinter.Button(self.janela, text='mostrar',command=self.exibir)
		self.bt3 = tkinter.Button(self.janela, text='sair', command=lambda: self.janela.destroy())
		#self.bt3.place(x=00,y=00)
		self.lb3 = tkinter.Label(self.janela)

		if modo == 'padrão':
			self.index_pack = list(self.conjunto_padrão.keys())
		elif modo == 'numero de cards':
			self.index_pack = list(self.conjunto_padrão.keys())
			if len(self.index_pack) < n_cards:
				while len(self.index_pack) < n_cards:
					rand = choice(list(self.conjunto_padrão.keys()))
					self.index_pack.append(rand)
					print(self.index_pack)
			elif len(self.index_pack) > n_cards:
				while len(self.index_pack) > n_cards:
					rand = choice(list(self.conjunto_padrão.keys()))
					self.index_pack.remove(rand)
					print(self.index_pack)
					
		self.janela.mainloop()

	def iniciar(self):
		try:
			self.limpar()	
			self.rd = choice(self.index_pack)		
			
			for i in self.index_pack:	
				if i == self.rd:
					#global n 
					self.n = i
					#self.j = self.n -1
			
			self.lb1['text'] = self.rd
			self.bt1['text'] = 'continue'
			self.bt1['state'] = tkinter.DISABLED
			self.bt2.place(x=220,y=250)		

			print(self.n)
			if self.rd in self.index_pack:
				self.index_pack.remove(self.rd)
				print(self.index_pack)
		except:
			self.limpar()
			self.lb3['text'] = 'Acabou'
			self.lb3.place(x=80,y=130)
			self.bt1['state'] = tkinter.DISABLED
			self.bt2['state'] = tkinter.DISABLED
			self.bt3.place(x=0,y=0)

	def exibir(self):
		self.lb2['text'] = self.conjunto_padrão[self.n]
		self.bt1['state'] = tkinter.ACTIVE
	 
	def limpar(self):
		self.lb1['text'] = ''
		self.lb2['text'] = ''


if __name__ == '__main__':
	janela = Flash_Card()

	