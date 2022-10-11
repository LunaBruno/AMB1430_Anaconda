from pt100 import PT100


class SensorDeTemperatura(PT100):
    """ Subclasse (herança) de leitura da temperatura medida pelo sensor PT100 """

    def __init__(self):
        PT100.__init__(self)

    def temperatura(self) -> float:
        return self.medir_temperatura()
