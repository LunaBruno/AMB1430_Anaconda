"""

CLASSES

    Classes proporcionam uma forma de organizar dados e funcionalidades juntos. Criar uma nova classe cria um novo “tipo”
    de objeto, permitindo que novas “instâncias” desse tipo sejam produzidas. Cada instância da classe pode ter atributos
    (variáveis ou características) anexados a ela, para manter seu estado. Instâncias da classe também podem ter métodos
    (funções definidas pela classe) para modificar seu estado.

HERANÇA

    Obviamente, uma característica da linguagem não seria digna do nome “classe” se não suportasse herança. A execução
    de uma definição de classe derivada procede da mesma forma que a de uma classe base. Quando o objeto classe é
    construído, a classe base é lembrada. Isso é utilizado para resolver referências a atributos. Se um atributo
    requisitado não for encontrado na classe, ele é procurado na classe base. Essa regra é aplicada recursivamente se
    a classe base por sua vez for derivada de outra.

    https://docs.python.org/pt-br/3/tutorial/classes.html#a-word-about-names-and-objects

"""

# Classe (superclasse)
class Computador:

    def __init__(self, processador: str, memoria: int, armazenamento: int) -> None:
        self._processador = processador
        self._memoria = memoria
        self._armazenamento = armazenamento

    def consultar_processador(self) -> str:
        return self._processador

    def atualizar_processador(self, processador: str) -> None:
        self._processador = processador

    def __str__(self) -> str:
        mensagem = f""" \n Classe Computador
                        \r --
                        \r Processador   : {self._processador}
                        \r Memória       : {self._memoria} GB
                        \r Armazenamento : {self._armazenamento} GB
                    """
        return mensagem

# Herança (subclasse)
class ComputadorGamer(Computador):
    def __init__(self, processador: str, memoria: int, armazenamento: int, placa_de_video: str, memoria_de_video: int) -> None:
        Computador.__init__(self, processador, memoria, armazenamento)
        self._placa_de_video = placa_de_video
        self._memoria_de_video = memoria_de_video

    def __str__(self) -> str:
        mensagem = f""" \n NOVA classe ComputadorGamer (herdou os atributos da classe Computador)
                        \r --
                        \r Processador      : {self._processador}
                        \r Memória RAM      : {self._memoria} GB
                        \r Armazenamento    : {self._armazenamento} GB
                        \r Placa de video   : {self._armazenamento}
                        \r Memória de video : {self._armazenamento} GB
                    """
        return mensagem


# Criação do Objeto a paritr da classe Computador (instanciação)
computador = Computador('Intel® Core™ i3-1215UL ', 4, 128)

# Atualizar atributo através do método da classe Computador
computador.atualizar_processador('Intel® Core™ i5-12600HL')

# Apresentar as caracteristicas do objeto computador (__str__)
print(computador)


# Criação do Objeto a partir da NOVA classe ComputadorGamer (instanciação)
computador_gamer = ComputadorGamer('Intel® Core™ i9-12900K', 64, 512, 'NVIDIA GeForce RTX Serie 40', 12)

# Atualizar atributo através do método da classe Computador (herança)
computador_gamer.atualizar_processador('Intel® Xeon® Platinum 8380')

# Apresentar as caracteristicas do objeto computador_gamer (__str__)
print(computador_gamer)
