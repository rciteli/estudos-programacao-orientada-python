from restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_mexicano = Restaurante('Taco Loco', 'Mexicana')
restaurante_japones = Restaurante('Sushitzu', 'Japonesa')


# Define a função main
def main():
    Restaurante.listar_restaurantes()

# Chama a função main
if __name__ == '__main__':
    main()