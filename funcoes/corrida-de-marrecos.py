def calcular_corridas(participantes):
    if participantes < 2:
        return 0

    connidas = 0

    while participantes >1:

        if participantes % 3 == 0:

            participantes //= 3 
        else:
            participantes = participantes // 3 + 1

        connidas += participantes

    return connidas

while True:
    t_participantes = int(input())
    
    if t_participantes == 0:
        break 

    print(calcular_corridas(t_participantes))
