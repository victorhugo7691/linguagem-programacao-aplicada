N = int(input())
votos = list(map(int, input().split()))

total_votos = sum(votos)

voto_maximo = max(votos)
votos.remove(voto_maximo)
segundo_voto_maximo = max(votos)

if voto_maximo >= total_votos * 0.45 or (voto_maximo >= total_votos * 0.4 and voto_maximo > segundo_voto_maximo + total_votos * 0.1):
    print('1')
else:
    print('2')
