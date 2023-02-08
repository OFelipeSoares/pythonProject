@property
def saldo(self):
    return self._saldo
@saldo.setter
def saldo(self, saldo):
    if (self.saldo < 0):
        print("Saldo inválido")
    else:
        self._saldo = saldp