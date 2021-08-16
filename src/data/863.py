n, q = map(int, input().split())
AB = [[*map(lambda x: int(x) - 1, input().split())] for _ in range(n - 1)]
CD = [[*map(lambda x: int(x) - 1, input().split())] for _ in range(q)]
# print(n,q)
# print(AB)
# print(CD)

G = [[] for _ in range(n)]
for a, b in AB:
    G[a].append(b)
    G[b].append(a)

# for i in range(n):
#     print(i,G[i])

from collections import deque


def bfs(p):
    res = []
    used = [False] * (n)
    dq = deque()
    i = 0
    dq.append([p, i])
    while dq:
        v, i = dq.popleft()
        if used[v]: continue
        used[v] = True
        res.append([v, i])
        for u in G[v]:
            dq.append([u, i + 1])
    return res


P = bfs(0)
P.sort()
# print(f'P {P}')

for c, d in CD:
    if (P[c][1] + P[d][1]) % 2:
        print('Road')
    else:
        print('Town')
