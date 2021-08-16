from collections import deque

N, Q = list(map(int, input().split()))
li = [[] for _ in range(N)]
for i in range(N - 1):
    s, t = list(map(int, input().split()))
    li[s - 1].append(t - 1)
    li[t - 1].append(s - 1)

d = deque()
d.append(s)
dist = [-1] * N
dist[s] = 0
while d:
    v = d.popleft()
    for i in li[v]:
        if dist[i] != -1:
            continue
        dist[i] = dist[v] + 1
        d.append(i)
for i in range(Q):
    s, t = list(map(int, input().split()))
    s -= 1
    t -= 1
    ans = abs(dist[s] - dist[t])
    if ans % 2 == 0:
        print("Town")

    else:
        print("Road")
