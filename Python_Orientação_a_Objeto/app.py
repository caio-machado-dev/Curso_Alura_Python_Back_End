from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa



restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('JackDaniel', 100.00, 'Grande')
prato = Prato('Camarão', 45.99,'ótimo prato' )
sobremesa = Sobremesa('Paleta Italiana', 49.90, 'doce italiano', 'Grande', 'Delicioso sorvete de chocolate' )

bebida_suco.aplicar_desconto()
prato.aplicar_desconto()
sobremesa.aplicar_desconto()

restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato)
restaurante_praca.adicionar_no_cardapio(sobremesa)




def main():
    print(bebida_suco)
    print(prato)
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':  
    main()