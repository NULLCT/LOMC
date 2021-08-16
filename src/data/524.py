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

    color = [None] * N
    color[0] = 0

    dq = deque()
    dq.append(0)
    while dq:
        v = dq.popleft()
        nc = color[v] ^ 1
        for u in G[v]:
            if color[u] is None:
                color[u] = nc
                dq.append(u)

    ans = []
    for _ in range(Q):
        c, d = (int(x) - 1 for x in input().split())
        msg = "Road" if color[c] ^ color[d] else "Town"
        ans.append(msg)
    print(*ans, sep='\n')


if __name__ == "__main__":
    main()
