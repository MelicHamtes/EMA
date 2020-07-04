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
					return 'Erro: nome não pode conter números'
			else:
				self.__nome = nome
		else:
			return 'Erro: vazio'
	@property
	def senha(self):
		return self.__senha
	@senha.setter
	def senha(self, senha):
		if senha != '':
			if len(senha) < 6:
				return 'Erro: número de caracteres insuficientes'
			else:
				self.__senha = senha
		else:
			return 'Erro: vazio'

	@property
	def email(self):
		return self.__email
	@email.setter
	def email(self, email):
		if email != '':
			self.__email = email
		else:
			return 'Erro: vazio'

	@property
	def username(self):
		return self.__username
	@username.setter
	def username(self, username):
		if username != '':
			if len(username) < 4:
				return 'Erro: número de caracteres insuficientes'
			else:
				self.__username = username
		else:
			return 'Erro: vazio'

	