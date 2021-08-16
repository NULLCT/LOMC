N, Q = map(int, input().split())
L = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    L[a].append(b)
    L[b].append(a)

dp = [-1 for _ in range(N)]
dp[0] = 0
que = [0]
bl = [1, 0]

for i in que:
    for j in L[i]:
        if dp[j] == -1:
            que.append(j)
            dp[j] = bl[dp[i]]

for _ in range(Q):
    c, d = map(lambda x: int(x) - 1, input().split())
    print('Town' if dp[c] == dp[d] else 'Road')
