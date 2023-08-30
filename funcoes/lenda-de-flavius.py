def josephus(n, k):
    circle = list(range(1, n + 1))
    idx = 0
    while len(circle) > 1:
        idx = (idx + k - 1) % len(circle)
        circle.pop(idx)
    return circle[0]

NC = int(input())

for case in range(1, NC + 1):
    n, k = map(int, input().split())
    result = josephus(n, k)
    print(f"Case {case}: {result}")
