import sqlite3


conexao = sqlite3.connect('Ema')
cursor = conexao.cursor()

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
cursor.execute('''CREATE TABLE IF NOT EXISTS deck(codigo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nome VARCHAR(25))''')
cursor.execute('''CREATE TABLE IF NOT EXISTS flash_cards(codigo_deck INTEGER, frente_card VARCHAR(80), verso_card VARCHAR, codigo_card  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,  CONSTRAINT fk_codigo_deck FOREIGN KEY (codigo_deck) REFERENCES deck (codigo))''')
cursor.execute('SELECT * FROM flash_cards')
p = cursor.fetchall()
print(p)

cursor.close()
conexao.close()