#O codigo de Wagner Filho me ajudou muito https://github.com/wagnerfilho1995/Metro-de-Paris


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


# Matriz com a distancia em linha reta entre as estações
matriz_estacoes = [
#	 E1     E2    E3    E4      E5   E6     E7    E8    E9    E10   E11   E12  E13   E14
	(0,    10,   18.5, 24.8, 36.4, 38.8,  35.8, 25.4, 17.6, 9.1,  16.7, 27.3, 27.6, 29.8),# E1
	(10,   0,    8.5,  14.8, 26.6, 29.1,  26.1, 17.3, 10,   3.5,  15.3, 20.9, 19.1, 21.8),# E2
	(18.5, 8.5,  0,    6.3,  18.2, 20.6,  17.6, 13.6, 9.4,  10.3, 19.5, 19.1, 12.1, 16.6),# E3
	(24.8, 14.8, 6.3,  0,    12,   14.4,  11.5, 12.4, 12.6, 16.7, 23.6, 18.6, 10.6, 15.4),# E4
	(36.4, 26.6, 18.2, 12,   0,    3,     2.4,  19.4, 23.3, 28.2, 34.2, 24.8, 14.5, 17.9),# E5
	(38.8, 29.1, 20.6, 14.4, 3,    0,     3.3,  22.3, 25.7, 30.3, 36.7, 27.6, 15.2, 18.2),# E6
	(35.8, 26.1, 17.6, 11.5, 2.4,  3.3,   0,    20,   23,   27.3, 34.2, 25.7, 12.4, 15.6),# E7
	(25.4, 17.3, 13.6, 12.4, 19.4, 22.3,  20,   0,    8.2,  20.3, 16.1, 6.4,  22.7, 27.6),# E8
	(17.6, 10,   9.4,  12.6, 23.3, 25.7,  23,   8.2,  0,    13.5, 11.2, 10.9, 21.2, 26.6),# E9
	(9.1,  3.5,  10.3, 16.7, 28.2, 30.3,  27.3, 20.3, 13.5, 0,    17.6, 24.2, 18.7, 21.2),# E10
	(16.7, 15.3, 19.5, 23.6, 34.2, 36.7,  34.2, 16.1, 11.2, 17.6, 0,    14.2, 31.5, 35.5),# E11
	(27.3, 20.9, 19.1, 18.6, 24.8, 27.6,  25.7, 6.4,  10.9, 24.2, 14.2, 0,    28.8, 33.6),# E12
	(27.6, 19.1, 12.1, 10.6, 14.5, 15.2,  12.4, 22.7, 21.2, 18.7, 31.5, 28.8, 0,    5.1),# E13
	(29.8, 21.8, 16.6, 15.4, 17.9, 18.2,  15.6, 27.6, 26.6, 21.2, 35.5, 33.6, 5.1,  0) # E14
	]

# AZUL     1
# AMARELA  2
# VERDE    3
# VERMELHA 4

# Matriz com as ligações entre as estações
ligacoes = [
#	E0  E1  E2 E3 E4 E5 E6 E7 E8 E9 E10 E11 E12 E13
	(0, 1,  0, 0, 0, 0, 0, 0, 0,  0,  0,  0,  0,  0),# E0
	(1, 0,  1, 0, 0, 0, 0, 0, 2,  2,  0,  0,  0,  0),# E1
	(0, 1,  0, 1, 0, 0, 0, 0, 4,  0,  0,  0,  4,  0),# E2
	(0, 0,  1, 0, 1, 0, 0, 3, 0,  0,  0,  0,  3,  0),# E3
	(0, 0,  0, 1, 0, 1, 2, 2, 0,  0,  0,  0,  0,  0),# E4
	(0, 0,  0, 0, 1, 0, 0, 0, 0,  0,  0,  0,  0,  0),# E5
	(0, 0,  0, 0, 2, 0, 0, 0, 0,  0,  0,  0,  0,  0),# E6
	(0, 0,  0, 3, 2, 0, 0, 0, 2,  0,  0,  3,  0,  0),# E7
	(0, 2,  4, 0, 0, 0, 0, 2, 0,  0,  4,  0,  0,  0),# E8
	(0, 2,  0, 0, 0, 0, 0, 0, 0,  0,  0,  0,  0,  0),# E9
	(0, 0,  0, 0, 0, 0, 0, 0, 4,  0,  0,  0,  0,  0),# E10
	(0, 0,  0, 0, 0, 0, 0, 3, 0,  0,  0,  0,  0,  0),# E11
	(0, 0,  4, 3, 0, 0, 0, 0, 0,  0,  0,  0,  0,  3),# E12
	(0, 0,  0, 0, 0, 0, 0, 0, 0,  0,  0,  0,  3,  0) # E13
	]

# Receber a estação de início e fim
estacoes = str(input('Insira a estação de início e destino, respectivamente e separadas por espaços (Ex.: 1 3): ')).strip()
s, t = receber_st(resposta=estacoes)
# Recebendo velocidade do trem
v = int(input('Velocidade média do trem em km/h: '))
# Receber o tempo de baldeação
# u = int(input('Tempo para trocar de metrô, em minutos: '))

# Calculos