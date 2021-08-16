N, Q = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(N - 1)]
xy = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(Q)]


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
                dist[i] = dist[label] + c
                stack += [i]
    return dist


distance = BFS(0, edges, N)

result = []
for a, b in xy:
    tar = distance[a] + distance[b]
    if tar % 2 == 0:
        result.append('Town')
    else:
        result.append('Road')
print(*result, sep='\n')
