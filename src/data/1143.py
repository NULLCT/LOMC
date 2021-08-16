N, Q = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(N - 1)]
cd = [list(map(int, input().split())) for i in range(Q)]
f = [[] for i in range(N)]
for a, b in ab:
    f[a - 1].append(b - 1)
    f[b - 1].append(a - 1)
from collections import deque

d = deque()
d.append(0)
dp = [-1] * N
dp[0] = 0
while d:
    z = d.popleft()
    for i in f[z]:
        if dp[i] == -1:
            dp[i] = dp[z] + 1
            d.append(i)
for c, d in cd:
    if dp[c - 1] % 2 == dp[d - 1] % 2:
        print("Town")
    else:
        print("Road")
