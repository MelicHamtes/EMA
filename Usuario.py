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
					self.__nome = 'nome não pode conter números'
			else:
				self.__nome = nome
		else:
			self.__nome = 'nome está vazio'
	@property
	def senha(self):
		return self.__senha
	@senha.setter
	def senha(self, senha):
		if senha != '':
			if len(senha) < 6:
				self.__senha = 'número de caracteres da senha insuficiente, mínimo 6'
			else:
				self.__senha = senha
		else:
			self.__senha = 'senha está vazia'

	@property
	def email(self):
		return self.__email
	@email.setter
	def email(self, email):
		if email != '':
			#for i in range(len(email)):
				#if email[i:] == '@gmail.com':
			self.__email = email
				#elif email[i:] == '@outlook.com':
					#self.__email = email
				#else:
					#self.__email = 'email não contem endereço correto'
		else:
			self.__email = 'email está vazio'

	@property
	def username(self):
		return self.__username
	@username.setter
	def username(self, username):
		if username != '':
			if len(username) < 4:
				self.__username = 'número de caracteres de usuário insuficiente, mínimo 4'
			else:
				self.__username = username
		else:
			self.__username = 'username está vazio'

	