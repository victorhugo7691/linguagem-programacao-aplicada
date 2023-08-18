valor = float(input())
saldo = ""

if valor >= 0 and valor <= 2000.00:
    saldo = -1

elif valor >= 2000.01 and valor <= 3000.00:
    saldo = (valor - 2000.00) * 0.08

elif valor >= 3000.01 and valor <= 4500.00:
    saldo = 1000.00 * 0.08 + (valor - 3000.00) * 0.18

elif valor > 4500.00:
    saldo =  1000.00 * 0.08 +  1500.00 * 0.18 + (valor - 4500.00) * 0.28

if saldo == -1:
    print("Isento")
else: 
    print(f"R$ {saldo:.2f}")