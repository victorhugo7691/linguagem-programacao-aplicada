dias_do_ano = 365
dias_do_mes = 30

dias = int(input())

anos = int(dias / dias_do_ano)
dias_restantes = dias % dias_do_ano
meses = dias_restantes // dias_do_mes
dias_restantes = dias_restantes % dias_do_mes

print(anos, "ano(s)")
print(meses, "mes(es)")
print(dias_restantes, "dia(s)")