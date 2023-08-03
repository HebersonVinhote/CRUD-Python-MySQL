import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='pythonteste',
    password='crudcompython',
    database='meubd'
)

cursor = conn.cursor()

# CREATE
nome_produto = 'Fanta Laranja 2L'
valor = 6
comando = f'INSERT INTO vendas (Nome_Produto, Valor_Produto) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
conn.commit()

# READ
comando2 = f'SELECT * FROM vendas'
cursor.execute(comando2)
resultado = cursor.fetchall()
print(resultado)

# UPDATE
nomeProduto = 'todynho'
novoValor = 6

comando3 = f'UPDATE vendas SET Valor_Produto = {novoValor} WHERE nome_produto = "{nomeProduto}"'
cursor.execute(comando3)
conn.commit()

# DELETE

nameProduct = 'manteiga'
comando4 = f'DELETE FROM vendas WHERE Nome_Produto = "{nameProduct}"'
cursor.execute(comando4)
conn.commit()


cursor.close()
conn.close()