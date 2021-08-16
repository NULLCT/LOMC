import sys
from collections import deque

input = sys.stdin.buffer.readline

N, Q = map(int, input().split())
T = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = (int(x) - 1 for x in input().split())
    T[a].append(b)
    T[b].append(a)

table = [None] * N
d = deque([0])
table[0] = True
while d:
    v = d.pop()
    bx = not table[v]
    for x in T[v]:
        if table[x] is None:
            table[x] = bx
            d.append(x)
for _ in range(Q):
    c, d = (int(x) - 1 for x in input().split())
    print('Road' if table[c] ^ table[d] else 'Town')
