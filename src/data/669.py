def main():
    n, qqqq = map(int, input().split())
    ab = [list(map(int, input().split())) for _ in [0] * (n - 1)]
    g = [[] for _ in [0] * n]
    [g[a - 1].append(b - 1) for a, b in ab]
    [g[b - 1].append(a - 1) for a, b in ab]
    root = 0  # 根
    d = [-1] * n  # 根からの距離
    d[root] = 0
    q = [root]
    cnt = 0
    while q:  # BFS
        cnt += 1
        qq = []
        while q:
            i = q.pop()
            for j in g[i]:
                if d[j] == -1:
                    d[j] = cnt
                    qq.append(j)
        q = qq

    for i in range(qqqq):
        c, dd = map(int, input().split())
        if (d[c - 1] + d[dd - 1]) % 2:
            print("Road")
        else:
            print("Town")


main()
