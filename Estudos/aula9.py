from tkinter import messagebox
from mysql import connector
import mysql
from tkinter import *

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

def inserir():
    codigo = e_codigo.get()
    nome = e_nome.get()
    preco =e_preco.get()
    quantidade = e_quantidade.get()

    if(codigo=='' or nome=='' or preco=='' or quantidade==''):
        messagebox.showerror('Inserir', 'Todos os campos são obrigatórios')
    else:
        c.execute('insert into produto(codigo, nome, preco, quantidade) values(%s,%s,%s,%s)'
                  '', (codigo, nome, preco, quantidade))
        con.commit()
        messagebox.showinfo('Inserir', 'Produto Inserido com sucesso')

        e_codigo.delete(0,END)
        e_nome.delete(0,END)
        e_preco.delete(0,END)
        e_quantidade.delete(0,END)
def excluir():
    codigo = e_codigo.get()
    if codigo == '':
        messagebox.showerror('Excluir', 'Informe o código do produto')
    else:
        c.execute('delete from produto where codigo=%s', (codigo,))
        con.commit()
        messagebox.showinfo('Excluir', 'Produto Excluido com sucesso')
        e_codigo.delete(0,END)


def atualizar():
    codigo = e_codigo.get()
    nome = e_nome.get()
    preco = e_preco.get()
    quantidade = e_quantidade.get()

    if(codigo=='' or nome=='' or preco=='' or quantidade==''):
        messagebox.showerror('Atualizar', 'Todos os campos são obrigatórios')
    else:
        c.execute('update produto set nome=%s, preco=%s, quantidade=%s where codigo=%s',
                  (nome, preco, quantidade, codigo))
        con.commit()
        messagebox.showinfo('Atualizar', 'Produto Atualizado com sucesso')

        e_codigo.delete(0,END)
        e_nome.delete(0,END)
        e_preco.delete(0,END)
        e_quantidade.delete(0,END)

def selecionar():
    codigo = e_codigo.get()
    if codigo == '':
        messagebox.showerror('Excluir', 'Informe o codigo do produto')
    else:
        c.execute('select * from produto where codigo=%s', (codigo,))
        r = c.fetchall()

        if r:
            for r1 in r:
                e_nome.delete(0,END)
                e_preco.delete(0,END)
                e_quantidade.delete(0,END)

                e_nome.insert(0,r1[1])
                e_preco.insert(0,r1[2])
                e_quantidade.insert(0,r1[3])
                messagebox.showinfo('Selecionando', 'Selecionado com sucesso!'f'Codigo:{r1[0]}\nNome:{r1[1]}\nPreco:{r1[2]}\nQuantidade:{r1[3]}')

            else:
                messagebox.showerror('Selecionando', 'Selecionado com sucesso!')






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


frame_botoes = Frame(root)
frame_botoes.grid(row=120, column=0, columnspan=2, pady=10)

Button(root, text='Consultar', command=atualizar).place(x=100, y=160)
Button(root, text='Inserir', command=inserir).place(x=180, y=160)
Button(root, text='Alterar', command=selecionar).place(x=260, y=160)
Button(root, text='Excluir', command=excluir).place(x=340, y=160)


root.mainloop()

