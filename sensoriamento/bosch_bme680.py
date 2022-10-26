from requests import get
from bs4 import BeautifulSoup
from random import uniform


class BME680:
    """ Classe de emulação do sensor ambiental Bosch BME680
        https://www.bosch-sensortec.com/products/environmental-sensors/gas-sensors/bme680/ """

    def __init__(self):
        self._temperatura = 0.0
        self._umidade = 0.0

    def medir_temperatura(self) -> float:
        """ Umidade medida na estação meteorológica da Usina Fotovoltaica de Solo UFERSA Mossoró """

        # # Copiar conteúdo da página Climatempo para as condições ambientais do aeroporto de Mossoró
        # html = get('https://www.climatempo.com.br/previsao-do-tempo/aeroporto/347/aeroportodemossoro-rn').content
        # soup = BeautifulSoup(html, 'html.parser')
        # # Selecionar temperatura na página
        # self._temperatura = soup.find(id='momento-temperatura')
        # # Remover o simbolo de graus da string (text[:-1])
        # # Converter a string de temperatura para um número do tipo ponto flutuante
        # # Adicionar a incerterza no intervalo [-1;1]
        # self._temperatura = float(self._temperatura.text[:-1]) + uniform(-0.5, 0.5)

        # Emulacao da temperatura
        self._temperatura = 28 + uniform(-0.5, 0.5)
        # Retornar o valor de temperatura
        return self._temperatura

    def medir_umidade(self) -> float:
        """ Temperatura medida na estação meteorológica da Usina Fotovoltaica de Solo UFERSA Mossoró """

        # # Copiar conteúdo da página Hobolink para as condições ambientais em Mossoró
        # html = get('https://hobolink.com/p/7ecfd5f9f91512d3644c9ab924e1ade7').content
        # soup = BeautifulSoup(html, 'html.parser')
        # # Selecionar umidade na página
        # self._umidade = soup.select('#hobolink-latest-conditions-form\:conditions-tree\:0_1\:j_idt90 > div > span.latest-conditions-info-reading > nobr')
        # self._umidade = str(self._umidade).split('</nobr>')
        # self._umidade = self._umidade[0].split('<nobr>')[1]
        # # Converter a string de umidade para um número do tipo ponto flutuante
        # # Adicionar a incerterza no intervalo [-1;1]
        # self._umidade = float(self._umidade) + uniform(-0.5, 0.5)

        # Emulacao da temperatura
        self._umidade = 60 + uniform(-0.5, 0.5)
        # Retornar o valor de umidade
        return self._umidade
