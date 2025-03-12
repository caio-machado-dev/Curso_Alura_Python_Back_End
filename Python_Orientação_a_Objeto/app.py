from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato



restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('JackDaniel', 100.00, 'Grande')
prato = Prato('Camarão', 45.99,'ótimo prato' )

def main():
    print(bebida_suco)
    print(prato)


if __name__ == '__main__':  
    main()