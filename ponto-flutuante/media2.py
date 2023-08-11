A = float(input())
B = float(input())
C = float(input())

if A>=10:
    A = 10.0
if B>=10:
    B = 10.0
if C>=10:
    C = 10.0

m = A*0.2 + B*0.3 + C*0.5

print(f"MEDIA = {m:.1f}")