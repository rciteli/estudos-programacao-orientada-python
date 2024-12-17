# Exercício para prática de programação orientada a objetos
# Autor: Rciteli

class Carro:
    carros = []

    def __init__(self, marca, modelo, cor, ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        Carro.carros.append(self)

    def __str__(self):
        return f'{self.marca} | {self.modelo} | {self.cor} | {self.ano}'
    
    def listar_carros():
        for carro in Carro.carros:
            print(f'{carro.marca} | {carro.modelo} | {carro.cor} | {carro.ano}')

carro_uno = Carro('Fiat', 'Uno', 'Prata', '1998')
carro_gol = Carro('VW','Gol', 'Preto', '2004')
carro_opala = Carro('Chevrolet', 'Chevrolet Opala', 'Amarelo', '1977')

Carro.listar_carros()