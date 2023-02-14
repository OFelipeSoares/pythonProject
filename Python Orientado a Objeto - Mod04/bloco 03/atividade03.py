#Modificar a classe filha "Ônibus", de modo que foneça os assentos
class Veiculo:
    def __init__(self, nome, Vel_Max, KM_litro):
        self.nome = nome
        self.Vel_Max = Vel_Max
        self.KM_litro = KM_litro

    def capacidade(self, capacidade):
        print(f'A capacidade máxima de assentos no veículo: {self.nome} é de {capacidade} lugares')

    def toStr(self):
        print(f"nome: {self.nome}")
        print(f'A Velocidade Máxima é de: {self.Vel_Max} Km/h')
        print(f'A autonomia do carro é de: {self.KM_litro} Km/Litro')

class Onibus(Veiculo):
    def capacidade(self, capacidade=70):
        return super().capacidade(capacidade=70)


onibus_escolar = Onibus('Scania', 120, 8)
onibus_escolar.toStr()
onibus_escolar.capacidade()

