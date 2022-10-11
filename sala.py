from sensor import SensorDeTemperatura


class SalaDeAula:
    """ Classe de caracterização e leitura da temperatura ambiente da sala de aula """

    def __init__(self, id_sala: int, largura: float = 1.0, comprimento: float = 1.0):
        self._id_sala = id_sala
        self._largura = largura
        self._comprimento = comprimento
        self._sensor = SensorDeTemperatura()

    def temperatura(self) -> float:
        return self._sensor.temperatura()
