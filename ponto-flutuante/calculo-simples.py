linha = input()
linha2 = input()
valores = linha.split()
valores2 = linha2.split()

codigo = int(valores[0])
numeroPecas = int(valores[1])
valorDaPeca = float(valores[2])

codigo2 = int(valores2[0])
numeroPecas2 = int(valores2[1])
valorDaPeca2 = float(valores2[2])

valorAPagar = numeroPecas*valorDaPeca + numeroPecas2*valorDaPeca2

print(f"VALOR A PAGAR: R$ {valorAPagar:.2f}")