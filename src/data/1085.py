from collections import deque

n, q = map(int, input().split())
g = [[] for _ in range(n)]
s = [-1 for _ in range(n)]

for i in range(n - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

queue = deque([[0, 0]])
while queue:
    now = queue.popleft()
    nowi = now[0]
    nows = now[1]
    s[nowi] = nows
    for i in g[nowi]:
        if (s[i] == -1):
            queue.append([i, (nows + 1) % 2])

for i in range(q):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if (s[a] == s[b]):
        print("Town")
    else:
        print("Road")
