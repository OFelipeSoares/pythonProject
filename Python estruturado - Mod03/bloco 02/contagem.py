class Pessoa:
    _contador = 0
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        Pesso._contador += 1
    def imprimir(self):
        print(self.nome, "tem", self.idade, "ano(s)")

    @property
    def contador(self):
        return type(self)._contador

p1 = Pessoa("Carlos", 18)
print(p1.contador)
print(Pessoa._contador)

class NomeCompleto:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    @classmethod
    def fromString(cls, texto):
        nome, sobrenome = map(str, texto.split(''))
        objeto = cls(nome, sobrenome)
        return objeto
registro1 = NomeCompleto.fromString("Luiz Braga")