#some todos os itens da lista

from functools import reduce

numeros = [1,2,3,4,5,6,7,8,9,10]

soma = lambda x,y: x+y

resultado = reduce(soma, numeros)

print(resultado)

minha_funcao = lambda x: x ** 2
resultado = minha_funcao(4)
print(resultado)