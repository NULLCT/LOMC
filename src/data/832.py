from sys import stdin

input = stdin.readline

N, Q = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(N - 1)]
xy = [list(map(int, input().split())) for i in range(Q)]


def BFS(K, edges, N):
    roots = [[] for i in range(N)]
    for a, b in edges:
        roots[a - 1] += [(b - 1, 1)]
        roots[b - 1] += [(a - 1, 1)]
    dist = [-1] * N
    stack = []
    stack.append(K)
    dist[K] = 0
    while stack:
        label = stack.pop(-1)
        for i, c in roots[label]:
            if dist[i] == -1:
                dist[i] = dist[label] + 1
                stack += [i]
    return dist


distance = BFS(1, edges, N)
for i in range(Q):
    print(['Town',
           'Road'][(distance[xy[i][0] - 1] + distance[xy[i][1] - 1]) % 2])
