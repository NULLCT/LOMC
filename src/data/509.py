import collections

N, Q = map(int, input().split())

adj = collections.defaultdict(list)
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    adj[a].append(b)
    adj[b].append(a)


def dfs():
    colors = [-1] * N
    q = [(0, 0)]  # (node, color)
    while q:
        node, color = q.pop()
        if colors[node] != -1: continue
        colors[node] = color
        for nd in adj[node]:
            q.append((nd, color ^ 1))
    return colors


colors = dfs()

for _ in range(Q):
    c, d = map(int, input().split())
    if colors[c - 1] == colors[d - 1]:
        print('Town')
    else:
        print('Road')
