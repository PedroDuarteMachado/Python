from tkinter import*

janela = Tk()

janela.title("Exemplo de Grid")
janela.geometry("400x300")

# r = Entry(janela)
# r.grid(row = 2, column = 30, padx = 10, pady =10)

#1-
# def mostrar_informacoes():
#     num = r.get()
#     try:
#         num = int(num)
#         if(num > 0):
#             label_posi = Label(janela, text="Positivo", font=("Arial", 12))
#             label_posi.grid(row = 6, column = 40, padx=10,pady=10)
#         else:
#             label_nega = Label(janela, text="Negativo", font=("Arial", 12))
#             label_nega.grid(row = 6, column = 40, padx=10,pady=10)
#     except ValueError:
#         r.config(text="Digite um número válido!", fg="black")

# btn = Button(janela, text="Enviar", font=("Arial", 12), command=mostrar_informacoes)
# btn.grid(row = 5, column = 30, padx =10, pady = 10)


#2-
# o = Entry(janela)
# o.grid(row = 3, column = 30, padx = 10, pady =10)

# def verificar():
#     try:
#         num_lista = r.get()
#         lim_lista = o.get()

#         lista = list(map(int,num_lista.split(',')))
#         limite = int(lim_lista)

#         ind = next((i for i, num in enumerate(lista) if num > limite), -1)

#         result.config(text=f"Índice: {ind}")
#     except ValueError:
#         result.config("valor inválido.")

# btn = Button(janela, text="Enviar", command=verificar)
# btn.grid(row = 5, column = 30, padx =10, pady = 10)


# result = Label(janela, text="", font=("Arial", 12))
# result.grid(row=6, column=30, padx=10,pady=10)

#3-
# def ano_bissexto():
#     ano = r.get()
#     try:
#         ano = int(ano)
#         if(ano % 4 == 0):
#             result = Label(janela, text=("Ano bissexto!"))
#             result.grid(row = 6, column = 40, padx=10,pady=10)
#         else:
#             result = Label(janela, text=("Este ano não é bissexto!"))
#             result.grid(row=6, column =40,padx =10, pady=10)

#     except ValueError:        
#         r.config(text="Digite um número válido!", fg="black")       

# btn = Button(janela, text="Enviar", command=ano_bissexto)
# btn.grid(row=5, column= 30, padx = 10, pady = 10)

# result = Label(janela, text="", font=("Arial", 12))
# result.grid(row=6, column=30, padx=10,pady=10)       
        
#4-
# r1 = Entry(janela)
# r1.grid(row = 2, column = 30, padx = 10, pady =10)
# r2 = Entry(janela)
# r2.grid(row = 3, column = 30, padx = 10, pady =10)

# def calculadora(op):
#  try:
#         num1 = int(r1.get())
#         num2 = int(r2.get())

#         if op == "somar":
#             result = num1 + num2
#         elif op == "subtrair":
#             result = num1 - num2
#         elif op == "multiplicar":
#             result = num1 * num2
#         elif op == "dividir":
#             if r2 == 0:
#                 result = "Erro: Divisão por zero"
#             else:
#                 result = num1 / num2
#         result_label.config(text=f"Resultado: {result}")

#  except ValueError:
#         result_label.config(text="Erro: Insira números válidos!") 

# btn1 = Button(janela, text="Somar", command=lambda: calculadora("somar"))
# btn1.grid(row=5, column=20,padx=10, pady=10)

# btn2 = Button(janela, text="Subtrair", command=lambda: calculadora("subtrair"))
# btn2.grid(row=5, column=25,padx=10, pady=10)

# btn3 = Button(janela, text="Multiplicar",command=lambda:calculadora("multiplicar"))
# btn3.grid(row=5, column=30,padx=10, pady=10)

# btn4 = Button(janela, text="Dividir",command=lambda:calculadora("dividir"))
# btn4.grid(row=5, column=35,padx=10, pady=10)

# result_label = Label(janela, text="Resultado: ", font=("Arial", 12))
# result_label.grid(row=10, column=30, padx=10,pady=10)   

#5-

def analisar():
    try:
        num = [int(r1.get()), int(r2.get()), int(r3.get()), int(r4.get())]
        print(num)

        qtd_nove = num.count(9)

        if 3 in num:
          ind_tres = num.index(3) + 1
        else: 
           ind_tres = "Não encontrado!"
        
        pares = []
        for numeros in num:
           if numeros % 2 == 0:
                pares.append(numeros)

        if pares:
            num_pares = ", ".join(map(str, pares))
        else:
            num_pares = "Nenhum número par"

        result_label.config(text=f"Qtd 9: {qtd_nove}\n1º 3: {ind_tres}\nPares: {num_pares}")
    
    except ValueError:
            result_label.config(text="Erro: Insira apenas números!")




r1 = Entry() 
r1.grid(row = 2, column = 30, padx = 10, pady =10)

r2 = Entry()
r2.grid(row = 5, column = 30, padx = 10, pady =10)

r3 = Entry()
r3.grid(row = 2, column = 60, padx = 10, pady =10)

r4 = Entry()
r4.grid(row = 5, column = 60, padx = 10, pady =10)


btn = Button(janela, text="Analisar", command= analisar)
btn.grid(row = 8, column = 30, padx = 10, pady = 10 )

result_label = Label(janela, text="Resultado: ", font=("Arial", 12))
result_label.grid(row=10, column=30, padx=10,pady=10)  



janela.mainloop()