import collections

n, m = map(int, input().split())

g = []
for _ in range(n + 1):
    g.append([])

for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

visited = [False] * (n + 1)
visited[1] = [True]
que = collections.deque([1])
dst = [0] * (n + 1)

while que:
    q = que.popleft()
    for i in g[q]:
        if visited[i] == False:
            visited[i] = True
            que.append(i)
            dst[i] = dst[q] + 1

for i in range(m):
    c, d = map(int, input().split())
    if abs(dst[c] - dst[d]) % 2 == 1:
        print("Road")
    else:
        print("Town")
