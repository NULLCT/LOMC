from collections import deque

N, Q = map(int, input().split())
city = [[] for _ in range(N + 1)]
for i in range(N - 1):
    a, b = map(int, input().split())
    city[a].append(b)
    city[b].append(a)
n_city = [-1] * (N + 1)
q = deque([])
q.append(1)
n_city[1] = 0
while q:
    x = q.pop()
    p = n_city[x]
    for i in city[x]:
        if n_city[i] != -1:
            continue
        q.append(i)
        n_city[i] = p ^ 1
for i in range(Q):
    c, d = map(int, input().split())
    if n_city[c] == n_city[d]:
        print("Town")
    else:
        print("Road")
