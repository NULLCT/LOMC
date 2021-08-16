n, k = map(int, input().split(' '))
from collections import defaultdict, deque

g = defaultdict(list)
for _ in range(n - 1):
    a, b = map(int, input().split(' '))
    g[a].append(b)
    g[b].append(a)
d = defaultdict(int)
q = deque()
q.append((1, -1))
v = {1}
while q:
    t, par = q.popleft()
    if par == -1:
        d[t] = 0
    else:
        d[t] = abs(d[par] - 1)
    for child in g[t]:
        if child not in v:
            v.add(child)
            q.append((child, t))

for _ in range(k):
    a, b = map(int, input().split(' '))
    if d[a] == d[b]:
        print('Town')
    else:
        print('Road')
