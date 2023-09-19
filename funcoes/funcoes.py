def funcaoRafael(x, y):
    return (3*x)*(3*x) + y*y

def funcaoBeto(x, y):
    return 2*(x*x) + 5*(x*x*x)

def funcaoCarlos(x, y):
    return -100*x + (y*y*y)

nCasos = int(input())

for i in range(nCasos):
    linha = input()
    valores = linha.split()

    x = int(valores[0])
    y = int(valores[1])

    if funcaoRafael(x, y) > funcaoBeto(x,y) and funcaoRafael(x, y) > funcaoCarlos(x, y):
        print("Rafael ganhou")
    
    elif funcaoBeto(x, y) > funcaoRafael(x, y) and funcaoBeto(x, y) > funcaoCarlos(x, y):
        print("Beto ganhou")
    
    else:
        print("Carlos ganhou")