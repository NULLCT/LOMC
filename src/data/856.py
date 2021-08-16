import sys

sys.setrecursionlimit(10**9)

n, q = map(int, input().split())

if n == 2:
    for i in range(q):
        print("Road")
    sys.exit()

road = [[] for _ in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())
    road[a].append(b)
    road[b].append(a)
INF = float("inf")

le = [[] for _ in range(n + 1)]
seen = 1

start = 0
for i in range(1, n - 1):
    if len(road[i]) == 1:
        start = i
        break
le[start].append(1)


def dfs(cur, l):
    global seen
    if seen == n:
        return
    tind = 0
    tl = INF
    for t in road[cur]:
        if len(le[t]) == 0:
            tind = t
            seen += 1
            break
        elif max(le[t]) < tl:
            tl = max(le[t])
            tind = t
    le[tind].append(l + 1)
    dfs(tind, l + 1)


dfs(start, 1)

for i in range(q):
    x, y = map(int, input().split())
    ans = min(abs(max(le[x]) - min(le[y])), abs(max(le[y]) - min(le[x])))
    if ans % 2 == 1:
        print("Road")
    else:
        print("Town")
