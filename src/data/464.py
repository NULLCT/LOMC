from collections import deque

n, q = map(int, input().split())
l = [[] for i in range(n)]
t = [float("inf") for i in range(n)]
t[0] = 0
for i in range(n - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    l[a].append(b)
    l[b].append(a)
d = deque()
for i in range(len(l[0])):
    d.append([0, l[0][i]])
while len(d) > 0:
    x = d.popleft()
    t[x[1]] = x[0] + 1
    for i in range(len(l[x[1]])):
        if t[l[x[1]][i]] == float("inf"):
            d.append([t[x[1]], l[x[1]][i]])
for i in range(q):
    c, d = map(lambda x: int(x) - 1, input().split())
    if (t[c] - t[d]) % 2 == 0:
        print("Town")
    else:
        print("Road")
