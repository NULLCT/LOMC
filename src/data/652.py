import sys
import collections

sys.setrecursionlimit(10**5)

INF = 10**10

N, Q = map(int, input().split())

G = [[] for _ in range(N)]
seen = [-1] * N
todo = collections.deque()
th = []
et = [[INF, -1] for _ in range(N)]

for i in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)


def dfs(G, v):
    seen[v] = 0
    th.append(v)
    if len(G[v]) == 0:
        return
    else:
        for r in G[v]:
            if seen[r] != -1:
                continue
            else:
                dfs(G, r)
                th.append(v)


dfs(G, 0)
#print(th)
for i in range(len(th)):
    et[th[i]][0] = min(et[th[i]][0], i)
    et[th[i]][1] = max(et[th[i]][1], i)

#print(et)

for i in range(Q):
    c, d = map(int, input().split())
    s1, s2, e1, e2 = et[c - 1][0], et[d - 1][0], et[c - 1][1], et[d - 1][1]
    if max(s1, s2) <= min(e1, e2):
        dist = abs(s1 - s2) - 1
    else:
        dist = abs(min(e1, e2) - max(s1, s2)) - 1

    if dist % 2 == 1:
        print('Town')
    else:
        print('Road')
