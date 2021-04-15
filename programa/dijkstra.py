# Para realizar esse trabalho eu utilizei o Algoritmo de Dijkstra
# O código de TamaWilson me ajudou muito (https://github.com/TamaWilson/dijkstra_python)


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


def dijkstra(grafo, origem, fim):
    '''
    retorna a menor distancia de um No origem até um No destino e o caminho até ele
    :param grafo: Dict
    :param origem: Estação de partida
    :param fim: Estação de chegada
    :return:
    '''

    controle = {}
    distanciaAtual = {}
    noAtual = {}
    naoVisitados = []
    atual = origem
    noAtual[atual] = 0

    for vertice in grafo.keys():
        naoVisitados.append(vertice)  # inclui os vertices nos não visitados
        distanciaAtual[vertice] = float('inf')  # inicia os vertices como infinito

    distanciaAtual[atual] = [0, origem]

    naoVisitados.remove(atual)

    while naoVisitados:
        for vizinho, peso in grafo[atual].items():
            pesoCalc = peso + noAtual[atual]
            if distanciaAtual[vizinho] == float("inf") or distanciaAtual[vizinho][0] > pesoCalc:
                distanciaAtual[vizinho] = [pesoCalc, atual]
                controle[vizinho] = pesoCalc

        if controle == {}: break

        minVizinho = min(controle.items(), key=lambda x: x[1])  # seleciona o menor vizinho
        atual = minVizinho[0]
        noAtual[atual] = minVizinho[1]
        naoVisitados.remove(atual)
        del controle[atual]

    print("A menor distância de %s até %s é: %s" % (origem, fim, distanciaAtual[fim][0]))
    print("O menor caminho é: %s" % printPath(distanciaAtual, origem, fim))
    return float(distanciaAtual[fim][0])


def printPath(distancias, inicio, fim):
    if fim != inicio:
        return "%s-%s" % (printPath(distancias, inicio, distancias[fim][1]), fim)
    else:
        return inicio


#Dicionario com as informações do grafo (Distancia em km)
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

#Receber a estação de início e fim
estacoes = str(input('Insira a estação de início e destino, respectivamente e separadas por espaços (Ex.: 1 3): ')).strip()
s, t = receber_st(resposta=estacoes)
#Recebendo velocidade do trem
v = int(input('Velocidade média do trem em km/h: '))
#Receber o tempo de baldeação
#u = int(input('Tempo para trocar de metrô, em minutos: '))

#Calculos
distancia_total = dijkstra(grafo=grafo_estacoes, origem=s, fim=t)
tempo_trem_minutos = (distancia_total/v)*60
print(f'Tempo do trem é igual a {tempo_trem_minutos} e distancia total é {distancia_total}')
