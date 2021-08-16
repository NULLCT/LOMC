from collections import deque

n, q = map(int, input().split())
Road = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    Road[a - 1].append(b - 1)
    Road[b - 1].append(a - 1)

Query = [list(map(int, input().split())) for _ in range(q)]

inf = 10**7

All_cost = []


def bfs(x):
    global cost
    cost = [inf] * n
    dp = [0] * n
    que = deque([x])
    cost[x] = 0
    dp[x] = 1
    while que:
        now = que.popleft()
        curr_cost = cost[now]
        next_cost = curr_cost + 1
        for y in Road[now]:
            if next_cost < cost[y]:
                que.append(y)
                dp[y] = dp[now]
                cost[y] = next_cost
            elif next_cost == cost[y]:
                dp[y] += dp[now]


bfs(0)

for c, d in Query:
    if (cost[c - 1] - cost[d - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
