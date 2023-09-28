def calcular_sequencias(N, memo):
    if N == 0:
        return 1
    if N < 0:
        return 0

    if memo[N] != -1:
        return memo[N]

    memo[N] = calcular_sequencias(N - 1, memo) + calcular_sequencias(N - 2, memo)
    return memo[N]

while True:
    N = int(input())
    if N == 0:
        break
    memo = [-1] * (N + 1)
    resultado = calcular_sequencias(N, memo)
    print(resultado)
