import math

x = math.sqrt(5) #sqrt -> retorna a raiz quadrada de qqr número inteiro
print(x)

# math -> usado para operações matemáticas
# random -> usado para gerar nº pseudoaleatórios
# smtplib -> Usado para permitir envio de e-mails
# time -> implementar contadores temporais
# tkinter -> desenvolver interfaces gáficas

# MÓDULOS NATIVOS DO PYTHON
    # Módulo Math
        # sqrt(x) -> raiz quadrada de x
        # ceil(x) -> menor inteiro maior ou igual a x
        # floor(x) -> Maior inteiro menor ou igual a x
        # cos(x) -> Cosseno de x
        # sin(x) -> Seno de x
        # log(x, b) -> Logaritimo de x na base b
        # pi -> Valor de Pi(3.141592...)
        # e -> Valor de e (2.718281...)

    # Módulo Random
        # Nº nteiros -> Seleção a partir de um intervalo
        # Sequências -> Seleção de um elemento aleatório em dado intervalo

        # random() -> Ponto flutuante no intervalo (00,0, 1,0)
        # uniforme(a, b) -> Nº de ponto flutuante N tal que a<=N<=b
        # gauss(mu, sigma) -> Distribuição gaussiana. mu = média e sigma = desvio padrão.
        # normalvariante(mu, sigma) -> Distribuição gaussiana. mu = média e sigma = desvio padrão.

    #Funções para Nº Inteiros
        # randrange(stop) -> Um elemento selecionado aleatório de range(start, stop, step), mas sem construir um objeto range.
        # randrange(start, stop, [step])
        # randint(a, b) -> Numero inteiro N tal que a<=N<=b

    #Funções para sequências
        # choice(seq) -> Elemento aleatório de uma sequência não vazia seq.
        # shuffle(x[, random]) -> Embaralha a sequência x no lugar.
        # sample(pop, k) -> Uma sequência de tamanho k de elementos escolhidos da população pop, sem repetição.
                            #Usada para amostragem sem substituição.

    # Módulo Time
        # time() -> Número de segundos passados desde o início da contagem (epoch). Por padrão, o início é 00:00:00 do dia 1 de janeiro de 1970.
        # ctime(segundos) -> Uma string representando o horário local, calculado a partir do número de segundos passado como parâmetro
        # gmtime(segundos) -> Converte o número de segundos em um objeto struct_time descrito a seguir.
        # localtime(segundos) -> Semelhante à gmtime(), mas converte para o horário local.
        # sleep(segundos) -> 	A função suspende a execução por determinado número de segundos.