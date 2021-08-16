from collections import deque

N, Q = map(int, input().split())
gr = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    gr[a].append(b)
    gr[b].append(a)
s = 0
d = deque()
d.append(s)
log = [0 for i in range(N)]
log[0] = 1
while d:
    e = d.popleft()
    for i in gr[e]:
        if log[i] == 0:
            log[i] = 1
            d.append(i)
            s = i
dis = [0 for i in range(N)]
log = [0 for i in range(N)]
log[s] = 1
d = deque()
d.append(s)
while d:
    e = d.popleft()
    for i in gr[e]:
        if log[i] == 0:
            log[i] = 1
            d.append(i)
            dis[i] = dis[e] + 1
for i in range(Q):
    f, g = map(int, input().split())
    h = abs(dis[f - 1] - dis[g - 1])
    if h % 2 == 0:
        print("Town")
    else:
        print("Road")
