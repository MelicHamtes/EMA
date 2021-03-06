from tkinter import * 
import sys
import time 

class Pomodoro:
	def __init__(self, tempo=None):
		self.janela_pomodoro = Tk()
		self.janela_pomodoro.geometry('300x200')
		self.janela_pomodoro.resizable(0,0)
		self.janela_pomodoro.title('Pomodoro')
		self.numero_vezes_pomodoro = 0
		self.lb1 = Label(self.janela_pomodoro, text=tempo)
		self.lb1.config(font=('Arial', 20))
		self.lb1.pack()

		self.bt1 = Button(self.janela_pomodoro, text='Estudar', command=self.estudo)
		self.bt1.pack(side=BOTTOM)

		self.bt2 = Button(self.janela_pomodoro, text='Pausa', command=self.pausa)
		self.bt2.pack(side=BOTTOM)
		self.janela_pomodoro.mainloop()
		

	def estudo(self):
		minutos = 25
		minutos_convertidos = 25 * 60
		segundos = 60
		self.janela_pomodoro.destroy()
		for i in range(minutos_convertidos,0,-1):
			if segundos == 0:
				segundos = 60	
				minutos -= 1
			if minutos < 10:
				if segundos < 10:
					tempo = '0' + str(minutos) + '0' + str(segundos)
					sys.stdout.write(f'\r0{minutos}:0{segundos}\n')
					pm = Pomodoro(tempo=tempo)
				else:
					tempo = '0' + str(minutos)  + str(segundos)
					sys.stdout.write(f'\r0{minutos}:{segundos}\n')
					pm = Pomodoro(tempo=tempo)
			else:
				if segundos < 10:
					tempo =  str(minutos) + '0' + str(segundos)
					sys.stdout.write(f'\r{minutos}:0{segundos}\n')
					pm = Pomodoro(tempo=tempo)

				else:
					tempo = str(minutos)  + str(segundos)
					sys.stdout.write(f'\r{minutos}:{segundos}\n')
					pm = Pomodoro(tempo=tempo)

			pm.destroy()
			sys.stdout.flush()
			self.timesleep()
			segundos -= 1

	def pausa(self):
		pass
	def timesleep(self):
		time.sleep(1)

if __name__ == '__main__':
	pomodoro = Pomodoro()  
