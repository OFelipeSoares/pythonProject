#arredonde os números da lista de numeros de acordo com a lista de precisão de casas decimais
lista_numeros = [9.56783, 7.57568, 3.00914, 6.23211]
lista_precisao = [2,2,3,3]

arredondamento = lambda x, y: round(x,y)

resultado = list(map(arredondamento, lista_numeros, lista_precisao))

print(resultado)