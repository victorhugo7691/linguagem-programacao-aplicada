def calcular_numero_corridas(numero_marrecos):
    numero_corridas = 0
    
    while numero_marrecos > 1:
        if numero_marrecos % 3 == 0:
            numero_corridas += numero_marrecos // 3
            numero_marrecos = numero_marrecos // 3
        elif numero_marrecos % 3 == 1:
            numero_corridas += (numero_marrecos - 1) // 3
            numero_marrecos = (numero_marrecos - 1) // 3 + 1
        else:
            numero_corridas += (numero_marrecos - 2) // 3
            numero_marrecos = (numero_marrecos - 2) // 3 + 1
    
    return numero_corridas

numero_marrecos = int(input())
numero_corridas = calcular_numero_corridas(numero_marrecos)
print(numero_corridas)