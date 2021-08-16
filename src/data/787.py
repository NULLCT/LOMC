import sys

sys.setrecursionlimit(200000)

N, Q = map(int, input().split())

depth = [None] * N
canGo = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    canGo[a].append(b)
    canGo[b].append(a)


def iter(s, dep):
    depth[s] = dep
    for n in canGo[s]:
        if depth[n] is None:
            iter(n, dep + 1)


m = 0
s = 0
for i, x in enumerate(canGo):
    if len(x) > m:
        m = len(x)
        s = i
iter(s, 0)
# print(depth)

for _ in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if (depth[c] - depth[d]) % 2 == 0:
        print('Town')
    else:
        print('Road')
