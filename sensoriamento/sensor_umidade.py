from bosch_bme680 import BME680


class SensorUmidade(BME680):
    """ Subclasse (herança) de leitura da umidade medida pelo sensor Bosch BME680 """

    def __init__(self):
        BME680.__init__(self)

    def umidade(self) -> float:
        return self.medir_umidade()


