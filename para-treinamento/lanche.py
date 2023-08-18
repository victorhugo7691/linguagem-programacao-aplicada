dados = input()
codigo, quantidade = map(int, dados.split())

precos = [4, 4.5, 5, 2, 1.5]

print("Total: R$ {:.2f}".format(precos[codigo-1]*quantidade))