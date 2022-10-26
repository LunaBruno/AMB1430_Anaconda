from bosch_bme680 import BME680


class SensorTemperatura(BME680):
    """ Subclasse (herança) de leitura da temperatura medida pelo sensor Bosch BME680 """

    def __init__(self):
        BME680.__init__(self)

    def temperatura(self) -> float:
        return self.medir_temperatura()
