from requests import get
from bs4 import BeautifulSoup
"""
Requests
    Documentaoão
        https://requests.readthedocs.io/en/latest/user/quickstart/
    Instalação
        pip install requests

BeautifulSoup
    Documentaoão
        https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    Instalação      
        pip install beautifulsoup4
"""
from random import uniform
"""           
Distribuições com valor real
    random.uniform(a, b)
        Retorna um número de ponto flutuante aleatório N de forma
        que a <= N <= b para a <= b e b <= N <= a para b < a.
        O valor do ponto final b pode ou não ser incluído no intervalo,
        dependendo do arredondamento do ponto flutuante na equação a + (b-a) * random().
        
        https://docs.python.org/pt-br/3/library/random.html
"""


class PT100:
    """ Classe de emulação do sensor de temperatura PT100 """

    def __init__(self):
        self._temperatura = 0.0

    def medir_temperatura(self) -> float:
        """ Emulação da medição de temperatura através do sensor PT100

            Temperatura ambiente calculada no intervalo entre -0.5 a +0.5 graus
            sobre o valor médio obtido através do Climatempo para o aeroporto de Mossoró

            Args:
                (None)
            Returns:
                temperatura (float): temperatura emulada do sensor pt100
        """
        # Copiar conteúdo da página Climatempo para as condições ambientais no aeroporto de Mossoró
        html = get('https://www.climatempo.com.br/previsao-do-tempo/aeroporto/347/aeroportodemossoro-rn').content
        soup = BeautifulSoup(html, 'html.parser')
        # Selecionar temperatura na página
        self._temperatura = soup.find(id='momento-temperatura')
        # Remover o simbolo de graus da string (text[:-1])
        # Converter a string de temperatura para um número do tipo ponto flutuante
        # Adicionar a incerterza no intervalo [-1;1]
        self._temperatura = float(self._temperatura.text[:-1]) + uniform(-0.5, 0.5)
        # Retornar o valor de temperatura
        return self._temperatura
