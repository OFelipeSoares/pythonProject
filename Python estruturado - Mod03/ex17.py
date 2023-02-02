import time

x = time.time()
print(f'Local time: {time.ctime(x)}')

#A variável x recebe o número de segundos desde 00:00:00 de 01/01/1970 pela função time().
# Ao executar ctime(x), o número de segundos armazenado em x é
# convertido em uma string com o horário local.
# A classe time.struct_time gera objetos sequenciais com valor de tempo retornado
# pelas funções gmtime() e localtime(). São objetos com interface de tupla nomeada:
# os valores podem ser acessados pelo índice e pelo nome do atributo.

