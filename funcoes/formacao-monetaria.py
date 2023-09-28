def formatar_valor(dolares, centavos):
    dolares_formatados = f"${dolares:,}"
    
    centavos_formatados = f"{centavos:02}"
    
    valor_formatado = f"{dolares_formatados}.{centavos_formatados}"
    
    return valor_formatado

while True:
    try:
        dolares = int(input())
        centavos = int(input())
        valor_formatado = formatar_valor(dolares, centavos)
        print(valor_formatado)
    except EOFError:
        break
