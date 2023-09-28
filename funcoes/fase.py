N = int(input())
K = int(input())
pontuacoes = [int(input()) for _ in range(N)]
pontuacao_limite = sorted(pontuacoes, reverse=True)[K - 1]
classificados = sum(1 for pontuacao in pontuacoes if pontuacao >= pontuacao_limite)
print(classificados)
