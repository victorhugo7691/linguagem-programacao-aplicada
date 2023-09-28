def criar_dicionario_traducoes(N):
    traducoes = {}
    for _ in range(N):
        lingua = input()
        traducao = input()
        traducoes[lingua] = traducao
    return traducoes

def imprimir_etiquetas(M, traducoes):
    for _ in range(M):
        nome = input()
        lingua = input()
        traducao = traducoes[lingua]
        print(nome)
        print(traducao)
        print() 

N = int(input())
traducoes = criar_dicionario_traducoes(N)
M = int(input())
imprimir_etiquetas(M, traducoes)
