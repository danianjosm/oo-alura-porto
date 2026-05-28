from modelos.restaurante import Restaurante

restaurante_praca = Restaurante("praça", "Gourmet")
restaurante_praca.receber_avaliacao("joão", 9)
restaurante_praca.receber_avaliacao("dani", 10)
restaurante_praca.receber_avaliacao("gi", 7)


def main():
    Restaurante.listar_restaurantes()


if __name__ == "__main__":
    main()
