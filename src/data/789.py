from collections import deque

N, Q = map(int, input().split())
G = [[] for i in range(N)]
for i in range(N - 1):
    A, B = map(int, input().split())
    G[A - 1].append(B - 1)
    G[B - 1].append(A - 1)

ans = []
route = [-1] * N
route[0] = 0
d = deque([0])
while d:
    check = d.popleft()
    for j in G[check]:
        if route[j] == -1:
            if route[check] == 0:
                route[j] = 1
            else:
                route[j] = 0
            d.append(j)

ans = []
for i in range(Q):
    c, d = map(int, input().split())
    if route[c - 1] == route[d - 1]:
        ans.append("Town")
    else:
        ans.append("Road")

for i in range(Q):
    print(ans[i])
