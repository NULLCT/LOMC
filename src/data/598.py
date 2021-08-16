from collections import deque


def bfs(N, g):
    m = [-1] * (N + 1)
    m[1] = 0
    q = deque()
    q.append(1)
    while len(q) > 0:
        node = q.popleft()
        for child in g[node].children:
            if m[child] > -1:
                continue
            m[child] = m[node] + 1
            q.append(child)
    return m


class Node:
    def __init__(self, n):
        self.n = n
        self.children = []


def main():
    N, Q = map(int, input().split())
    g = [Node(i) for i in range(N + 1)]
    for i in range(N - 1):
        a, b = map(int, input().split())
        g[a].children.append(b)
        g[b].children.append(a)

    memo = bfs(N, g)
    for i in range(Q):
        c, d = map(int, input().split())
        if memo[c] % 2 == memo[d] % 2:
            print('Town')
        else:
            print('Road')


main()
