N, Q = map(int, input().split())
L = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    L[a].append(b)
    L[b].append(a)

dp = [-1 for _ in range(N)]
dp[0] == 0
que = [0]

for i in que:
    for j in L[i]:
        if dp[j] == -1:
            que.append(j)
            dp[j] = abs(dp[i] - 1)

for _ in range(Q):
    c, d = map(lambda x: int(x) - 1, input().split())
    tmp = dp[c] + dp[d]
    print('Road' if tmp % 2 else 'Town')
