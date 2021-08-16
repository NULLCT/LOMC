def resolve():
    N, Q = map(int, input().split())
    from collections import defaultdict, deque
    path = defaultdict(list)
    for i in range(N - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        path[a].append(b)
        path[b].append(a)
    nxt = deque([0])
    depth = [0] * N
    arv = [-1] * N
    arv[0] = 1
    while nxt:
        n = nxt.popleft()
        d = depth[n]
        for i in path[n]:
            if arv[i] == -1:
                arv[i] = 1
                depth[i] = d + 1
                nxt.append(i)

    for _ in range(Q):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        if (depth[c] + depth[d]) % 2 == 0:
            print("Town")
        else:
            print("Road")


resolve()
