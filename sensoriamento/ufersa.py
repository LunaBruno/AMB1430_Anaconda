from predio import Predio


class Ufersa:
    """ Classe de caracterização e leitura das variáveis ambientais da UFERSA """

    def __init__(self):
        self._predios = []

    def cadastrar_predio(self, id_predio: str):
        self._predios.append(Predio(id_predio))

    def id_predios(self) -> list:
        return [predio.id() for predio in self._predios]

    def cadastrar_sala(self, id_predio: str, id_sala: str, comprimento: float, largura: float) -> None:
        # Buscar o indice do elemento id_predio na lista
        lista_de_predios = self.id_predios()
        indice = [lista_de_predios.index(predio) for predio in lista_de_predios if predio == id_predio][0]
        # Cadastrar sala no predio
        self._predios[indice].cadastrar_sala(id_sala, comprimento, largura)

    def id_salas(self) -> list:
        return [predio.id_salas() for predio in self._predios]

    def larguras(self) -> list:
        return [predio.larguras() for predio in self._predios]

    def comprimentos(self) -> list:
        return [predio.comprimentos() for predio in self._predios]

    def temperaturas(self) -> list:
        return [predio.temperaturas() for predio in self._predios]

    def umidades(self) -> list:
        return [predio.umidades() for predio in self._predios]
