import tkinter as tk 
from tkinter.font import Font
import webbrowser
import sys

class Informacoes:
	def __init__(self):
		self.janela_info = tk.Tk()
		self.janela_info.geometry('600x120+200+100')
		self.janela_info.title('SRS')
		self.janela_info.resizable(0,0)
		self.janela_info.protocol('WM_DELETE_WINDOW', lambda: self.janela_info.destroy())

		font_title = Font(family='Arial', size=12, weight='bold')
		font_text = Font(family='Arial', size=10)
		
		self.lb1 = tk.Label(self.janela_info, text='SRS')
		self.lb1.configure(font=font_title)
		self.lb1.pack(side=tk.TOP)

		self.lb2 = tk.Label(self.janela_info, text='Sites com informações sobre o SRS:')
		self.lb2.pack(side= tk.TOP)


		link1 = tk.Label(self.janela_info, text="O Sistema de Repetição Espaçada (SRS): memorizar para jamais esquecer", fg="blue", cursor="hand2")
		link1.pack()
		link1.bind("<Button-1>", lambda e: self.callback("https://www.mosalingua.com/pt/o-sistema-de-repeticao-espacada-memorizar-para-jamais-esquecer/	"))

		link2 = tk.Label(self.janela_info, text="Sistema de Repetição Espaçada: o que é e como aplicar esta técnica de memorização", fg="blue", cursor="hand2")
		link2.pack()
		link2.bind("<Button-1>", lambda e: self.callback("https://aprendafalaringles.com.br/sistema-de-repeticao-espacada/"))

		link3 = tk.Label(self.janela_info, text="Como usar a técnica da Repetição Espaçada para relembrar tudo o que você já estudou", fg="blue", cursor="hand2")
		link3.pack()
		link3.bind("<Button-1>", lambda e: self.callback("https://mude.vc/repeticao-espacada/"))

		self.janela_info.mainloop()

	def callback(self,url):
		webbrowser.open_new(url)

if __name__ == '__main__':
	info = Informacoes()