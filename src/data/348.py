n, q = map(int, input().split())
a, b = zip(*[map(int, input().split()) for i in range(n - 1)])
c, d = zip(*[map(int, input().split()) for i in range(q)])

E = {i: [] for i in range(n)}
for s, t in zip(a, b):
    s, t = s - 1, t - 1
    E[s].append(t)
    E[t].append(s)
dp = [-1] * n
dp[0] = 0
que = [0]
while que:
    v = que.pop(0)
    for w in E[v]:
        if dp[w] == -1:
            dp[w] = dp[v] + 1
            que.append(w)
for v, w in zip(c, d):
    d = dp[v - 1] + dp[w - 1]
    if d % 2 == 0:
        print("Town")
    else:
        print("Road")
