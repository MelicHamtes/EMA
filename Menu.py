import tkinter 
from Deck import Deck, Deck_Estudo
from Informacoes import Informacoes
import sys

class Menu:
	def __init__(self):
		self.janela = tkinter.Tk()
		self.janela.geometry('600x400+500+200')
		self.janela.title('Menu EMA')
		self.janela.resizable(0,0)
		self.janela.protocol('WM_DELETE_WINDOW', lambda: sys.exit())
		lb = tkinter.Label(self.janela, text='EMA - Estudo, memorização e aprendizagem')
		lb.pack(side=tkinter.TOP)

		self.menu = tkinter.Menu(self.janela)
		self.menu_SRS = tkinter.Menu(self.menu, tearoff=0)

		self.menu_SRS.add_command(label='Estudar', command=self.estudar)
		self.menu_SRS.add_command(label='Confi. cards', command=self.config_cards)
		self.menu.add_cascade(label='SRS', menu=self.menu_SRS)

		self.menuInfo = tkinter.Menu(self.menu, tearoff=0)
		self.menuInfo.add_command(label='SRS', command=self.info)
		#menuInfo.add_command(label='Pomodoro')
		self.menu.add_cascade(label='Info', menu=self.menuInfo)		

		self.janela.config(menu=self.menu)

		self.janela.mainloop()
		 	
	def estudar(self):
		deck = Deck_Estudo()
		menu = Menu()

	def config_cards(self):
		deck = Deck()
		menu = Menu()

	def info(self):
		info = Informacoes()
		menu = Menu()

menu = Menu()