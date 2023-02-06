"A forma de realizar a captura e tratamento de erros é utiizar o par try/except"
"No primeiro constam as instruções nornais, ao passo que no segundi o que deve ser feito em caso de exceção"

try:
    num = eval(input("Entre com um número inteiro: \n"))
    print(num)
except "NameError - forma de tratar uma exceção em específico" :
    print("Entre com o valor numérico e não letras")

"PY permite diversos tratamentos de erros atrelados ao mesmo bloco try"
try:
        num = eval(input("Entre com um número inteiro: \n"))
        print(num)
    except ValueError:
        print("Mensagem 1")
    except IndexError:
        print("Mensagem 2")
    except:
        print("Mensagem 3")


"De forma geral, o tratamento de exceções é feito da seguinte forma"
try:
  Bloco 1
except Exception1:
  Bloco tratador para Exception1
except Exception2:
  Bloco tratador para Exception1
...
else:
  Bloco 2 – executado caso nenhuma exceção seja levantada
finally:
  Bloco 3 – executado independente do que ocorrer
Instrução fora do try/except

"sendo as cláusulas else e finally opcionais"