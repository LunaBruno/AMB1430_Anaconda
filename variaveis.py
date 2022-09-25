"""

MODELO DE DADOS
OBJETOS, VALORES E TIPOS

    Objetos são abstrações do Python para dados.
    Todos dados em um programa Python são representados por objetos ou por relações entre objetos.

    Todos os objetos tem uma identidade, um tipo e um valor.
    A identidade de um objeto nunca muda depois de criado.
    Você pode pensar nisso como endereço de objetos em memória.
    A função id() retorna um inteiro representando sua identidade.
    Para CPython, id(x) é o endereço de memória em que x é armazenado.

    O tipo de um objeto determina as operações que o objeto suporta e também define os valores
    possíveis para objetos desse tipo.
    A função type() retorna o tipo de um objeto

    O valor de alguns objetos pode mudar.
    Objetos cujos valores podem mudar são descritos como mutáveis,
    Objetos cujo valor não pode ser mudado uma vez que foram criados são chamados imutáveis

A HIERARQUIA DE TIPOS PADRÃO

    O Python distingue entre inteiros, números de ponto flutuante e números complexos. Eles são criados por literais
    numéricos e retornados como resultados por operadores aritméticos e funções aritméticas integradas. Os números do
    Python são, obviamente, fortemente relacionados aos números matemáticos, mas sujeitos às limitações da representação
    numérica em computadores.

        Integers (int)
            Eles representam números em um intervalo ilimitado, sujeito apenas à memória (virtual) disponível.
            Para o propósito de operações de deslocamento e máscara, uma representação binária é assumida e os
            números negativos são representados em uma variante do complemento de 2 que dá a ilusão de uma string
            infinita de bits de sinal estendendo-se para a esquerda.

        Booleanos (bool)
            Estes representam os valores da verdade Falsos e Verdadeiros. O tipo booleano é um subtipo do tipo inteiro,
            e os valores booleanos se comportam como os valores 0 e 1, respectivamente, em quase todos os contextos,
            com exceção de que, quando convertidos em uma string, as strings "False" ou "True" são retornados,
            respectivamente.

        numbers.Real (float)
            Eles representam números de ponto flutuante de precisão dupla no nível da máquina. Você está à mercê
            da arquitetura da máquina subjacente (e implementação C ou Java) para o intervalo aceito e tratamento
            de estouro. Python não oferece suporte a números de ponto flutuante de precisão única.

        numbers.Complex (complex)
            Eles representam números complexos como um par de números de ponto flutuante de precisão dupla no
            nível da máquina. As mesmas advertências se aplicam aos números de ponto flutuante.

    As sequëncias representam conjuntos ordenados finitos indexados por números não negativos. A função embutida len()
    retorna o número de itens de uma sequência. Quando o comprimento de uma sequência é n, o conjunto de índices
    contém os números 0, 1, …, n-1. O item i da sequência a é selecionado por a[i].

    Sequências também suportam fatiamento: a[i:j] seleciona todos os itens com índice k de forma que i <= k < j.
    Quando usada como expressão, uma fatia é uma sequência do mesmo tipo. Isso implica que o conjunto de índices é
    renumerado para que comece em 0.

    As sequências são distinguidas de acordo com sua mutabilidade (Um objeto de um tipo de sequência imutável não pode
    ser alterado depois de criado)

    Sequências imutáveis
        Strings
            Uma string é uma sequência de valores que representam pontos de código Unicode. Todos os pontos de código
            no intervalo U+0000 - U+10FFFF podem ser representados em uma string. Python não tem um tipo char; em vez
            disso, cada ponto de código na string é representado como um objeto string com comprimento 1. A função
            embutida ord() converte um ponto de código de sua forma de string para um inteiro no intervalo 0 - 10FFFF;
            chr() converte um inteiro no intervalo 0 - 10FFFF para o objeto de string correspondente de comprimento 1.
            str.encode() pode ser usado para converter uma str para bytes usando a codificação de texto fornecida,
            e bytes.decode() pode ser usado para conseguir o oposto.

        Tuplas
            Os itens de uma tupla são objetos Python arbitrários. Tuplas de dois ou mais itens são formadas por listas
            de expressões separadas por vírgulas. Uma tupla de um item (um “singleton”) pode ser formada afixando uma
            vírgula a uma expressão (uma expressão por si só não cria uma tupla, já que os parênteses devem ser usados
            para agrupamento de expressões). Uma tupla vazia pode ser formada por um par vazio de parênteses.

        Bytes
            Um objeto bytes é um vetor imutável. Os itens são bytes de 8 bits, representados por inteiros no intervalo
            0 <= x < 256. Literais de bytes (como b'abc') e o construtor embutido bytes() podem ser usados para criar
            objetos bytes. Além disso, os objetos bytes podem ser decodificados em strings através do método decode().

    Sequências mutáveis
        Listas
            Os itens de uma lista são objetos Python arbitrários. As listas são formadas colocando uma lista separada
            por vírgulas de expressões entre colchetes. (Observe que não há casos especiais necessários para formar
            listas de comprimento 0 ou 1.)

        Vetores de bytes
            Um objeto bytearray é um vetor mutável. Eles são criados pelo construtor embutido bytearray(). Além de
            serem mutáveis (e, portanto, inalteráveis), os vetores de bytes fornecem a mesma interface e funcionalidade
            que os objetos imutáveis bytes.

        O módulo de extensão array fornece um exemplo adicional de um tipo de sequência mutável.

    https://docs.python.org/pt-br/3/reference/datamodel.html


FUNÇÕES EMBUTIDAS

    O interpretador do Python possui várias funções e tipos embutidos que sempre estão disponíveis.
    Observar a lista de todas as funções embutidas.

    https://docs.python.org/pt-br/3/library/functions.html

"""

# Variável inteira
variavel_inteira = 10

# Variavel ponto flutuante
variavel_ponto_flutuante = 1.0

# Variavel complexa
# j representa a parte complexa do número
variavel_complexa = 10.0 + 10.0j

# Tipo, valor e endereço de memória em que a variável é armazenada
print(f"""
    variavel_inteira
      Tipo - {type(variavel_complexa)}
      Endereço - {id(variavel_complexa)}
      Valor - {variavel_complexa}""")

# String
string_imutavel = "texto da string"

# Tupla
tupla_imutavel = (1, 2)

# Bytes
bytes_imutavel = b'sequencia de bytes imutaveis'

# Lista
lista_mutavel = [1, 2, 4, 5, 6, 7]

# Lista de bytes
lista_bytes_mutavel = []

# Apresentar as funções embutidas para uma variavel inteira
print(dir(variavel_inteira))
