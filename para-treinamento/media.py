notas = input()
notas = map(float, notas.split())

pesos = [2, 3, 4, 1]

notas_ponderadas = [nota * pesos[i] for i, nota in enumerate(notas)]

media = sum(notas_ponderadas)/sum(pesos)

print("Media: {:.1f}".format(media))

if media >=7:
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    nota_exame = float(input())
    print("Nota do exame:", nota_exame)
    media_final = (media+nota_exame) / 2
    if media >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: {:.1f}".format(media_final))