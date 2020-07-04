import sqlite3
import os
import sys
import platform

class Banco_dados:
	def __init__(self, nome_conjunto=None):
		if platform.system() == 'Linux':
			self.dir_path = os.path.dirname(os.path.realpath(__file__)) + '/db/Ema'
			self.nome_conjunto = 'Ema'
		elif platform.system() == 'Windows':
			self.dir_path = os.path.dirname(os.path.realpath(__file__)) + '\\db\\Ema'
			self.nome_conjunto = 'Ema'
			
	def conectar(self):
		self.conexao = sqlite3.connect(self.dir_path)
		self.cursor = self.conexao.cursor()
		#self.criar_banco()

	def inserir_deck(self, nome_deck):
		self.cursor.execute('INSERT INTO deck (nome) VALUES (?)', (nome_deck,))
		self.conexao.commit()

	def criar_banco(self):
		self.conexao.execute('CREATE TABLE IF NOT EXISTS flashcards (''Codigo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,''Frente_card VARCHAR(100),''Verso_card TEXT(500)'')')

	def inserir_card(self, frente, verso, codigo_deck):
		self.cursor.execute('INSERT INTO flash_cards (codigo_deck, frente_card, verso_card) VALUES(?,?,?)', (codigo_deck, frente, verso))
		self.conexao.commit()

	def deletar_card(self, codigo):
		self.cursor.execute('DELETE FROM flash_cards WHERE codigo_card = (?)', (codigo,))
		self.conexao.commit()

	def deletar_deck(self, nome_deck):
		self.cursor.execute('SELECT codigo FROM deck WHERE nome = (?)', (nome_deck,))
		codigo = self.cursor.fetchall()
		codigo = int(codigo[0][0])
		self.cursor.execute('DELETE FROM flash_cards where codigo_deck = (?)', (codigo,))
		self.cursor.execute('DELETE FROM deck WHERE nome = (?)', (nome_deck,))
		self.conexao.commit()

	def alterar_card(self, codigo, frente, verso):
		self.cursor.execute('UPDATE flash_cards SET frente_card = (?), verso_card = (?) WHERE codigo_card = (?)', (frente, verso, codigo,))
		self.conexao.commit()

	def puxar_card(self, codigo_card):
		self.cursor.execute('SELECT codigo_card, frente_card, verso_card FROM flash_cards WHERE codigo_card = (?)', (codigo_card,))
		for linha_card in self.cursor.fetchall():
			codigo, frente_card, verso_card = linha_card
			return codigo, frente_card, verso_card

	def puxar_deck(self, codigo_deck):
		self.cursor.execute('SELECT frente_card, verso_card FROM flash_cards WHERE codigo_deck = (?)', (codigo_deck,))
		deck = {}
		for linha_card in self.cursor.fetchall():
			frente_card, verso_card = linha_card
			deck[frente_card] = verso_card
		return deck

	def puxar_codigo_deck(self, nome_deck):
		self.cursor.execute('SELECT codigo FROM deck WHERE nome = (?)', (nome_deck,))
		codigo = self.cursor.fetchone()
		codigo = codigo[0]
		return codigo

	def puxar_codigo_card(self, frente):
		self.cursor.execute('SELECT codigo_card FROM flash_cards WHERE frente_card = (?)', (frente,))
		codigo = self.cursor.fetchone()
		codigo = codigo[0]
		return codigo

	def listar_decks(self):
		self.cursor.execute('SELECT * FROM deck')
		deck = list()
		for linha in self.cursor.fetchall():
			codigo, nome = linha
			deck.append(nome)
		return deck

	def criar_login(self, nome, username, senha, email):
		pass
		
	def puxar_login(self):
		pass

	def fechar_banco(self):
		self.cursor.close()
		self.conexao.close()	

"""
bd = Banco_dados('teste')
#bd.criar_banco()
bd.inserir_card('1', 'lol')
print(bd.puxar_deck())
alter = input('Qual card vocẽ deseja alterar. Digite a frente:\n')
dado_1 = input('Nova frente:\n')	
dado_2 = input('Nova Verso:\n')
bd.alterar_card(dado_1, dado_2, alter)
print(bd.puxar_deck())
"""