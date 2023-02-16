valor = 20

def multiplica(fator):
    global valor
    valor = valor*fator
    print("Resultado", valor)

def main():
    numero = int(input())
    multiplica(numero)
    multiplica(numero)

multiplica(3)
multiplica(3)