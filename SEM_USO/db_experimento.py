import sqlite3
import os
import platform 
class Teste:
	def __init__(self):
		if platform.system() == 'Linux':
			dir_path = '/home/melic/PROJETOS/LP/EMA/Banco_armazenamento/db/'
		elif platform.system() == 'Windows':
			dir_path = os.path.dirname(os.path.realpath(__file__)) + '\\db\\Ema.db'
		
		conexao = sqlite3.connect(dir_path)
		cursor = conexao.cursor()
		self.di = {}
		conexao.execute('CREATE TABLE IF NOT EXISTS flashcards (''Codigo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,''Frente_card VARCHAR(100),''Verso_card TEXT(500)'')')
		
		cursor.execute('SELECT * FROM flashcards')
		for linha in cursor.fetchall():
			codigo, frente, verso = linha
			#print(linha)
			self.di[frente] = verso		
			print(linha)

		resposta = input('Deseja inserir dados no banco de dados?\n')
		if resposta.upper() == 'S':
			n = input('Quantos valores serão inseridos?\n')
			for i in range(int(n)):
				beri = input()
				cco = input()
				cursor.execute('INSERT INTO flashcards (Frente_card, Verso_card) VALUES(?,?)',(beri, cco))
		conexao.commit()
		
		resposta = str()

		resposta = input('Deseja alterar dados no banco de dados?\n')	
		if resposta.upper() == 'S':
			frente = input('Digite a frente do valor a ser alterado\n') 
			cursor.execute('SELECT Codigo FROM flashcards WHERE Frente_card = (?)', (frente,))
			codigo = cursor.fetchall()
			codigo = codigo[0][0] 
			print(codigo, type(codigo))
			frente = input()
			verso = input()
			cursor.execute('UPDATE flashcards SET Frente_card = (?), Verso_card = (?) WHERE Codigo = (?)', (frente, verso, codigo,))
		conexao.commit()

		resposta = str()

		resposta = input('Deseja excluir algum?\n')
		if resposta.upper() == 'S':
			codigo = int(input('Digite o codigo:\n'))
			cursor.execute('DELETE FROM flashcards WHERE Codigo = (?)', (codigo,))
			conexao.commit()


		cursor.execute('SELECT * FROM flashcards')
		for linha in cursor.fetchall():
			codigo, frente, verso = linha
			#print(linha)
			self.di[frente] = verso		
			print(linha)

		#print(self.di)	
		resposta = input('Deseja limpar o banco de dados?\n')

		if resposta.upper() == 'S':
			cursor.execute('DELETE flashcards')
			conexao.commit()
			print('Banco limpo')
		else:
			cursor.close()
			conexao.close()	

tt = Teste()