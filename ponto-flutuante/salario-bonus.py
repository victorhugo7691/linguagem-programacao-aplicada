nome = input()
salarioFixo = float(input())
totalDeVendas = float(input())

salarioComBeneficio = salarioFixo + totalDeVendas*0.15

print(f"TOTAL = R$ {salarioComBeneficio:.2f}")