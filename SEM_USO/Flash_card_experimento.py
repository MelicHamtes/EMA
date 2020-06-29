from tkinter import *
from random import choice
import sys 
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

class Flash_Card():
	def __init__(self):
		self.janela = Tk()
		self.janela.title('teste_EMA')
		self.janela.geometry('300x300')


		self.lb1= Label(self.janela)
		self.lb1.pack(side=TOP)
		self.lb2 = Label(self.janela)
		self.lb2.place(x=80, y=130)
		self.bt1 = Button(self.janela, text='começar', command=self.iniciar)
		self.bt1.place(x=100, y=250)
		self.bt2 = Button(self.janela, text='mostrar',command=self.exibir)
		self.bt3 = Button(self.janela, text='sair', command=lambda: sys.exit())
		self.bt3.place(x=00,y=00)
		self.lb3 = Label(self.janela)


		self.index_pack = list(conjunto_padrão.keys())

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
			self.bt1['state'] = DISABLED
			self.bt2.place(x=220,y=250)		
			
			for i in self.index_pack:
				if i == self.rd:
					self.index_pack.remove(i)
					print(self.index_pack)
		except:
			self.limpar()
			self.lb3['text'] = 'Acabou'
			self.lb3.place(x=80,y=130)
			self.bt1['state'] = DISABLED
			self.bt2['state'] = DISABLED

	def exibir(self):
		self.lb2['text'] = conjunto_padrão[self.n]
		self.bt1['state'] = ACTIVE
	 
	def limpar(self):
		self.lb1['text'] = ''
		self.lb2['text'] = ''



janela = Flash_Card()

