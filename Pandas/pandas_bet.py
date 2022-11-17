"""
    VECENDO AS CASAS DE APOSTAS COM SEUS PRÓPRIOS NÚMEROS E VERIFICANDO COMO O
    MERCADO DE APOSTAS ESPORTIVAS ONLINE É MANIPULADO

    RESUMO

    A indústria de jogos de azar online emprega equipes de analistas de dados para construir modelos de previsão com
    o objetivo de manter as probabilidades dos jogos a seu favor em um mercado ineficiente de apostas em futebol. Esta
    indústria pode ser consistentemente derrotada em milhares de jogos, onde é possível explorar a informação de
    probabilidade implícita nos dados disponíveis publicamente no mercado para encontrar apostas favoráveis para o
    apostador, ou seja, uma estratégia para vencer a casas de apostas com seus próprios números. Com essa abordagem,
    uma estratégia de apostas é proposta para atingir uma precisão de 47,2% e render um retorno de 8.5%.

    ATENCAO: A estratégia apresentada serve apenas para para ilustrar o uso da biblioteca pandas para fins didáticos.

    AVISO: A casa de aposta compensa as ineficiências de mercado com práticas discriminatórias severas contra clientes
    de sucesso, ou seja, a longo prazo o “apostador de sucesso” não pode executar sua estratégia e é “expulso da
    plataforma”. Além disso, não é possível acertar mais do que 47% dos jogos e não é possível manter um retorno maior
    que 8.5%. Neste cenário, a casa de apostas sempre vence, pois o mercado é manipulado para que o apostador nunca
    vença a longo prazo

    ALERTA: Mais de 1.000 jogos têm suspeita de manipulação de resultados em 2022, em mais de 86 países, envolvendo 12
    esportes diferentes. Desse número, mais de 130 partidas são do futebol brasileiro, a maioria em ligas inferiores.

    https://diariodonordeste.verdesmares.com.br/jogada/investigacao-aponta-mais-de-mil-jogos-com-suspeita-de-manipulacao-de-resultados-no-mundo-1.3301653)
    https://www.estadao.com.br/esportes/futebol/manipulacao-resultado-futebol-brasileiro-aposta-esportiva-denuncia/

    INTRODUCAO
    
    Nos últimos anos, o surgimento de tecnologias, plataformas de produtos e direitos de transmissão de TV transformou 
    a indústria de jogos de azar online em um negócio bilionário. Para maximizar o lucro, as casas de apostas empregam 
    equipes de cientistas de dados para analisar décadas de dados esportivos e desenvolver modelos altamente precisos 
    para prever os resultados dos eventos de esporte. Assim, aproveitando a experiência e a qualidade dos dados das 
    casas de apostas, é possível demonstrar que podem ser derrotadas com seus próprios números. 
    
    Uma estratégia de apostas para o mercado de futebol pode explorar a informação implícita contidas nas 
    probabilidades agregadas das casas de apostas para aproveitar sistematicamente eventos mal precificados. Nesta 
    estratégia de apostas, em vez de tentar construir um modelo para competir com experiência de previsão das casas 
    de apostas, utiliza-se as probabilidades disponíveis publicamente (1/odd) como a verdadeira probabilidade de um 
    resultado. Deste modo, busca-se oportunidades de precificação incorreta, ou seja, jogos com cotas oferecidas acima 
    do valor justo estimado. 
    
    A estratégia pode retornar lucros sustentados ao longo de anos de apostas simuladas com dados  históricos. Estes 
    resultados sugerem que as apostas em futebol são ineficientes. As casas de apostas, no entanto, implementam um 
    conjunto especial de regras para compensar para essas ineficiências. Algumas casas de apostas limitam severamente 
    as apostas dos jogadores eficientes, obrigando-os a interromper a estratégia de apostas. É possível demonstrar que 
    o sistema de apostas esportivas online é manipulado contra apostadores bem-sucedidos por meio de práticas 
    discriminatórias. Entretanto, neste cenário, as casas de apostas podem ser derrotadas de forma consistente.

    METODOLOGIA
    
    Para que uma aposta seja justa as cotas pagas pela casa de apostas deve ser o inverso da probabilidade do
    resultado. Uma vez que as casas de apostas podem construir um modelo preciso que estima a probabilidade subjacente 
    do resultado de um jogo e oferecer odds abaixo do valor justo. O mecanismo funciona de forma semelhante à roleta 
    no casino. Por exemplo, quando um cliente faz uma aposta no vermelho em uma roleta americana, há uma 18/38 chance 
    de dobrar a aposta (18 números verdes, 18 números vermelhos, mais 0 e 00, que são verdes). Nestas condições, 
    o justo valor do odd é 2.111 mas a casa paga apenas 2.000 e, portanto, a casa paga abaixo do valor justo. Este é 
    o imposto ou comissão cobrado pela casa de apostas, neste caso, para cada dólar apostado na roleta, a casa
    espera ganhar $ (2/38), ou 5.3 centavos.
    
    Para calcular as probabilidades que permitirão às casas de apostas ganhar a porcentagem desejada de dinheiro 
    apostado em jogos esportivos, eles precisam de modelos precisos para estimar a probabilidade de cada evento. 
    Existem muitos fatores diferentes que podem ser incorporados em um modelo para prever a probabilidade do resultado 
    de um jogo de futebol, por exemplo: os resultados dos últimos jogos para as duas equipes, o recorde de jogos 
    bem-sucedidos em casa ou fora dessas equipes, o número de gols marcados e sofridos por cada equipe durante os 
    jogos anteriores, lesões de jogadores antes do jogo e até mesmo as condições climáticas esperadas no dia da partida. 
    
    Se considerarmos o escopo dessas variáveis, a tarefa de desenvolver modelos precisos para prever o resultado de 
    milhares de jogos no futebol ligas ao redor do mundo torna-se um desafio extremamente complexo. Nos últimos anos, 
    porém, equipes de analistas profissionais melhoraram os resultados de seus modelos de previsão com análise 
    estatística cada vez mais sofisticada e grandes quantidades de dados em várias formas.
    
    Para quantificar a capacidade preditiva dos modelos das casas de apostas, realiza-se a análise histórica de 
    resultados de jogos de futebol. Desta forma observa-se as probabilidades históricas dos jogos de futebol de janeiro 
    2005 a junho de 2015 em portais esportivos online disponíveis na Internet. No total, analisou-se 479.440 jogos 
    de 818 ligas e divisões em todo o mundo. Assim, para medir a precisão das casas de apostas em estimar as 
    probabilidades (1/odd) do resultado de um jogo, calculou-se a média das probabilidades da seguinte forma:
    
    P_media = 1/ média(Ω) 

    (Como converter odds em probabilidades: 1 dividido pelas odd decimal e multiplicado por 100 resultará 
    em uma porcentagem. Por exemplo, odd decimal de 2 = (1/2) x 100 = 50%. 
    P_media_%_de_um_resultado = 100 / media_das_odds_de_um_resultado )
    
    onde Ω é um conjunto contendo as odds das casas de apostas para um determinado resultado (vitória do time da casa, 
    empate, vitória do time visitante). Desta forma, calculou-se a probabilidade de uma vitória do time da casa, um 
    empate ou uma vitória do time visitante para cada dos 479.440 jogos (no total 3 x 479.440 probabilidades). 
    Em seguida, agrupou-se os dados de acordo com a média das probabilidades entre 0 e 1 em passos de 0,0125. 
    
    Baseado nesses resultados, foi desenvolvida uma estratégia de apostas sobre a evidência de que as casas de 
    apostas já possuem modelos altamente precisos para prever os resultados dos jogos de futebol. Lembrando que uma 
    estratégia destinada a vencer as casas de apostas na previsão do resultado dos jogos esportivos requer uma modelo 
    mais preciso do que os que as casas de apostas desenvolveram ao longo de muitos anos de dados coleta e análise. 
    Assim, em vez de tentar criar tal modelo, é possível usar a estimativas das próprias casas de apostas dos 
    resultados para encontrar oportunidades de preços incorretos. Mais especificamente, procurar oportunidades de 
    probabilidades oferecidas acima de sua estimativa valor justo. 
    
    Às vezes, as casas de apostas oferecem cotas acima do valor justo para competir para atrair clientes ou 
    para manter um equilibrado para evitar ficar excessivamente exposto ao risco. Por exemplo, quando muito 
    muitos clientes apostam em um resultado (vitória do time da casa) as casas de apostas podem aumentar as 
    chances de outro resultado (vitória da equipe visitante), a fim de atrair mais jogadores para apostar nele 
    e diminuir sua exposição. Isso significa que as casas de apostas podem oferecer uma probabilidade implícita 
    (1/odd) menor do que a probabilidade real de um resultado. Este é o fator-que pode ser explorado na estratégia.
    
    P_real ≃ P_media – α
    
    onde α é o termo de ajuste que nos permite incluir a análise de regressão sobre os resultados dos jogos. 
    Nessas condições, é possível fazer uma aposta quando o retorno esperado for maior que 0, ou seja, quando:
    
    Ω > 1/ (P_media − α) 
    
    Este raciocínio é utilizado definir a estratégia de aposta sempre que as odds máximas oferecidas para um 
    determinado resultado cumprem a seguinte desigualdade:
    
    máx(Ω) > 1 / (P_media − 0,05)
    
    O valor esperado de cada aposta aumenta com o parâmetro α, enquanto o número de jogos disponível para apostas 
    diminui. Isso ocorre porque a condição se torna mais rigorosa e menos casas de apostas oferecem probabilidades 
    altas. Assumindo α igual a 0,05 obtém-se o retorno ideal (5%) com a maior quantidade de jogos (um α de 0,06, 
    por exemplo, igualmente lucrativo, mas α igual a 0,05 ofereceu o dobro de jogos para apostar, o que pode ser 
    útil em uma estratégia que aumenta o valor apostado em função dos ganhos). 
    
    Em resumo, a estratégia de apostas supõe que as probabilidades publicadas por as casas de apostas permitem 
    obter uma estimativa altamente precisa da probabilidade real do resultado de um evento (calculando o inverso 
    das probabilidades médias entre as casas de apostas menos um constante equivalente a comissão da casa de apostas). 
    Assim, a estratégia de apostas consiste em fazer apostas sempre que as odds oferecidas por alguma casa de 
    apostas desviar da média e acima do valor justo, ou seja, quando o retorno esperado da aposta for positivo. 
    É importante notar que a tarefa de identificar as chances que satisfizeram o limite não exigia um modelo 
    com maior precisão do que os modelos das casas de apostas.

    RESULTADOS

    O mercado de apostas online de futebol é ineficiente pois a estratégia foi capaz de obter lucros sustentados ao
    longo dos anos com dados históricos. Na prática, porém, a ineficiência do mercado de apostas em futebol foi
    compensada pelas práticas restritivas das casas de apostas. Embora as atividades de apostas fossem legais e
    conduzidas de acordo com regras das casas de apostas, as apostas são restritas.

    Os limites das contas impostas na indústria de jogos de azar online constituem práticas ilegais em outras
    indústrias, ou são mesmo ilegal em geral. Por exemplo, anunciar produtos ou serviços com a intenção de não os
    vender conforme anunciado, ou anunciar bens ou serviços sem a intenção de fornecer demanda, mas com a intenção
    de atrair o cliente para comprar outro produto é considerada propaganda enganosa e acarreta prejuízos pecuniários
    penalidades no Reino Unido, Austrália e Estados Unidos da América. A maioria dos países tem leis regulamentando
    a publicidade na indústria de jogos de azar, mas algumas dessas leis foram relaxadas em últimos anos e variam de
    país para país. Este caso ilustra algumas das práticas discriminatórias do mercado de apostas esportivas online
    ‒ a indústria de apostas esportivas tem liberdade de divulgar e oferecer probabilidades aos seus clientes,
    mas espera-se que esses clientes percam e, se eles são bem-sucedidos, eles podem ser impedidos de apostar.

"""

# Importar biblioteca pandas
import pandas as pd

# Funcoes da biblioteca Pandas
# https://pandas.pydata.org/docs/user_guide/10min.html

# Declarar um data frame a partir do arquivo CSV
dataframe = pd.read_csv('world_cup_datathon_dataset.csv')

# Substituir odds NaN por 2.0
dataframe = dataframe.fillna(value=2.0)

# Exibir informações sobre o arquivo CSV (nomes das colunas e tipos de dados)
# print(dataframe.info())

# Apresentar todas as colunas do dataframe
pd.set_option('display.max_columns', None)

# Numero de jogos em casa por seleção
# print(dataframe['team_1'].value_counts())

# Numero de jogos fora de casa por seleção
# print(dataframe['team_2'].value_counts())

# Jogos da selecao brasileira
# print(dataframe.query('team_1 == "Brazil" or team_2 == "Brazil"'))

# Jogos da copa de 2014
# print(dataframe.query('tournament == "World Cup 2014"'))

# Jogos da selecao brasileira
jogos_do_brasil = dataframe.query('team_1 == "Brazil" or team_2 == "Brazil"')

# Jogos da selecao brasileira no ano de 2014
# jogos_do_brasil_2014 = jogos_do_brasil.query('date >= "2014-01-01" and date < "2015-01-01"')

# Jogos da selecao brasileira na Copa do Mundo de 2014
jogos_do_brasil_copa_2014 = jogos_do_brasil.query('tournament == "World Cup 2014"')

# Vitorias da selecao brasileira na Copa do Mundo de 2014
# vitorias_brasil_copa_2014 = jogos_do_brasil_copa_2014.query('team_1_goals > team_2_goals')

# Derrotas da selecao brasileira na Copa do Mundo de 2014
# derrotas_brasil_copa_2014 = jogos_do_brasil_copa_2014.query('team_1_goals < team_2_goals')

# Empate da selecao brasileira na Copa do Mundo de 2014
# empates_brasil_copa_2014 = jogos_do_brasil_copa_2014.query('team_1_goals == team_2_goals')

# Probabilidade da selecao brasileira na Copa do Mundo de 2014 em cada jogo
# probabilidade_de_vitoria = 1 / vitorias_brasil_copa_2014['team_1_betfair_odds']
# probabilidade_de_empate = 1 / vitorias_brasil_copa_2014['draw_betfair_odds']
# probabilidade_de_derrota = 1 / vitorias_brasil_copa_2014['team_2_betfair_odds']

# Odds da casa de aposta para os jogos da selecao brasileira na Copa do Mundo de 2014
jogos_do_brasil_copa_2014 = jogos_do_brasil_copa_2014.drop(['tournament', 'is_team_1_home', 'is_team_2_home', 'is_neutral'], axis=1)
# print(jogos_do_brasil_copa_2014)

"""
RESULTADOS DA SELECAO BRASILEIRA NA COPA DO MUNDO DE 2014

            date  team_1       team_2  team_1_goals  team_2_goals  
6441  2014-06-12  Brazil      Croatia             3             1   
6456  2014-06-17  Brazil       Mexico             0             0   
6474  2014-06-23  Brazil     Cameroon             4             1   
6489  2014-06-28  Brazil        Chile             1             1   
6498  2014-07-04  Brazil     Colombia             2             1   
6502  2014-07-08  Brazil      Germany             1             7   
6504  2014-07-12  Brazil  Netherlands             0             3   

ODDS DA SELECAO BRASILEIRA 

      team_1_betfair_odds  draw_betfair_odds  team_2_betfair_odds  
6441                 1.33               5.30                14.00  
6456                 1.33               5.70                11.50  
6474                36.00              11.00                 1.12  
6489                 1.53               4.60                 7.00  
6498                 1.74               3.95                 5.30  
6502                 2.66               3.10                 3.20  
6504                 2.12               3.65                 3.75  

PROBABILIDADE = 1/odd 
EXEMPLO LINHA 6441 = 1/team_1_betfair_odds = 1/1.33 = 0.7519
    Neste exemplo a seleção brasileira tinha 75% de chance de vitória, confirmada pelo placar de 3x1. Entretanto,
    a taxa de acerto durante a copa foi de 29%, ou seja, 2 acertos em 7 jogos. Este resultado pode indicar manipulação 
    da casa de aposta ou a baixa maturidade de dados referentes a seleção brasileira.  
"""

# Jogos da selecao alema
jogos_da_alemanha = dataframe.query('team_1 == "Germany" or team_2 == "Germany"')

# Jogos da selecao brasileira na Copa do Mundo de 2014
jogos_da_alemanha_copa_2014 = jogos_da_alemanha.query('tournament == "World Cup 2014"')

# Odds da casa de aposta para os jogos da selecao brasileira na Copa do Mundo de 2014
jogos_da_alemanha_copa_2014 = jogos_da_alemanha_copa_2014.drop(['tournament', 'is_team_1_home', 'is_team_2_home', 'is_neutral'], axis=1)
# print(jogos_da_alemanha_copa_2014)

"""
RESULTADOS DA SELECAO ALEMA NA COPA DO MUNDO DE 2014

            date   team_1     team_2  team_1_goals  team_2_goals  
6452  2014-06-16  Germany   Portugal             4             0   
6468  2014-06-21  Germany      Ghana             2             2   
6488  2014-06-26      USA    Germany             0             1   
6494  2014-06-30  Germany    Algeria             2             1   
6499  2014-07-04   France    Germany             0             1   
6502  2014-07-08   Brazil    Germany             1             7   
6505  2014-07-13  Germany  Argentina             1             0   

ODDS DA SELECAO ALEMA 

      team_1_betfair_odds  draw_betfair_odds  team_2_betfair_odds  
6452                 2.18               3.45                 3.80  
6468                 1.34               5.80                10.50  
6488                 4.70               1.72                 4.50  
6494                 1.31               5.90                12.50  
6499                 2.84               3.20                 2.84  
6502                 2.66               3.10                 3.20  
6505                 2.44               3.35                 3.30  
"""

# Vitorias da selecao alema nos 2 anos anteriores a copa de 2014
jogos_da_alemanha_ate_2013 = jogos_da_alemanha.query('date >= "2012-08-01" and date < "2014-06-07"')
print(jogos_da_alemanha_ate_2013)

TODO: Determine a quatidade de vitorias da selecao da Alemanha nos 2 anos anteriores a copa de 2014
TODO: Determine a quatidade de vitorias da selecao da Argentina nos 2 anos anteriores a copa de 2014
TODO: Determine a quatidade de vitorias da selecao do Brasil nos 2 anos anteriores a copa de 2014

TODO: Determine a probabilidade de vitoria em cada jogo da selecao da Alemanha nos 2 anos anteriores a copa de 2014
      a partir da coluna 'team_1_betfair_odds' (probabilidade de vitoria = 1/team_1_betfair_odds)
TODO: Determine a probabilidade de vitoria em cada jogo da selecao da Argentina nos 2 anos anteriores a copa de 2014
      a partir da coluna 'team_1_betfair_odds' (probabilidade de vitoria = 1/team_1_betfair_odds)
TODO: Determine a probabilidade de vitoria em cada jogo da selecao do Brasil nos 2 anos anteriores a copa de 2014
      a partir da coluna 'team_1_betfair_odds' (probabilidade de vitoria = 1/team_1_betfair_odds)

TODO: Determine o numero de acertos de resultados em cada jogo da selecao da Alemanha nos 2 anos anteriores a copa de 2014
      a partir do resultado do jogo e da probabilidade de vitoria (vitoria e menor odd ou maior probabilidade)
TODO: Determine o numero de acertos de resultados  em cada jogo da selecao da Argentina nos 2 anos anteriores a copa de 2014
      a partir do resultado do jogo e da probabilidade de vitoria
TODO: Determine o numero de acertos de resultados  em cada jogo da selecao do Brasil nos 2 anos anteriores a copa de 2014
      a partir do resultado do jogo e da probabilidade de vitoria

TODO: É possível determinar um vencedor a partir dos resultados de jogos anteriores a copa de 2014?
      Quais seria a sua estrategia de as apostas no times da seleção da Alemanha, Argentina e Brasil?

