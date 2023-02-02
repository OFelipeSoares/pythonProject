from tkinter import* #A linha 1 mostra a importação de todos os elementos disponíveis em tkinter. O objeto janelaPrincipal é do tipo Tk.
# Um objeto Tk é um elemento que representa a janela GUI. Para que essa janela apareça, é necessário chamar o método mainloop();
def funcClicar():
        print("Botão pressioado")

janelaPrincipal = Tk()
texto = Label(master = janelaPrincipal, text = "Minha janela exibida")
texto.pack()

pic = PhotoImage(file="logoEstacio.jpg")
logo = Label(master = janelaPrincipal, image = pic)
logo.pack()

botao = Button(master = janelaPrincipal, text = 'Clique', command = funcClicar)
botao.pack()

janelaPrincipal.mainloop()