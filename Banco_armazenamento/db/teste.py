import sqlite3
import mysql.connector


'''

conexao = mysql.connector.connect(
		host='localhost',
		user='root',
		password='root',
		database='EMA'
	)'''
conexao = sqlite3.connect('Ema')
cursor = conexao.cursor()

cursor.execute('PRAGMA foreign_keys=ON')
'''
n = input('digite o nome da tabela')
cursor.execute("DROP TABLE n")
cursor.execute("CREATE TABLE n (id INTEGER, nome TEXT)")
cursor.execute("INSERT INTO n VALUES (1, 'Lucas')")
cursor.execute("SELECT * FROM n")
cursor.execute("SELECT * FROM sqlite_master WHERE type='table'")
al = cursor.fetchall()
print(al)
'''

cursor.execute('CREATE TABLE IF NOT EXISTS Usuario(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nome VARCHAR(40), senha VARCHAR(20), email VARCHAR(35), userName VARCHAR(15))')
cursor.execute('CREATE TABLE IF NOT EXISTS Deck(codigo INTEGER NOT NULL DEFAULT 0 PRIMARY KEY AUTOINCREMENT, nome VARCHAR(25), idUsuario INTEGER NOT NULL, CONSTRAINT fk_idUsuario FOREIGN KEY (idUsuario) REFERENCES Usuario(id))')
cursor.execute('CREATE TABLE IF NOT EXISTS Card(codigoDeck INTEGER NOT NULL , frenteCard VARCHAR(80), versoCard VARCHAR(250), idCard  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, CONSTRAINT fk_codigoDeck FOREIGN KEY (codigoDeck) REFERENCES Deck(codigo))')
#cursor.execute('INSERT INTO Usuario values (?,?,?,?,?)', (1, 'Marcos', '1234','marquinhos@gmail.com', 'm4rcos'))
cursor.execute('SELECT * FROM Usuario')
p = cursor.fetchall()
print(p)
#cursor.execute('INSERT INTO Usuario VALUES ()')
#cursor.execute('INSERT INTO Deck values (?,?,?)', (3,'FOGo', 1))
#cursor.execute('INSERT INTO Deck values (?,?,?)', (0,'agua', 1,))
#cursor.execute('INSERT INTO Card VALUES (?,?,?,?)', (3, 'Church', 'Igreja', 4))


conexao.close()