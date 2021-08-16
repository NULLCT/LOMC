def solv():
    N, Q = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(N - 1)]
    query = [list(map(int, input().split())) for i in range(Q)]

    #print(edges)
    #print(query)
    roots_color = [-1] * N

    def BFS(edges, N, roots_color):
        # ノードリスト
        roots = [[] for i in range(N)]
        # 辺を取り出す
        for a, b in edges:
            roots[a - 1] += [(b - 1, 1)]
            roots[b - 1] += [(a - 1, 1)]
        stack = []
        roots_color[0] = 0
        stack.append(0)
        now_color = roots_color[0]
        while stack:
            label = stack.pop(-1)
            now_color = roots_color[label]
            for i, cost in roots[label]:
                if roots_color[i] == -1:
                    roots_color[i] = now_color ^ 1
                    stack += [i]
        return roots_color

    roots_color = BFS(edges, N, roots_color)

    #print(roots_color)

    for x, y in query:
        if roots_color[x - 1] == roots_color[y - 1]:
            print('Town')
        else:
            print('Road')


if __name__ == "__main__":
    solv()
