from sala import Sala


class Predio:
    """ Classe de caracterização e leitura das variáveis ambientais do prédio """

    def __init__(self, id_predio: str):
        self._id_predio = id_predio
        self._salas = []

    def id(self) -> str:
        return self._id_predio

    def cadastrar_sala(self, id_sala: str, largura: float, comprimento: float):
        self._salas.append(Sala(id_sala, largura, comprimento))

    def id_salas(self) -> list:
        return [sala.id() for sala in self._salas]

    def larguras(self) -> list:
        return [sala.largura() for sala in self._salas]

    def comprimentos(self) -> list:
        return [sala.comprimento() for sala in self._salas]

    def areas(self) -> list:
        return [sala.area() for sala in self._salas]

    def temperaturas(self) -> list:
        return [sala.temperatura() for sala in self._salas]

    def umidades(self) -> list:
        return [sala.umidade() for sala in self._salas]
