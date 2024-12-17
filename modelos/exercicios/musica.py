# Exercício para prática de programação orientada a objetos
# Autor: Rciteli

class Musica:
    musicas = []

    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)

    def __str__(self):
        return f'{self.nome} | {self.artista} | {self.duracao}'
    
    def listar_musicas():
        for musica in Musica.musicas:
            print(f'{musica.nome} | {musica.artista} | {musica.duracao}')

musica_californication = Musica('Californication', 'Red Hot Chili Peppers', '3:52')
musica_numb = Musica('Numb', 'Linkin Park', '3:30')
musica_welcomeToTheJungle = Musica('Welcome to the Jungle', 'Guns & Roses', '4:10')

Musica.listar_musicas()