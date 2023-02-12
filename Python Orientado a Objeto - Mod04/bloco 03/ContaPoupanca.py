import datetime
class ContaPoupanca:
    def __init__(self, taxaremuneracao):
        self.taxaremuneracao = taxaremuneracao
        self.sata_abertura = datetime.datetime.today()

    def remuneraaoConta(self):
        self.saldo += self.saldo * self.taxaremuneracao