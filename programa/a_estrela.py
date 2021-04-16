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
    return int(inicio), int(fim)

def estrela():
	k = 0
	while k > -1:
		# AINDA NÃO CHEGAMOS...
		for i in range(0, len(fronteira)):
			if visitados[fronteira[i][2]] == 0:
				break
		if fronteira[i][2] == target:
			visitados[fronteira[i][2]] = 1
			resposta.append(fronteira[i][2])
			caminho(fronteira[i])
			break
		sucessores_de(fronteira[i])
		nomes_visitados.append(estacoes_nomes[fronteira[i][2]])
		fronteira.sort(key=lambda fronteira: fronteira[0])
		k += 1


def caminho(a):
	while a[3][2] != -1:
		resposta.append(a[3][2])
		a = a[3]

def sucessores_de(a):
	for i in range(0, len(estacoes_nomes)):
		if matriz_ligacoes[a[2]][i] != 0 and visitados[a[2]] == 0:
			#	CALCULAR O G DESSE SUCESSOR
			g = converterParaTempo(a[3][1] + matriz_estacoes[a[2]][i])
			#	CALCULAR H DESSE SUCESSOR
			h = converterParaTempo(matriz_estacoes[i][target])
			#	PAI DO SUCESSOR (DE QUE ESTAÇÃO ESSE TREM CHEGOU EM i)
			pai = a
			#	COR DA LINHA
			linha = matriz_ligacoes[a[2]][i]
			if a[4] != linha:
				h += tempo_baldeacao	#	ACRESCIMO DO TEMPO GASTO NA TROCA DE LINHA
			#	ADICIONAR NA FRONTEIRA NOVO SUCESSOR
			s = [h+g, g, i, pai, linha]
			fronteira.append(s)
	visitados[a[2]] = 1

def converterParaTempo(x):
	mins = x*2
	return mins

def tempo_final(kilometros_rodados):
	'''
	Encontrar o tempo total da viagem do trem, a partir da velocidade media
	:param kilometros_rodados: kilometragem total da corrida
	:return: o tempo em minutos
	'''
	horas = kilometros_rodados/velocidade_media
	minutos = horas * 60
	return minutos

# LISTA REPRESENTANDO A FRONTEIRA USADA PARA A BUSCA DO A*
fronteira = []

# ARRAY AUXILIAR PARA MARCAÇÃO DE ESTAÇÕES JÁ OU NÃO VISITADAS
visitados = [0]*14

resposta = []

trocasDeEstacao = 0
km = 0

# Matriz com a distancia em linha reta e real entre as estações
matriz_estacoes = [
#	 E1     E2    E3    E4      E5   E6     E7    E8    E9    E10   E11   E12  E13   E14
	(0,    10,   18.5, 24.8, 36.4, 38.8,  35.8, 25.4, 17.6, 9.1,  16.7, 27.3, 27.6, 29.8),# E1
	(10,   0,    8.5,  14.8, 26.6, 29.1,  26.1, 17.3, 10,   3.5,  15.3, 20.9, 19.1, 21.8),# E2
	(18.5, 8.5,  0,    6.3,  18.2, 20.6,  17.6, 13.6, 9.4,  10.3, 19.5, 19.1, 18.7, 16.6),# E3
	(24.8, 14.8, 6.3,  0,    13,   14.4,  11.5, 15.3, 12.6, 16.7, 23.6, 18.6, 12.8, 15.4),# E4
	(36.4, 26.6, 18.2, 13,   0,    3,     2.4,  30,   23.3, 28.2, 34.2, 24.8, 14.5, 17.9),# E5
	(38.8, 29.1, 20.6, 14.4, 3,    0,     3.3,  22.3, 25.7, 30.3, 36.7, 27.6, 15.2, 18.2),# E6
	(35.8, 26.1, 17.6, 11.5, 2.4,  3.3,   0,    20,   23,   27.3, 34.2, 25.7, 12.4, 15.6),# E7
	(25.4, 17.3, 13.6, 15.3, 30,   22.3,  20,   0,    9.6,  20.3, 16.1, 6.4,  22.7, 27.6),# E8
	(17.6, 10,   9.4,  12.6, 23.3, 25.7,  23,   9.6,  0,    13.5, 12.2, 10.9, 21.2, 26.6),# E9
	(9.1,  3.5,  10.3, 16.7, 28.2, 30.3,  27.3, 20.3, 13.5, 0,    17.6, 24.2, 18.7, 21.2),# E10
	(16.7, 15.3, 19.5, 23.6, 34.2, 36.7,  34.2, 16.1, 12.2, 17.6, 0,    14.2, 31.5, 35.5),# E11
	(27.3, 20.9, 19.1, 18.6, 24.8, 27.6,  25.7, 6.4,  10.9, 24.2, 14.2, 0,    28.8, 33.6),# E12
	(27.6, 19.1, 18.7, 12.8, 14.5, 15.2,  12.4, 22.7, 21.2, 18.7, 31.5, 28.8, 0,    5.1), # E13
	(29.8, 21.8, 16.6, 15.4, 17.9, 18.2,  15.6, 27.6, 26.6, 21.2, 35.5, 33.6, 5.1,  0)    # E14
	]

# AZUL     1
# AMARELA  2
# VERDE    3
# VERMELHA 4

# Matriz com as ligações entre as estações(linhas)
matriz_ligacoes = [
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
start, target = receber_st(resposta=estacoes)
start -= 1
target -= 1
# Nome das estações
estacoes_nomes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
# Recebendo velocidade do trem
velocidade_media = int(input('Velocidade média do trem em km/h: '))
# Receber o tempo de baldeação
tempo_baldeacao = int(input('Tempo para trocar de metrô, em minutos: '))
# Calculos
V = [0, 0, -1, -1, -1]
# lista com nomes das estações visitadas
nomes_visitados = []
# E = [f, g, indiceEstacao, pai, corDaLinha]
a = [converterParaTempo(0 + matriz_estacoes[start][target]), 0, start, V, None]

fronteira.append(a)

estrela()

final = resposta[::-1]

#printar as estações na ordem que foram expandidas pelo programa
for pos in range(0, len(nomes_visitados)):
	print(f'{nomes_visitados[pos]}', end='-')
print(f'{target + 1}')

for i in range(0, len(final)):
	if i == 0:
		km += (matriz_estacoes[final[i]][final[i+1]])
	elif i == len(final)-1:
		print(f'{estacoes_nomes[final[i]]}')
		break
	else:
		km += matriz_estacoes[final[i]][final[i+1]]
		if matriz_ligacoes[final[i-1]][final[i]] != matriz_ligacoes[final[i]][final[i+1]]:
			trocasDeEstacao += 1
	print(f'{estacoes_nomes[final[i]]}', end='-')

print(tempo_final(km) + (tempo_baldeacao*trocasDeEstacao))
