from collections import deque

n, Q = map(int, input().split())
g = [set() for i in range(n)]
for i in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    g[a].add(b)
    g[b].add(a)

depth = [-1] * n
depth[0] = 0
q = deque([0])
while q:
    at = q.pop()
    for i in g[at]:
        if depth[i] == -1:
            depth[i] = depth[at] + 1
            q.append(i)
for i in range(Q):
    c, d = map(lambda x: int(x) - 1, input().split())
    print('Road') if abs(depth[c] - depth[d]) % 2 else print('Town')
