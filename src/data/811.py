N, Q = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N - 1)]

connect = [[] for _ in range(N + 1)]
for a, b in ab:
    connect[a].append(b)
    connect[b].append(a)

odd = [None] * (N + 1)
checked = [False] * (N + 1)
checked[1] = True
odd[1] = True
q = [1]
while q:
    s = q.pop(0)
    for n in connect[s]:
        if not checked[n]:
            checked[n] = True
            odd[n] = not odd[s]
            q.append(n)
for _ in range(Q):
    c, d = map(int, input().split())
    if odd[c] == odd[d]:
        print("Town")
    else:
        print("Road")
