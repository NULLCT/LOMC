from collections import defaultdict, deque

distances = {}


def depth(edges, n):
    visited = [0] * (n + 1)
    distance = [0] * (n + 1)

    # queue to do BFS.
    Q = deque()
    distance[1] = 0

    Q.append(1)
    visited[1] = True
    while Q:
        x = Q.popleft()

        for i in edges[x]:
            if visited[i]:
                continue

            distance[i] = distance[x] + 1
            Q.append(i)
            visited[i] = 1
    return distance


n, q = map(int, input().split())
graph = defaultdict(list)
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

depths = depth(graph, n)

for _ in range(q):
    c, d = map(int, input().split())
    dist = depths[c] - depths[d]
    if dist % 2 == 1:
        print('Road')
    else:
        print('Town')
