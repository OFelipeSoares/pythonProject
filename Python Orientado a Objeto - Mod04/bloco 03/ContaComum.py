from ContaCliente import ContaClinete

class ContaComun(ContaClinete):
    def __init__(self, numero, IOF, IR, valorinvestido, taxarendimento):
        super().__init__(numero, IOF, IR, valorinvestido, taxarendimento)

    def CalculoRendimento(self): #2
        self.valorinvestido += (self.valorinvestido * self.taxarendimento)