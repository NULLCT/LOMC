def main():
    from collections import deque
    import sys
    input = sys.stdin.readline

    N, Q = map(int, input().split())

    G = tuple(list() for _ in range(N))
    for _ in range(N - 1):
        a, b = (int(x) - 1 for x in input().split())
        G[a].append(b)
        G[b].append(a)

    dist = [None] * N
    dist[0] = 0

    dq = deque()
    dq.append(0)
    while dq:
        v = dq.popleft()
        du = dist[v] ^ 1
        for u in G[v]:
            if dist[u] is not None:
                continue
            dist[u] = du
            dq.append(u)

    ans = []
    for _ in range(Q):
        c, d = (int(x) - 1 for x in input().split())
        if dist[c] == dist[d]:
            ans.append("Town")
        else:
            ans.append("Road")
    print(*ans, sep='\n')


if __name__ == "__main__":
    main()

# 距離偶数なら町、奇数なら道
