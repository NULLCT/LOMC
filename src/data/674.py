import sys
from collections import deque

readline = sys.stdin.readline
readall = sys.stdin.read
ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: map(int, readline().split())
nl = lambda: list(map(int, readline().split()))
prl = lambda x: print(*x, sep='\n')
string = 'abcdefghijklmnopqrstuvwxyz'


def bfs(s, W):
    n = len(W)
    color = [-1] * len(W)
    que = deque([s])
    color[s] = 0
    while que:
        v = que.popleft()
        for w in W[v]:
            if color[w] > -1:
                continue
            color[w] = abs(color[v] - 1)
            que.append(w)
    return color


n, q = nl()
W = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = nl()
    W[a - 1].append(b - 1)
    W[b - 1].append(a - 1)

color = bfs(0, W)
for _ in range(q):
    c, d = nl()
    if color[c - 1] == color[d - 1]:
        print('Town')
    else:
        print('Road')
