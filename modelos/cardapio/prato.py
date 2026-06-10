from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio): # essa classe prato vai herdar metodo atributos de outra classe 
    def __init__(self, nome, preco, descricao):
        super().__init__(nome,preco)
        self.descricao = descricao
    
    def __str__(self):
        return self._nome