from collections import deque

N, Q = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N - 1)]
CD = [list(map(int, input().split())) for _ in range(Q)]
G = [[] for _ in range(N)]
dp = [-1] * N

for ab in AB:
    a, b = ab
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

Q = deque()
Q.append(0)
dp[0] = 0
while Q:
    q = Q.pop()
    for g in G[q]:
        if dp[g] == -1:
            dp[g] ^= dp[q]
            Q.append(g)

for cd in CD:
    c, d = cd
    if dp[c - 1] == dp[d - 1]:
        print("Town")
    else:
        print("Road")
