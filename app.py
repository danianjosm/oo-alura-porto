from modelos.restaurante import Restaurante

from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante("praça", "Gourmet")
bebida_suco = Bebida("Suco de melancia", 5.0, "grande")
prato_pao = Prato("pão", 2.00, "O melhor pão da cidade")
restaurante_praca.adicionar_nocardapio(bebida_suco)
restaurante_praca.adicionar_nocardapio(prato_pao)


def main():
    restaurante_praca.exibir_cardapio



if __name__ == "__main__":
    main()


