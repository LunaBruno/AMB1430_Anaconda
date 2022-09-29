"""

CRUZAMENTO POR ZERO (DETECÇÃO)

    A detecção de cruzamento por zero permite estimar o período e a frequência de uma forma de onda periódica. Este arquivo
    consiste na descrição dos seguintes blocos de código:

        Bloco de simulação da forma de onda senoidal
            Geração dos instantes de tempo das amostras da forma de onda senoidal
            Cálculo da amplitude da forma de onda senoidal nos instantes de tempo da amostras
        
        Bloco de detecção de cruzamento por zero
            Identificação do sinal da forma de onda (positivo ou negativo)
            Detecção de cruzamento por zero
                Subtração dos elementos adjacentes da lista de sinal (f[n+1] - f[n])
                Identificação das posições com resultados diferentes de zero

"""

# Importar funções da biblioteca padrão
from math import pi, sin, radians

# Importar funções da biblioteca
from matplotlib import use
from matplotlib import pyplot as plt

"""           
    SIMULAÇÃO DA FORMA DE ONDA PERIÓDICA SENOIDAL
 
        Geração dos instantes de amostragem (t) da forma de onda senoidal
    
            t = [0*h, 1*h, 2*h, 3*h, 4*h, 5*h, 6*h, 7*h, 8*h, 9*h, ..., n*h]
    
            t : lista de instantes de tempo de amostragem em segundos
            h : período de amostragem ou passo de cálculo em segundos
            n : indice da última amostra da lista de instantes de tempo de amostragem
                e represemta o número de amostras:
            
            n = (intervalo de tempo de simulação / periodo de amostragem)
    
            Exemplo:
            
                intervalo de tempo de simulação = 1.0 s
                passo de cálculo = 0.1 s
                numero de amostras (n) = 1.0 / 0.1 = 10
    
                h = 0.1
                t = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
"""

# Geração dos instantes de amostragem
# Intervalo entre 0 e 1.55 períodos da forma de onda soindal (50Hz) com período de amostragem de 0.001s
tempo_de_simulacao = 1.55 * (1 / 50.0)
periodo_de_amostragem = 0.001
numero_de_amostras = int(tempo_de_simulacao/periodo_de_amostragem)
t = [periodo_de_amostragem * numero_da_amostra for numero_da_amostra in range(numero_de_amostras)]

# Apresentação dos instantes de amostragem
print('\n Instante de tempo da amostra    = ', end='')
for instante_da_amostra in t:
    print(f'{instante_da_amostra:05.4f} ', end='')

"""
    Determinação da amplitude da forma de onda f(t) no instante de amostragem
        
        f(t) = amplitude * sin( 2 * pi * frequencia * t + fase)
        
        Exemplo:        
            
            amplitude = 10
            frequencia = 50
            fase = 0
            
            f(t) = amplitude * sin( 2 * pi * frequencia * t + fase)
            t = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
        
            f(t) = [f(0.0), f(0.1), ..., f(0.9)]
                f(0.0) = 10.0 * sin( 2 * pi * 50 * 0.0 + 0.0) =  0.00 
                f(0.1) = 10.0 * sin( 2 * pi * 50 * 0.1 + 0.0) =  3.09
                ...
                f(0.9) = 10.0 * sin( 2 * pi * 50 * 0.9 + 0.0) = -3.09
"""

# Atribuição dos parâmetros da forma de onda senoidal
senoide = []
amplitude = 10
frequencia = 50
fase = 0

# Calculo o valor da forma de onda nos instantes de amostragem
for instante_de_amostragem in t:
    senoide.append(amplitude * sin( 2 * pi * frequencia * instante_de_amostragem + radians(fase)))

# Apresentação das amplitudes da senoide nos instantes de amostragem
print('\n Amplitude da onda senoidal      = ', end='')
for amplitude_da_amostra in senoide:
    print(f'{amplitude_da_amostra:6.2f} ', end='')

"""
    DETECÇAO DE CRUZAMENTO POR ZERO

        Identificação do sinal da amplitude da forma de onda f(t) nos instantes de amostragem
    
            sinal(f) =  1 se f(t) > 0
                       -1 se f(t) < 0
"""

# Lista de armazenamento dos sinais das amostras da forma de onda senoidal
sinal = []

# Determinação o sinal da forma de onda a partir da amplitude calculada no instante de amostragem
for amplitude in senoide:
    if amplitude > 0.0:
        sinal.append(1.0)
    else:
        sinal.append(-1.0)

# Apresentação do sinal da amplitude da forma de onda senoidal
print('\n Sinal da forma de onda senoidal = ', end='')
for sinal_da_amostra in sinal:
    print(f'{sinal_da_amostra:6.0f} ', end='')

"""
    Determinação os instantes de mudança de sinal

        cross(f) =  f[n + 1] - f[n], onde n é indice da amostra 
        cross(f) : 0 se nao ocorrer mudanca de sinal (cruzamento por zero)
                   2 se ocorrer mudanca de sinal
"""

# Lista de armazenamento das detecções de cruzamentos por zero das amostras da forma de onda senoidal
cruzamento_por_zero = []

# Detecção do cruzamento por zero através da diferença entre amostras adjacentes (f[n + 1] - f[n])
ultimo_sinal_da_amostra = -1.0
for sinal_da_amostra in sinal:
    cruzamento_por_zero.append(sinal_da_amostra - ultimo_sinal_da_amostra)
    ultimo_sinal_da_amostra = sinal_da_amostra

# Apresentação da detecção de cruzamento por zero (valores diferentes de zero)
print('\n Detecção do cruzamento por zero = ', end='')
for amplitude_da_amostra in cruzamento_por_zero:
    print(f'{amplitude_da_amostra:6.0f} ', end='')

"""            
    Apresentação dos resultados através da biblioteca matplotlib
    
    Instalacao da biblioteca matplotlib
        https://matplotlib.org/stable/index.html
    
    Exemplo de uso do pyplot
        https://matplotlib.org/stable/plot_types/basic/index.html
        https://matplotlib.org/stable/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py
    
    Matplotlib cheatsheets and handouts
        https://matplotlib.org/cheatsheets/
"""

# Criacao da figura
use('TkAgg')
plt.figure()

# Apresentação os instantes de amostragem e os valores calculados para o seno
plt.subplot(411)
plt.stem(t, senoide, 'b--')
plt.grid(color='0.90')

# Apresentação forma de onda senoidal interpolada entre as amostras
plt.subplot(412)
plt.plot(t, senoide, 'bo')
plt.plot(t, senoide, 'r--')
plt.grid(color='0.90')

# Apresentação sobreposicao das formas de onda
plt.subplot(413)
plt.plot(t, sinal, 'bo')
plt.plot(t, sinal, 'r--')
plt.grid(color='0.90')

plt.subplot(414)
plt.plot(t, cruzamento_por_zero, 'bo')
plt.plot(t, cruzamento_por_zero, 'r--')
plt.grid(color='0.90')

# Formatacao da figura
plt.xlabel('Tempo (s)')
# Apresentar gráfico
plt.show()
