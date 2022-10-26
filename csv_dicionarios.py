"""
    LEITURA E ESCRITA DE ARQUIVOS CSV

    O chamado formato CSV (Comma Separated Values) é o formato mais comum de importação e exportação
    de planilhas e bancos de dados. O formato CSV foi usado por muitos anos antes das tentativas de
    descrever o formato de maneira padronizada em RFC 4180.

    O módulo csv implementa classes para ler e gravar dados tabulares no formato CSV.
    Ele permite que os programadores digam “escreva esses dados no formato preferido
    pelo Excel” ou “leia os dados desse arquivo gerado pelo Excel”, sem conhecer os
    detalhes precisos do formato CSV usado pelo Excel. Os programadores também podem
    descrever os formatos CSV entendidos por outros aplicativos ou definir seus próprios
    formatos CSV para fins especiais.

    Os objetos de reader e writer do módulo csv leem e escrevem sequências. Os programadores
    também podem ler e gravar dados no formato de dicionário usando as classes DictReader e DictWriter.

    https://docs.python.org/pt-br/3/library/csv.html


    DICIONÁRIOS

    Outra estrutura de dados muito útil embutida em Python é o dicionário, cujo tipo é dict. Dicionários são
    também chamados de “memória associativa” ou “vetor associativo” em outras linguagens. Diferente de sequências
    que são indexadas por inteiros, dicionários são indexados por chaves (keys), que podem ser de qualquer tipo
    imutável (como strings e inteiros).

    Um bom modelo mental é imaginar um dicionário como um conjunto não-ordenado de pares chave:valor, onde as
    chaves são únicas em uma dada instância do dicionário. Dicionários são delimitados por chaves: {}, e contém uma
    lista de pares chave:valor separada por vírgulas. Dessa forma também será exibido o conteúdo de um dicionário
    no console do Python. O dicionário vazio é {}.

    As principais operações em um dicionário são armazenar e recuperar valores a partir de chaves. Também é possível
    remover um par chave:valor com o comando del. Se você armazenar um valor utilizando uma chave já presente, o
    antigo valor será substituído pelo novo. Se tentar recuperar um valor usando uma chave inexistente, será gerado
    um erro.

    https://docs.python.org/pt-br/3/tutorial/datastructures.html#dictionaries
"""

import csv


# Abrir arquivo CSV para escrita de dicionários
with open('dicionario.csv', mode='w', newline='', encoding='utf-8') as arquivo_csv:
    # Criar lista de colunas a ser gravada no arquivo CSV
    cabecalho = ['predio', 'sala', 'largura', 'comprimento', 'temperatura', 'umidade']

    # Criar o objeto de dados separados por virgula
    dados_csv = csv.DictWriter(arquivo_csv, fieldnames=cabecalho)

    # Gravar lista de colunas no arquivo CSV
    dados_csv.writeheader()

    # Criar dicionário de dados a ser gravado no arquivo CSV
    dicionario = {'predio': 'Laboratório de Ciências da Computação',
                  'sala': 'Laboratorio de Informática 5',
                  'largura': 5.0,
                  'comprimento': 5.5,
                  'temperatura': 25.0,
                  'umidade': 70.0}

    # Escrever o dicionário no arquivo
    dados_csv.writerow(dicionario)

    # Criar dicionário de dados a ser gravado no arquivo CSV
    dicionario = {'predio': 'Central de Aulas 6',
                  'sala': 'Sala 2',
                  'largura': 6.0,
                  'comprimento': 7.0,
                  'temperatura': 23.0,
                  'umidade': 60.0}

    # Escrever o dicionário no arquivo
    dados_csv.writerow(dicionario)

    # Criar dicionário de dados a ser gravado no arquivo CSV
    dicionario = {'predio': 'Palácio das Carnaúbas',
                  'sala': 'Sala da Reitoria',
                  'largura': 10.0,
                  'comprimento': 10.0,
                  'temperatura': 20.0,
                  'umidade': 50.0}

    # Escrever o dicionário no arquivo
    dados_csv.writerow(dicionario)


# Abrir arquivo CSV para leitura de dicionários
with open('dicionario.csv', mode='r', newline='', encoding='utf-8') as arquivo_csv:
    # Criar o objeto de dados separados por virgula
    dados_csv = csv.DictReader(arquivo_csv)

    # Ler os dados do objeto linha por linha e retornar um dicionário para cada linha
    for dados in dados_csv:
        print(dados)
