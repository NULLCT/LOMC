from collections import deque


def main():
    N, Q = map(int, input().split())
    G = [[] for i in range(N)]
    Query = []
    for i in range(N - 1):
        a, b = map(int, input().split())
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)

    for i in range(Q):
        c, d = map(int, input().split())
        Query.append([c, d])

    trace = [-1 for i in range(N)]
    layer = 0

    q = deque()
    s = 0
    trace[s] = layer
    q.append([s, layer])

    while len(q) > 0:
        s_layer = q.popleft()
        s = s_layer[0]
        layer = s_layer[1]
        for i in range(len(G[s])):
            s_ = G[s][i]
            if trace[s_] == -1:
                trace[s_] = layer + 1
                q.append([G[s][i], layer + 1])

    for i in range(Q):
        c = Query[i][0] - 1
        d = Query[i][1] - 1
        if (trace[d] - trace[c]) % 2 == 0:
            print("Town")
        else:
            print("Road")


if __name__ == "__main__":
    main()
