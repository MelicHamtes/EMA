class Controlador:
	def __init__(self):
		'''
		self._deck = str()
		self._frente = str()
		self._verso = str()
		self._codigo = int()
		'''
	@property
	def deck(self):
		return self._deck

	@deck.setter
	def deck(self, deck):
		for index in range(len(deck)):
			if deck[0].isdigit():
				deck = deck.replace(deck[0], '')
			cont = 0
			while cont < len(deck):
				deck = deck.lower()
				if deck[cont] == ' ':
					deck = deck.replace(deck[cont],'')
				if deck[cont] == '_':
					deck = deck.replace(deck[cont], '')
				cont += 1	
		self._deck = deck

	@property
	def frente(self):
		return self._frente 
	@frente.setter
	def frente(self, frente):
		frente = frente.rstrip('\n')
		self._frente = frente

	@property
	def verso(self):
		return self._verso
	@verso.setter
	def verso(self, verso):
		verso = verso.rstrip('\n')
		self._verso = verso

	@property
	def codigo(self):
		return self._codigo
	@codigo.setter
	def codigo(self, codigo):
		codigo = codigo.rstrip('\n')
		self._codigo = codigo

#d = (input('Insira o nome do deck\n'))
#f = (input('Digite a frente\n'))
#v = (input('Digite o verso\n'))
#cc = Controlador()
#cc.deck = d
#print(cc.deck)
#cc.frente = f
#cc.verso = v
#print('Nome do deck: {};\n Frente:{}\n Verso: {} '.format(cc.deck,cc.frente,cc.verso))


