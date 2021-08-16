import sys
import math
from collections import deque

sys.setrecursionlimit(10**6)
INF = float('inf')


def solve():
    n, q = map(int, input().split())

    graph = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * n

    logn = int(math.log(n, 2)) + 1
    pa = [[None for _ in range(n)] for _ in range(logn + 1)]
    depth = [None for _ in range(n)]

    def build():
        que = deque()
        que.append(0)
        depth[0] = 0
        c = [[] for _ in range(n)]
        while que:
            cur = que.popleft()
            visited[cur] = True

            for child in graph[cur]:
                if visited[child]:
                    continue
                depth[child] = depth[cur] + 1
                que.append(child)
                c[cur].append(child)

        for i in range(n):
            for child in c[i]:
                pa[0][child] = i
        for i in range(logn):
            for j in range(n):
                if pa[i][j] != None:
                    pa[i + 1][j] = pa[i][pa[i][j]]

    def query(u, v):
        def move(src, dst):
            return src, dst

        while depth[u] != depth[v]:
            if depth[v] < depth[u]:
                u, v = v, u
            d = depth[v] - depth[u]
            for k in range(logn):
                if d & 1:
                    move(v, pa[k][v])
                    v = pa[k][v]
                d = d >> 1
        for nk in range(logn):
            k = logn - nk - 1
            if pa[k][u] != pa[k][v]:
                move(u, pa[k][u])
                u = pa[k][u]
                move(v, pa[k][v])
                v = pa[k][v]
        if u == v:
            res = u
        else:
            move(u, pa[0][u])
            res = pa[0][u]

        return res

    depth[0] = 0
    build()

    ans = []
    for i in range(q):
        c, d = map(int, input().split())
        c -= 1
        d -= 1
        parent = query(c, d)
        if (depth[c] - depth[parent] + depth[d] - depth[parent]) % 2 == 0:
            ans.append('Town')
        else:
            ans.append('Road')

    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
