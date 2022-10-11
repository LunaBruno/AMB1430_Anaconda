from sala import SalaDeAula


class Predio:
    """ Classe de caracterização e leitura das variáveis ambientais do prédio """

    def __init__(self, id_predio: int):
        self._id_predio = id_predio
        self._salas = []

    def cadastrar_sala(self, id_sala: int, largura: float, comprimento: float):
        self._salas.append(SalaDeAula(id_sala, largura, comprimento))

    def temperatura_sala(self, id_sala: int) -> float:
        return self._salas[id_sala].temperatura()
