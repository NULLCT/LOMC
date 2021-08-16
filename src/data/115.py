N, Q = map(int, input().split())

G = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

tmp = [0] * N
tmp[0] = 1
check = []
check.append(0)

while check:
    i = check.pop(0)
    for k in G[i]:
        if tmp[k] == 0:
            tmp[k] = tmp[i] * (-1)
            check.append(k)

for i in range(Q):
    c, d = map(int, input().split())
    if tmp[c - 1] == tmp[d - 1]:
        print("Town")
    else:
        print("Road")