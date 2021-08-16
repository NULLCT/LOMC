n, q = map(int, input().split())
a = [[]]
for _ in range(n):
    a.append([])
for _ in range(n - 1):
    b = list(map(int, input().split()))
    a[b[0]].append(b[1])
    a[b[1]].append(b[0])

visited = [False] * (n + 1)
visited[1] = True
e = [1]
f = [-1] * (n + 1)
f[1] = 0
while len(e) > 0:
    for i in a[e[0]]:
        if not visited[i]:
            e.append(i)
            f[i] = (f[e[0]] + 1) % 2
            visited[i] = True
    e.pop(0)
for i in range(q):
    c, d = map(int, input().split())
    if f[c] == f[d]:
        print("Town")
    else:
        print("Road")
