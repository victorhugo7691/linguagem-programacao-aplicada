inicio, fim = map(int, input().split())

duracao = ((24 - inicio) + fim) % 24
if duracao == 0: duracao = 24

print('O JOGO DUROU', duracao, 'HORA(S)')