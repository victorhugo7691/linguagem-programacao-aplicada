def eh_perfeito(numero):
    divisores = [1]
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            divisores.append(i)
            if i != numero // i:
                divisores.append(numero // i)
    
    return sum(divisores) == numero

N = int(input())  

if N == 1:
    print(f"{N} nao eh perfeito")

else:
    for _ in range(N):
        X = int(input())
        if X == 1:
            print(f"{X} nao eh perfeito")
        else:
            if eh_perfeito(X):
                print(f"{X} eh perfeito")
            else:
                print(f"{X} nao eh perfeito")