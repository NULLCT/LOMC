N, Q = map(int, input().split())
tree = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a - 1].append(b - 1)
    tree[b - 1].append(a - 1)
import sys

sys.setrecursionlimit(10**7)
D = [0] * N
from functools import lru_cache


@lru_cache
def dfs(t=0, d=0, p=-1):
    global D
    for u in tree[t]:
        if u == p:
            continue
        D[u] = (d + 1) % 2
        dfs(u, d + 1, t)


dfs()
for _ in range(Q):
    c, d = map(int, input().split())
    print('Road' if (D[c - 1] - D[d - 1]) % 2 == 1 else 'Town')
