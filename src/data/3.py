import sys

sys.setrecursionlimit(100000)

N, Q = map(int, input().split())

bridges = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    bridges[a - 1].append(b - 1)
    bridges[b - 1].append(a - 1)
a = [-1] * N
a[0] = 0


def bfs(c):
    for i in bridges[c]:
        if a[i] == -1:
            a[i] = 0 if a[c] else 1
            bfs(i)


bfs(0)

for i in range(Q):
    x, y = map(int, input().split())
    print('Road' if a[x - 1] != a[y - 1] else 'Town')
