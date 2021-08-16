from collections import defaultdict

n, m = map(int, input().strip().split())
g = defaultdict(list)
for i in range(n - 1):
    x, y = map(int, input().strip().split())
    g[x - 1].append(y - 1)
    g[y - 1].append(x - 1)

color = [-1] * n
q = [0]
color[0] = 0
while q:
    t = q.pop(0)
    for i in g[t]:
        if color[i] == -1:
            color[i] = color[t] ^ 1
            q.append(i)

for i in range(m):
    x, y = map(int, input().strip().split())
    if color[x - 1] != color[y - 1]:
        print("Road")
    else:
        print("Town")
