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
"""

import csv


# Abrir arquivo CSV para escrita de listas
with open('lista.csv', mode='w', newline='', encoding='utf-8') as arquivo_csv:
    # Criar o objeto de dados separados por virgula
    dados_csv = csv.writer(arquivo_csv)

    # Criar lista de colunas a ser gravada no arquivo CSV
    cabecalho = ['predio', 'sala', 'largura', 'comprimento', 'temperatura', 'umidade']
    dados_csv.writerow(cabecalho)

    # Criar lista de dados a ser gravada no arquivo CSV
    lista = ['Laboratório de Ciências da Computação', 'Laboratorio de Informática 3', 5.0, 5.5, 25.0, 70.0]
    # Escrever os dados no arquivo
    dados_csv.writerow(lista)

    # Criar lista de dados a ser gravada no arquivo CSV
    lista = ['Central de Aulas 6', 'Sala 2', 6.0, 7.0, 23.0, 60.0]
    dados_csv.writerow(lista)

    # Criar lista de dados a ser gravada no arquivo CSV
    lista = ['Palácio das Carnaúbas', 'Sala da Reitoria', 10.0, 10.0, 20.0, 50.0]
    dados_csv.writerow(lista)

    lista = ['Engenharias', 'Teto', 100.0, 1.0, 45.0, 10]
    dados_csv.writerow(lista)


# Abrir arquivo CSV para leitura de listas
with open('lista.csv', mode='r', newline='', encoding='utf-8') as arquivo_csv:
    # Criar o objeto de dados separados por virgula
    # dados_csv = csv.reader(arquivo_csv)
    dados_csv = csv.DictReader(arquivo_csv)

    # Ler os dados do objeto linha por linha e retornar uma lista para cada linha
    for dados in dados_csv:
        print(dados)
