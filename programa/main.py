def receive_st():
    awnser = str(input('Insira a estação de início e destino, respectivamente e separadas por espaços (Ex.: 1 3): ')).strip()
    numbers = awnser.split()
    start = int(numbers[0])
    end = int(numbers[1])
    return start, end



#Receiving start station and final station
s, t = receive_st()
#Receiving train average speed
v = int(input('Velocidade média do trem em km/h: '))
#Receiving the trade time
u = int(input('Tempo para trocar de metrô, em minutos: '))

