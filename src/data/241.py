from sys import stdin

input = stdin.readline

n, q = map(int, input().split())

e = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    e[a - 1].append(b - 1)
    e[b - 1].append(a - 1)

dist = [-1] * n
stack = [0]
dist[0] = 0
while stack:
    v = stack.pop(-1)
    for u in e[v]:
        if dist[u] == -1:
            dist[u] = dist[v] + 1
            stack += [u]

for j in range(q):
    c, d = map(int, input().split())
    ans = dist[c - 1] + dist[d - 1]

    if ans % 2 == 1:
        print('Road')
    else:
        print('Town')
