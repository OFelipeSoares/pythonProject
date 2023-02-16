#Houve apenas a adição de esteréotipo <> para indicar que Conta Cliente é uma classe abstrata. O Python utiliza
# um módulo chamado abc para definir uma classe como abstrata, a qual será herdeira da superclasse ABC (Abstract Base Classes).

from abc import ABC, abstractmethod
class ContaCliente(ABC):
    def __init__(self, numero, IOF, IR, valorinvestido, taxarendimento):
        self.numero = numero
        self.IOF = IOF
        self.IR = IR
        self.valorinvestido = valorinvestido
        self.taxarendimento = taxarendimento

    @abstractmethod
    def CalculoRendimento(self):
        pass