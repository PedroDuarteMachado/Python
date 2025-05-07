from mysql import connector
import mysql
from tkinter import*

con = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='loja'
)

c = con.cursor()
#c.execute('create database loja')
#c.execute('use loja')

# c.execute('''create table produto(
#             codigo int primary key,
#             nome varchar(20) not null,
#             preco decimal(10,2) not null,
#             quantidade integer not null)''')

root = Tk()
root.geometry('500x300')
root.title('Loja')

Label(root, text='Código').place(x=20,y=30)
Label(root, text='Nome').place(x=20,y=60)
Label(root, text='Preço').place(x=20,y=90)
Label(root, text='Quantidade').place(x=20,y=120)


e_codigo = Entry(root)
e_codigo.place(x=100,y=30)

e_nome = Entry(root)
e_nome.place(x=100,y=60)

e_preco = Entry(root)
e_preco.place(x=100, y=90)

e_quantidade = Entry(root)
e_quantidade.place(x=100, y=120)



root.mainloop()

