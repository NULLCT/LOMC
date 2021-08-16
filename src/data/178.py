def abc209d():
    from collections import deque
    n, Q = map(int, input().split())
    g = [list() for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        a, b = a - 1, b - 1
        g[a].append(b)
        g[b].append(a)
    c = [-1] * n
    q = deque([0])
    c[0] = 0
    while len(q) > 0:
        node = q.popleft()
        for nxt in g[node]:
            if c[nxt] != -1: continue
            c[nxt] = 1 - c[node]
            q.append(nxt)
    ans = []
    for _ in range(Q):
        a, b = map(int, input().split())
        a, b = a - 1, b - 1
        if c[a] == c[b]:
            ans.append("Town")
        else:
            ans.append("Road")
    for item in ans:
        print(item)


abc209d()
