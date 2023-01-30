#Em Python, as funções definidas pelo desenvolvedor devem
# ser precedidas pela palavra reservada def. Não são
# especificados o tipo de retorno e os tipos dos parâmetros,
# como no exemplo a seguir:

#def calculaIMC (peso, altura)

escolha = input("Escolha uma opção de função: 1 ou 2\n")
if escolha == "1":
    def func1(x):
        return x + 1
    s = func1(10)

else:
    def func2(x):
        return x + 2
    s = func2(10)

print(s)