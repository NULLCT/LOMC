import collections

N, Q = map(int, input().split())
edges = collections.defaultdict(list)
for _ in range(N - 1):
    a, b = map(int, input().split())
    edges[a - 1].append(b - 1)
    edges[b - 1].append(a - 1)
targets = [0]
group = [0] * N
group[0] = 1
while targets:
    t = targets.pop()
    for u in edges[t]:
        if group[u] != 0: continue
        group[u] = -group[t]
        targets.append(u)
for _ in range(Q):
    c, d = map(int, input().split())
    if group[c - 1] * group[d - 1] == 1:
        print("Town")
    else:
        print("Road")
