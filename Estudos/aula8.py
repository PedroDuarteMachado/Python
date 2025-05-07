import mysql
from mysql import connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='aula8'
)

cursor = conexao.cursor()

#cursor.execute('create database if not exists aula8')


'''
#mostrar todas as bases de dados -------------------
cursor.execute('show databases')
for i in cursor:
    print(i)

#usando o banco de dados ---------------------------

cursor.execute('use aula8')
'''

#criar tablela -------------------------------------
"""
cursor.execute('''create table if not exists aluno(
               matricula int primary key auto_increment,
               nome varchar(50) not null,
               idade int(3),
               email varchar(40))''')

#mostrar todas as tabelas -------------------------

cursor.execute('show tables')
for i in cursor:
    print(i)

#mostrar a descrição da tabela (desc ou describe)--------------------

cursor.execute('desc aluno')
for i in cursor:
    print(i)

#inserir dados na tabela - insert into nome da tabela (atributos) values(valores)

y = 'insert into aluno(nome,idade,email) values("Pedro", 23, "pedro@gmail.com")'

cursor.execute(y)
conexao.commit()

print(cursor.rowcount,'Registro(s) inserido(s)')
"""
"""
v = [
    ("Luana", 18, "teste@gmail.com"),
    ("Guilherme", 29, "teste1@gmail.com"),
    ("Gabriel", 43, "teste2@gmail.com"),
    ("Rodrigo", 20, "teste3@gmail.com"),
    ("Raquel", 22, "teste4@gmail.com"),
    ("Marcella", 21, "teste5@gmail.com"),
    ("Enzo", 20, "teste6@gmail.com"),
    ("Natan", 19, "teste7@gmail.com"),
    ("Ryan", 21, "teste8@gmail.com"),
    ("Lara", 18, "teste9@gmail.com"),
]

cursor.executemany('insert into aluno(nome,idade,email) values(%s,%s,%s)', v)
conexao.commit()
print(cursor.rowcount, 'Registro(s) inserido(s)')

#seleção simples -------------------------------------------------------------

cursor.execute('select * from aluno')
r = cursor.fetchall() '  ou    fetchone'

print('Dados do aluno: ')
for i in r:
    print(i)

#seleção condição - where ---------------------------------------------------

cursor.execute('select nome from aluno where idade > 20')
r = cursor.fetchall()
print('Dados do aluno: ')
for i in r:
    print(i)

#Ordenação asc/desc - order by -----------------------------------------------


cursor.execute('select nome from aluno where idade > 30 order by nome desc')
r = cursor.fetchall()
print('Dados do aluno ordenado (A-Z)')
for i in r:
    print(i)

#delete - deletar apenas 1 registro ----------------------------------

cursor.execute('delete from aluno where matricula=1')
conexao.commit()
print(cursor.rowcount, 'Registro(s) Deletados(s)')

#deletar multiplos registros IN -----------------------------------

# r = 'delete from aluno where matricula in(%s,%s)'
# cursor.execute(r,(2,4))
# conexao.commit()
# print(cursor.rowcount, 'Registro(s) Deletados(s)')

#deletar com intervalo - between -----------------------------------

r1='delete from aluno where matricula between %s and %s'
cursor.execute(r1,(6,9))
conexao.commit()
print(cursor.rowcount, 'Registro(s) Deletados(s)')

#update - atualizar -------------------------------

cursor.execute('update aluno set nome="Tatiana Viana" where matricula=1')
conexao.commit()
print(cursor.rowcount, 'Registro(s) atualizado(s)')"""

#drop - apaga tudo ---------------------------------------------------

#cursor.execute('drop database aula8')
cursor.execute('drop table aluno')















