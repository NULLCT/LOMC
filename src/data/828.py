from collections import deque

n, q = map(int, input().split())

g = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    g[a].append(b)
    g[b].append(a)

query = []
for _ in range(q):
    x, y = map(int, input().split())
    query.append((x - 1, y - 1))

d = [0] * n
visited = set()
que = deque([0])
cnt = 0
while que:
    for _ in range(len(que)):
        cur = que.popleft()
        visited.add(cur)
        d[cur] = cnt
        for nxt in g[cur]:
            if nxt not in visited:
                que.append(nxt)
    cnt += 1

for x, y in query:
    if abs(d[x] - d[y]) % 2 == 0:
        print("Town")
    else:
        print("Road")
