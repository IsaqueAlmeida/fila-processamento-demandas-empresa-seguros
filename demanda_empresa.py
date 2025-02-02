class Item:
    # inserindo um item em uma lista
    def __init__(self, valor=None, proximo=None):
        self.valor = valor
        self.proximo = proximo

    def __repr__(self):
        return '%s, %s' % (self.valor, self.proximo)


class Fila:
    # Constroi uma fila usando listas encadeadas

    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def __repr__(self):
        return str(self.primeiro)

    def push(self, valor):
        # adicionando itens a fila
        item = Item(valor)

        # verificando se existe um item na lista
        if self.primeiro:
            # o valor do último item atual, recebe o valor atual de
            self.ultimo.proximo = item

            # todo objeto item recebe o item a se a lista estiver vazia, então
            self.ultimo = item
        else:
            self.primeiro = item  # o item atual se torna o primeiro
            self.ultimo = item  # o item atual também se torna o último item

    def pop(self):
        # remove o item da lista
        self.primeiro = self.primeiro.proximo


def main():
    # função principal
    # instancia uma nova fila
    fila = Fila()

    # adicionando itens
    fila.push(1)
    fila.push(2)
    fila.push(3)

    print(fila)

    # removendo itens
    fila.pop()
    print(fila)


# executando a função principal
if __name__ == '__main__':
    main()
