import datetime

class ContaPoupanca:
    def __init__(self, taxaremuneracao):
        self.taxaremuneracao = taxaremuneracao
        self.data_abertura = datetime.datetime.today()

    def remuneracaoConta(self):
        self.saldo += self.saldo * self.taxaremuneracao


class ContaClinete:

    def __init__(self, numero, IOF, IR, valorinvestido, taxarendimento ):
        self.numero = numero
        self.IOF = IOF
        self.IR = IR
        self.valorinvestido = valorinvestido
        self.taxarendimento = taxarendimento


    def CalculoRendimento(self):
        self.valorinvestido += (self.valorinvestido * self.taxarendimento)
        self.valorinvestido = (self.valorinvestido - (self.taxarendimento - self.IOF * self.IR))

    def Extrato(self): #(1)
        print(f'O saldo atual da conta {self.numero} é: {self.valorinvestido:10.2f}')
