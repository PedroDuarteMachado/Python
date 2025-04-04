from tkinter import*

dicionario = {
    "fruta": ["uva","limão", "kiwi"],
    "preço": [13.99, 4.00, 32.99]
}




def verificar_dici():
        fruta = resp.get()
        if fruta in dicionario["fruta"]:
            i = dicionario["fruta"].index(fruta)
            preco = dicionario["preço"][i]
            rotulo_resultado.config(text= "tem "+f"{fruta} no estoque por R$ {preco:.2f}")
        else:
            rotulo_resultado.config(text="não tem"+ f"{fruta} está no estoque")

def  produtoNovo(): 
    




i = Tk()
i.geometry('600x300')


rotulo = Label(i, text="Entrada")
rotulo.grid(row = 1, column=10,padx=10, pady=5)
resp = Entry()
resp.grid(row = 2, column= 10, padx=10, pady=5)


btn = Button(i, text="Verificar", command=verificar_dici)
btn.grid(row = 3, column = 10, padx = 10, pady=5)

btn2 = Button(i, text="Inserir Produto", command=produtoNovo)
btn.grid(row = 3, column = 15, padx = 10, pady = 5 )

rotulo_resultado = Label(i, text="")
rotulo_resultado.grid(row =4, column = 10, padx= 10, pady=5)











i.mainloop()