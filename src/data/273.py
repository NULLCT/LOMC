from collections import deque

N, Q = map(int, input().split())
V = [[] for _ in range(N + 1)]
for i in range(N - 1):
    a, b = map(int, input().split())
    V[a].append(b)
    V[b].append(a)

q = deque()
q.append(1)
dp = [-1 for _ in range(N + 1)]
dp[1] = 0
while q:
    now = q.popleft()
    for nxt in V[now]:
        if dp[nxt] == -1:
            q.append(nxt)
            dp[nxt] = (dp[now] + 1) % 2

for i in range(Q):
    c, d = map(int, input().split())
    if dp[c] == dp[d]:
        print('Town')
    else:
        print('Road')
