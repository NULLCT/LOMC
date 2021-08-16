N, Q = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N - 1)]
cd = [list(map(int, input().split())) for _ in range(Q)]

G = [[] for _ in range(N + 1)]
for a, b in ab:
    G[a].append(b)
    G[b].append(a)

dp = [10**9] * (N + 1)
from collections import *

que = deque([])
que.append(1)
dp[1] = 0
while que:
    x = que.popleft()
    for nx in G[x]:
        if dp[nx] > dp[x] + 1:
            dp[nx] = dp[x] + 1
            que.append(nx)

for c, d in cd:
    if (dp[c] % 2) == (dp[d] % 2):
        print('Town')
    else:
        print('Road')
