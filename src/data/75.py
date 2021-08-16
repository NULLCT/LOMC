def main():
    N, Q = map(int, input().split())

    import collections
    tree = collections.defaultdict(list)
    for _ in range(N - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        tree[a].append(b)
        tree[b].append(a)

    RED = 1
    BLACK = 2
    colors = [None] * N

    # DFS for color
    stack = [(0, RED)]
    while stack:
        u, c = stack.pop()
        colors[u] = c
        next_c = BLACK if c == RED else RED
        for v in tree[u]:
            if not colors[v]:
                stack.append((v, next_c))

    for _ in range(Q):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        if colors[c] == colors[d]:
            print('Town')
        else:
            print('Road')


if __name__ == "__main__":
    main()
