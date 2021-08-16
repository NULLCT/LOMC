from collections import deque


def getDist(n, graph, rootNum) -> list:
    # print("getdist")
    # print("n", n)
    # print("m", m)
    dist = list()
    dist = [-1] * (n + 1)
    dist[0] = 0
    dist[rootNum] = 0
    # print(dist)

    d = deque()
    d.append(rootNum)

    while d:
        v = d.popleft()
        for i in graph[v]:
            if dist[i] != -1:
                continue
            dist[i] = dist[v] + 1
            d.append(i)

    ans = dist[1:]
    # print(*ans, sep="\n")
    return ans


def solve():

    N, Q = map(int, input().split())

    n, m = N, N - 1

    graph = [[] for _ in range(n + 1)]

    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    # print("n", n)
    # print("m", m)

    DD = list()
    # for i in range(N):
    for i in range(1):
        nnn = i + 1
        # print("rootNum", nnn, getDist(nnn))
        DD.append(getDist(n, graph, nnn))

    for i in range(Q):
        a, b = map(int, input().split())
        # print("Q:", a, b)
        # print(a-1, b)
        # print(DD)
        # assert DD[a-1]
        # assert DD[a-1][b-1]
        # if DD[a-1][b-1] % 2 == 1:
        #     print("Road")
        # else:
        #     print("Town")
        if (DD[0][a - 1] + DD[0][b - 1]) % 2 == 1:
            print("Road")
        else:
            print("Town")


solve()
