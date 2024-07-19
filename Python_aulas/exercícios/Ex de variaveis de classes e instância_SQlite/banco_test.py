# Cria um banco de dados chamado exemplo.sqlite e uma tabela chamada clientes
import sqlite3

banco_test = sqlite3.connect("exemplo.sqlite")
cursor = banco_test.cursor()

# Cria a tabela clientes
#cursor.execute("CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))")

# Insere dados na tabela clientes
#data = ("Maria", "maria@gmail.com")
#cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", data)
#banco_test.commit()  

# atualiza dados na tabela clientes
def criar_tabela(banco_test, cursor):
    cursor.execute("CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))")
    banco_test.commit()

def inserir_dados(banco_test, cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", data)
    banco_test.commit()

def atualizar_dados(banco_test, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome = ?, email = ? WHERE id = ?", data)
    banco_test.commit()

atualizar_dados(banco_test, cursor, "Marina", "marina@gmail.com", 2)

# adicionar varios dados na tabela clientes
def iserir_muitos(banco_test, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?, ?)", dados)
    banco_test.commit()

dados = [("João", "joao@gmail.com"),
         ("Maria", "maria@gmail.com"),
]

iserir_muitos(banco_test, cursor, dados)