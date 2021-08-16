def euler_tour(s):
    stack = [~s, s]
    t, d = 0, 0
    depth, first_visit, last_visit, tour = [0] * N, [0] * N, [0] * N, []
    parent, seen = [None] * N, [False] * N
    parent[s] = -1
    depth[s] = 0
    seen[s] = True

    while stack:
        u = stack.pop()
        if u >= 0:
            t += 1
            first_visit[u] = t
            tour.append(u)
            for v in G[u]:
                if seen[v]:
                    continue
                else:
                    seen[v] = True
                depth[v] = depth[u] + 1
                parent[v] = u
                stack.append(~v)
                stack.append(v)
        else:
            t += 1
            last_visit[u] = t
            tour.append(~u)
    return depth, first_visit, last_visit, tour


N, Q = map(int, input().split())
G = [[] for i in range(N)]
for i in range(N - 1):
    A, B = map(int, input().split())
    A, B = A - 1, B - 1
    G[A].append(B)
    G[B].append(A)

depth, first_visit, last_visit, tour = euler_tour(0)
for i in range(Q):
    C, D = map(int, input().split())
    C, D = C - 1, D - 1
    if (depth[C] - depth[D]) % 2 == 0:
        print("Town")
    else:
        print("Road")