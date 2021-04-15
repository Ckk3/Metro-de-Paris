def receber_st(resposta):
    '''
    Recebe uma string com os valores de s e t separadas por espaço e as retorna como duas variáveis diferentes
    :param resposta: Numeros inseridos pelo usuario
    :return: s e t separados em variáveis diferentes
    '''
    numeros = resposta.split()
    inicio = str(numeros[0])
    fim = str(numeros[1])
    return inicio, fim


#Dicionario com a distancia real entre as estações
grafo_estacoes = {'1': {'2': 10},
         '2': {'3': 8.5, '9': 10, '10': 3.5},
         '3': {'4': 6.3, '9': 9.4, '13': 18.7},
         '4': {'5': 13, '8': 15.3, '13': 12.8},
         '5': {'6': 3, '7': 2.4, '8': 30},
         '6': {},
         '7': {},
         '8': {'9': 9.6, '12': 6.4},
         '9': {'11': 12.2},
         '10': {},
         '11': {},
         '12': {},
         '13': {'14': 5.1},
         '14': {}
}

#Dicionario com as distancias em linha reta entre as estações
distancia_real = {'1': {'2': 10, '3': 18.5, '4': 24.8, '5': 36.4, '6': 38.8, '7': 35.8, '8': 25.4, '9': 17.6, '10': 9.1, '11': 16.7, '12': 27.3, '13': 27.6, '14': 29.8},
         '2': {'3': 8.5, '4': 14.8, '5': 26.4, '6': 29.1, '7': 26.1, '8': 17.3, '9': 10, '10': 3.5, '11': 15.5, '12': 20.9, '13': 19.1, '14': 21.8},
         '3': {'4': 6.3, '5': 18.2, '6': 20.6, '7': 17.6, '8': 13.6, '9': 9.4, '10': 10.3, '11': 19.5, '12': 19.1, '13': 12.1, '14': 16.6},
         '4': {'5': 12, '6': 14.4, '7': 11.5, '8': 12.4, '9': 12.6, '10': 16.7, '11': 23.6, '12': 18.6, '13': 10.6, '14': 15.4},
         '5': {'6': 3, '7': 2.4, '8': 19.4, '9': 23.3, '10': 28.2, '11': 34.2, '12': 24.8, '13': 14.5, '14': 17.9},
         '6': {'7': 3.3, '8': 22.3, '9': 25.7, '10': 30.3, '11': 36.7, '12': 27.6, '13': 15.2, '14': 18.2},
         '7': {'8': 20, '9': 23, '10': 27.3, '11': 34.2, '12': 25.7, '13': 12.4, '14': 15.6},
         '8': {'9': 8.2, '10': 20.3, '11': 16.1, '12': 6.4, '13': 22.7, '14': 27.6},
         '9': {'10': 13.5, '11': 11.2, '12': 10.9, '13': 21.2, '14': 26.6},
         '10': {'11': 17.6, '12': 24.2, '13': 18.7, '14': 21.2},
         '11': {'12': 14.2, '13': 31.5, '14': 35.5},
         '12': {'13': 28.8, '14': 33.6},
         '13': {'14': 5.1},
         '14': {}
}

#Receber a estação de início e fim
estacoes = str(input('Insira a estação de início e destino, respectivamente e separadas por espaços (Ex.: 1 3): ')).strip()
s, t = receber_st(resposta=estacoes)
#Recebendo velocidade do trem
v = int(input('Velocidade média do trem em km/h: '))
#Receber o tempo de baldeação
#u = int(input('Tempo para trocar de metrô, em minutos: '))

#Calculos