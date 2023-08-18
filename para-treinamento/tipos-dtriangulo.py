lados = map(float, input().split())

lados_ordenados = sorted(lados, reverse=True)

a, b, c = lados_ordenados

if a >= c+b:
    print("NAO FORMA TRIANGULO")
else:
    quadrado_catetos = b**2 + c**2
    quadrado_maior = a**2

    if quadrado_maior == quadrado_catetos:
        print("TRIANGULO RETANGULO")
    elif quadrado_maior > quadrado_catetos:
        print("TRIANGULO OBTUSANGULO")
    else:
        print("TRIANGULO ACUTANGULO")

    if a == b == c:
        print("TRIANGULO EQUILATERO")
    elif a == b or a == c or b == c:
        print("TRIANGULO ISOSCELES")