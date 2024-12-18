from restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_praca.receber_avaliacao('João', 5)
restaurante_praca.receber_avaliacao('Maria', 4)
restaurante_praca.receber_avaliacao('Pedro', 3)
restaurante_praca.receber_avaliacao('Ana', 4)
restaurante_praca.receber_avaliacao('Carlos', 5)


# Define a função main
def main():
    Restaurante.listar_restaurantes()

# Chama a função main
if __name__ == '__main__':
    main()