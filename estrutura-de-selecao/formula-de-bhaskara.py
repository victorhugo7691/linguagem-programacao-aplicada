import math

linha = input()
valores = linha.split()

A = round(float(valores[0]), 1)
B = round(float(valores[1]), 1)
C = round(float(valores[2]), 1)

try:
    delta = B**2 - 4*A*C

    r1 = ((-B + math.sqrt(delta)) / 2*A / 100)
    r2 = ((-B - math.sqrt(delta)) / 2*A / 100)

    print(f"R1 = {r1:.5f}")
    print(f"R2 = {r2:.5f}")

except:
    print("Impossivel calcular")
