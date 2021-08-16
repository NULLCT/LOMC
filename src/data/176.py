n, q = map(int, input().split())

G = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)
d = [None] * n
d[0] = 0
queue = [0]
l = 0
while l < len(queue):
    u = queue[l]
    l += 1
    for v in G[u]:
        if d[v] is None:
            d[v] = d[u] + 1
            queue.append(v)

for _ in range(q):
    ci, di = map(int, input().split())
    ci -= 1
    di -= 1
    if (d[ci] + d[di]) % 2 == 0:
        print("Town")
    else:
        print("Road")
