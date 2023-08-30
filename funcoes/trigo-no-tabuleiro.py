n = int(input())

for _ in range(n):
    x = int(input())
    if x > 0 and x <= 64:
        grãos = 2 ** x - 1
        kg = grãos // 12
        print(f"{kg} kg")
    else:
        print("Valor fora do intervalo permitido.")
