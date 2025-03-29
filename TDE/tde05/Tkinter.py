from tkinter import*

janela = Tk()

janela.title("Exemplo de Grid")
janela.geometry("400x300")


root = Label(janela, text="Olá, Tkinter!", font=("Arial", 14), fg="blue")
root.grid(row = 0, column= 0, padx=10, pady=10)



r = Entry(janela)
r.grid(row = 2, column = 0, padx = 10, pady =10)






janela.mainloop()