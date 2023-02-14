#Crie uma classe filha "Ônibus" que herdará todas as variáveis e métodos da classe "Veiculo"

from atividade01 import Veiculo

class Onibus(Veiculo):
    pass

onibus_escolar = Onibus("Scania", 120, 8)
onibus_escolar.toStr()