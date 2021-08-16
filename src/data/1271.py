N, Q = map(int, input().split())
edge = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(lambda x: int(x) - 1, input().split())
    edge[a].append(b)
    edge[b].append(a)

q = [0]
dep = [0] * N
fixed = [False] * N
while q:
    now = q.pop()
    fixed[now] = True
    for e in edge[now]:
        if fixed[e]:
            continue
        dep[e] = dep[now] + 1
        q.append(e)

ans = []
for _ in range(Q):
    c, d = map(lambda x: int(x) - 1, input().split())
    if (dep[c] + dep[d]) & 1:
        ans.append("Road")
    else:
        ans.append("Town")
print(*ans, sep="\n")
