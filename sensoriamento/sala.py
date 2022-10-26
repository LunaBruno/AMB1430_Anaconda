from sensor_temperatura import SensorTemperatura
from sensor_umidade import SensorUmidade


class Sala:
    """ Classe de caracterização e leitura das variáveis ambientais da sala de aula """

    def __init__(self, id_sala: str, largura: float, comprimento: float):
        self._id_sala = id_sala
        self._largura = largura
        self._comprimento = comprimento
        self._temperatura = SensorTemperatura()
        self._umidade = SensorUmidade()

    def id(self) -> str:
        return self._id_sala

    def largura(self) -> float:
        return self._largura

    def comprimento(self) -> float:
        return self._comprimento

    def area(self) -> float:
        return self._largura * self._comprimento

    def temperatura(self) -> float:
        return self._temperatura.temperatura()

    def umidade(self) -> float:
        return self._umidade.umidade()
