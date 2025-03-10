from Python_Orientação_a_Objeto.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicano')
restaurante_japones = Restaurante('Japa', 'Japonesa')

restaurante_mexicano.alternar_estado()

restaurante_praca.receber_avaliacao('Caio', 2)
restaurante_japones.receber_avaliacao('Caio', 5)
restaurante_mexicano.receber_avaliacao('Caio', 4)

print(restaurante_praca._avaliacao)  # Deve exibir uma lista de objetos Avaliacao


def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':  
    main()