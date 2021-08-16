from collections import deque

n, q = map(int, input().split())
graph = [[] for i in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

dp = [0] * n

que = deque()
que.append([0, 1])
ch = [False] * n
while (que):
    t = que.popleft()
    x = t[0]
    cnt = t[1]
    for i in graph[x]:
        if (ch[i]):
            continue
        else:
            if (cnt % 2):
                dp[i] = 1
            ch[i] = True
            que.append([i, cnt + 1])

ans = [0] * q
for i in range(q):
    c, d = map(int, input().split())
    if (dp[c - 1] == dp[d - 1]):
        ans[i] = 1

for i in range(q):
    if (ans[i]):
        print("Town")
    else:
        print("Road")
