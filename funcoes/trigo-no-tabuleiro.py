def calcular_quantidade_graos(casas):
    quantidade_total = 1
    
    for i in range(1, casas):
        quantidade_total += 2 ** i
    
    return quantidade_total

n = int(input())

for _ in range(n):
    casas = int(input())
    quantidade_graos = calcular_quantidade_graos(casas)
    quantidade_kg = quantidade_graos / 12 / 1000
    print(f"{int(quantidade_kg)} kg")
