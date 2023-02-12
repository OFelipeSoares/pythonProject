from ContasClientesExtrato import Conta
from ContaPoupanca import Poupanca

class ContaRemuneradaPoupanca(Conta, poupanca):
    def __init__(self, taxaremuneracao, clientes, numero, saldo):
        Conta.__init__(self, clientes, numero, saldo)
        POupanca.__init__(self, taxaremuneracao)
        self.taxaremuneracao = taxaremuneracao

    def remuneraConta(self):
        self.saldo += self.saldo *(self.taxaremuneracao/30)
        self.saldo -= self.taxaremuneracao