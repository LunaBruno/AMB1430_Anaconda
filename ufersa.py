from predio import Predio


class Ufersa:
    """ Classe de caracterização e leitura das variáveis ambientais da UFERSA """

    def __init__(self):
        self._predios = []

    def cadastrar_predio(self, id_predio: int):
        self._predios.append(Predio(id_predio))

    def cadastrar_sala(self, id_predio: int, id_sala: int, comprimento: float, largura: float):
        self._predios[id_predio].cadastrar_sala(id_sala, comprimento, largura)

    def temperatura_sala(self, id_predio: int, id_sala: int) -> float:
        return self._predios[id_predio].temperatura_sala(id_sala)
