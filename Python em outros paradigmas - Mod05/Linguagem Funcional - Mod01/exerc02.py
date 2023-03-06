lista = [0,1,1,2,3,5,8,13,21,34]
pares = []

for x in lista:
    if x %2 == 0:
        pares.append(x)
    else:
        pass

print(pares)


#Solução da faculdade - Usando programação funcional

lista_1 = lista

fTesteParidade = lambda x: x % 2 == 0

print(f'Teste paridade(5) = {fTesteParidade(5)}')

pares_1 = list(filter(fTesteParidade, lista_1))

print(f'lista de números pares = {pares_1}')