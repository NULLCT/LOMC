N, Q = map(int, input().split())
G = dict()
for i in range(N - 1):
    a, b = map(int, input().split())
    if a not in G:
        G[a] = []

    if b not in G:
        G[b] = []

    G[a].append(b)
    G[b].append(a)

color = [-1] * (N + 1)
color[1] = 0
s = [1]
while len(s) > 0:
    v = s.pop()
    for w in G[v]:
        if color[w] != -1:
            continue

        color[w] = 1 - color[v]
        s.append(w)

for i in range(Q):
    c, d = map(int, input().split())
    if color[c] == color[d]:
        print("Town")
    else:
        print("Road")
