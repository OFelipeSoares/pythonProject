from ContaCliente import ContaClinete

class ContaRemunerada(ContaClinete):
    def __init__(self, numero, IOF, IR, valorinvestido, taxarendimento):
        super().__init__(numero, IOF,IR,valorinvestido, taxarendimento)

    def CalculoRendimento(self): #3
        self.valorinvestido += (self.valorinvestido * self.taxarendimento)
        self.valorinvestido -= self.valorinvestido *self.IOF