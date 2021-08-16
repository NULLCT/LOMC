from collections import defaultdict
from collections import deque

n, q = map(int, input().split())

bi = defaultdict(int)

graph = [[] for _ in range(n)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)
    graph[b - 1].append(a - 1)

bi[0] = 0
next_nodes = deque()
visited = set()

next_nodes.append(0)

while next_nodes:
    current = next_nodes.popleft()
    if bi[current] == 0:
        for next_node in graph[current]:
            if next_node in visited:
                pass
            else:
                next_nodes.append(next_node)
                visited.add(next_node)
                bi[next_node] = 1
    if bi[current] == 1:
        for next_node in graph[current]:
            if next_node in visited:
                pass
            else:
                next_nodes.append(next_node)
                visited.add(next_node)
                bi[next_node] = 0

for _ in range(q):
    c, d = map(int, input().split())
    if bi[c - 1] == bi[d - 1]:
        print('Town')
    else:
        print('Road')
