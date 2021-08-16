import sys

sys.setrecursionlimit(10**9)

n, q = map(int, input().split())
se = [[] for _ in range(n)]
for i in range(n - 1):
    a, b = map(int, input().split())
    se[a - 1].append(b - 1)
    se[b - 1].append(a - 1)

kyori = [10**9] * n
done = [True] * n
done[0] = False


def dfs(t, m):
    global kyori
    kyori[t] = m
    for i in se[t]:
        if done[i]:
            done[i] = False
            dfs(i, m + 1)


dfs(0, 0)

for i in range(q):
    c, d = map(int, input().split())
    if kyori[c - 1] % 2 == kyori[d - 1] % 2:
        print("Town")
    else:
        print("Road")
