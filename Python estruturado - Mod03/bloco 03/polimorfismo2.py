class Veiculo:
    def rodar(self):
        print("Reduz o consumo de ccmbustível.")

class VeiculoEletrico(Veiculo):
    def rodar(self):
        super().rodar()
        print("Esse veículo utiliza eletricidade")

veiculo_eletrico = VeiculoEletrico()
veiculo_eletrico.rodar()