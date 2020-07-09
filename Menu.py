import tkinter 
from Configuracoes_deck import Configuracoes_deck
from Estudar import Estudar
from Informacoes import Informacoes
import sys

class Menu:
	def __init__(self, usuario, nome_user=None):
		self.usuario = usuario
		self.nome_user = nome_user
		self.janela = tkinter.Tk()
		self.janela.geometry('400x250+400+150')
		self.janela.title('Menu EMA')
		self.janela.resizable(0,0)
		self.janela.protocol('WM_DELETE_WINDOW', lambda: sys.exit())
		lb = tkinter.Label(self.janela, text='EMA - Estudo, memorização e aprendizagem', font=('Arial','8', 'bold'))
		lb.pack(side=tkinter.BOTTOM)

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
		self.labelFrame = tkinter.LabelFrame(self.janela)
		self.frame_1 =  tkinter.Frame(self.labelFrame)
		self.frame_2 = tkinter.Frame(self.labelFrame)
		self.frame_3 = tkinter.Frame(self.labelFrame)

		self.label =  tkinter.Label(self.frame_1, text='Bem vindo, ')
		self.label_1 = tkinter.Label(self.frame_1, text=self.nome_user, font=('Arial','10', 'bold'))

		self.label_2 = tkinter.Label(self.frame_2, text='Baralhos:', font=('Arial','10', 'bold'))
		self.label_3 = tkinter.Label(self.frame_2)

		self.label_4 = tkinter.Label(self.frame_3, text='Cartões:', font=('Arial','10', 'bold'))
		self.label_5 = tkinter.Label(self.frame_3)

		self.label.pack(side=tkinter.LEFT)
		self.label_1.pack(side=tkinter.RIGHT)

		self.label_2.pack(side=tkinter.RIGHT)
		self.label_3.pack(side=tkinter.LEFT)

		self.label_4.pack(side=tkinter.LEFT)
		self.label_5.pack(side=tkinter.RIGHT)

		self.frame_1.pack(anchor=tkinter.CENTER)
		self.frame_2.pack(anchor=tkinter.CENTER)
		self.frame_3.pack(anchor=tkinter.CENTER)
		self.labelFrame.pack(anchor=tkinter.CENTER)

		self.janela.mainloop()
		 	
	def estudar(self):
		self.janela.destroy()
		deck = Estudar(self.usuario)
		menu = Menu(self.usuario, self.nome_user)

	def config_cards(self):
		self.janela.destroy()
		deck = Configuracoes_deck(self.usuario)
		menu = Menu(self.usuario, self.nome_user)

	def info(self):
		self.janela.destroy()
		info = Informacoes()
		menu = Menu(self.usuario,self.nome_user)

	def deck_cartoes(self):
		pass

if __name__ == '__main__':
	app =Menu('l')