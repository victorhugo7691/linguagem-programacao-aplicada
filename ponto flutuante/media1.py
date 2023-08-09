A = float(input())
B = float(input())

if A>10:
    A = 10.0
elif B>10:
    B=10.0

nf = A*3.5/11 + B*7.5/11

print(f"MEDIA = {nf: .5f}\n")