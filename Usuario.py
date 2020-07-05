class Usuario:
	def __init__(self):
		pass

	@property
	def nome(self):
		return self.__nome
	@nome.setter
	def nome(self, nome):
		if nome != '':
			if nome.isdigit():
					self.__nome = 'Erro: nome não pode conter números'
			else:
				self.__nome = nome
		else:
			self.__nome = 'Erro: nome está vazio'
	@property
	def senha(self):
		return self.__senha
	@senha.setter
	def senha(self, senha):
		if senha != '':
			if len(senha) < 6:
				self.__senha = 'Erro: número de caracteres insuficientes'
			else:
				self.__senha = senha
		else:
			self.__senha = 'Erro: senha está vazia'

	@property
	def email(self):
		return self.__email
	@email.setter
	def email(self, email):
		if email != '':
			self.__email = email
		else:
			self.__email = 'Erro: vazio'

	@property
	def username(self):
		return self.__username
	@username.setter
	def username(self, username):
		if username != '':
			if len(username) < 4:
				self.__username = 'Erro: número de caracteres insuficientes'
			else:
				self.__username = username
		else:
			self.__username = 'Erro: vazio'

	