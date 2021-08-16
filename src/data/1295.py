n, q = map(int, input().split())
path = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    path[a - 1].append(b - 1)
    path[b - 1].append(a - 1)
kyori = [-1 for i in range(n)]
kyori[0] = 0
now = [0]
for i in range(10**5):
    next = []
    for p in now:
        for go in path[p]:
            if kyori[go] == -1:
                kyori[go] = i + 1
                next.append(go)
    now = next
for i in range(q):
    c, d = map(int, input().split())
    if kyori[c - 1] % 2 == kyori[d - 1] % 2:
        print("Town")
    else:
        print("Road")
