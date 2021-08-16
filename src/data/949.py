def main():
    import sys
    input = sys.stdin.readline
    from collections import defaultdict, deque
    n, q = map(int, input().split())

    G = defaultdict(list)
    for _ in range(n - 1):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    # BFS
    dist = {}
    que = deque()
    dist[1] = 0
    que.append(1)
    while len(que) > 0:
        v = que.popleft()
        for x in G[v]:
            if x in dist:
                continue
            dist[x] = dist[v] + 1
            que.append(x)

    for _ in range(q):
        c, d = map(int, input().split())
        t = dist[c] - dist[d]
        print('Town' if t % 2 == 0 else 'Road')


main()
