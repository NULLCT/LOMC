import queue

n, Q = map(int, input().split())
g = [[] for i in range(n)]

for i in range(n - 1):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    g[b - 1].append(a - 1)

used = [False] * n
dep = [0] * n

q = queue.Queue()
used[0] = 1
q.put(0)

while not q.empty():
    v = q.get()
    for u in g[v]:
        if used[u]:
            continue
        dep[u] = dep[v] + 1
        used[u] = 1
        q.put(u)

ans = []
for i in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if abs(dep[d] - dep[c]) % 2 == 0:
        print('Town')
    else:
        print('Road')
