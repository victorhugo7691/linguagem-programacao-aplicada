import math

linha = input()
valores = linha.split()

A = round(float(valores[0]), 1)
B = round(float(valores[1]), 1)
C = round(float(valores[2]), 1)

delta = B ** 2 - 4 * A * C

if A == 0 or delta < 0:
    print("Impossivel calcular")
else:
    r1 = (-B + math.sqrt(delta)) / (2*A)
    r2 = (-B - math.sqrt(delta)) / (2*A )
    print(f"R1 = {r1:.5f}")
    print(f"R2 = {r2:.5f}")