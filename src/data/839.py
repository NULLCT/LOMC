from collections import deque


def resolve():
    N, Q = map(int, input().split())
    G = [[] for i in range(N)]
    color = [0 for i in range(N)]
    for i in range(N - 1):
        a, b = map(int, input().split())
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)

    que = deque([0])
    color[0] = 1
    while len(que):
        p = que.popleft()
        for q in G[p]:
            if color[q] == 0:
                color[q] = -color[p]
                que.append(q)

    for i in range(Q):
        c, d = map(int, input().split())
        if color[c - 1] == color[d - 1]:
            print("Town")
        else:
            print("Road")


resolve()
