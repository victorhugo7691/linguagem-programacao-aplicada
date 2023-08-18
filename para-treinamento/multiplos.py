x = input().split()
x = [int(i) for i in x]

if x[0] > x[1]:
    x[0],x[1] = x[1],x[0]
    
if x[1] % x[0] == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")