veiculos = ['avião', 'carro', 'navio', 'ônibus']

f_maiuscula = lambda x: str.capitalize(x)

nomes_maiusculos = list(map(f_maiuscula, veiculos))

print(nomes_maiusculos)
