def funcaoDoRafael(x, y):
    return (3*x)*(3*x) + y*y

def funcaoDoBeto(x, y):
    return 2*(x*x) + (5*y)*(5*y)

def funcaoDoCarlos(x, y):
    return -100 * x + (y*y*y)

n = int(input())

for _ in range(n):
    valor = input()
    valores = valor.split()
    x = int(valores[0])
    y = int(valores[1])

    rafael = funcaoDoRafael(x, y)
    beto = funcaoDoBeto(x, y)
    carlos = funcaoDoCarlos(x, y)

    if rafael > beto and rafael  > carlos:
        print("Rafael ganhou")
    if beto > carlos and beto > rafael:
        print("Beto ganhou")
    elif (carlos > beto and carlos > rafael):
        print("Carlos ganhou")
