#Implementar um programa para criar uma classe Veiculo com atributos de instância "Velocidade máxima" e "KM/litro"

class Veiculo:
    def __init__(self, nome, Vel_Max, KM_litro):
        self.nome = nome
        self.Vel_Max = Vel_Max
        self.KM_litro = KM_litro

    def toStr(self):
        print(f"nome: {self.nome}")
        print(f'A Velocidade Máxima é de: {self.Vel_Max} Km/h')
        print(f'A autonomia do carro é de: {self.KM_litro} Km/Litro')

modelo_carro = Veiculo('Fusca', 80, 5)
modelo_carro.toStr()

