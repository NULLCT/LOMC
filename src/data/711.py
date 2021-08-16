def main():
    import queue
    n, q = (int(x) for x in input().split())
    g = [[] for _ in range(n)]
    for i in range(n - 1):
        a, b = (int(x) - 1 for x in input().split())
        g[a].append(b)
        g[b].append(a)
    que = queue.Queue()
    color = [-1] * n
    color[0] = 0
    que.put(0)
    while not que.empty():
        t = que.get()
        for i in g[t]:
            if color[i] == -1:
                color[i] = 1 - color[t]
                que.put(i)
    for i in range(q):
        c, d = (int(x) - 1 for x in input().split())
        print("Town" if color[c] == color[d] else "Road")


if __name__ == '__main__':
    main()
