A = float(input())
B = float(input())

if A>10:
    A = 10
elif B>10:
    B=10

nf = A*3.5/10 + B*7.5/10

print(f"MEDIA = {nf: .5f}")