from collections import defaultdict, deque


def solve(N, graph):
    # BFS
    queue = deque()
    for key, value in graph.items():
        if len(value) == 1:
            queue.append((key, BLUE))
            break
    while queue:
        size = len(queue)
        for i in range(size):
            curNode, color = queue.popleft()
            colorTable[curNode] = color
            for nei in graph[curNode]:
                graph[nei].remove(curNode)
                queue.append((nei, -color))


BLUE, RED = 1, -1
N, Q = map(int, input().split())

# Build graph
graph = defaultdict(list)
queries = []
for i in range(N - 1):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

# Build color table
colorTable = [None] * (N + 1)
solve(N, graph)

# Return value
for i in range(Q):
    C, D = map(int, input().split())
    if colorTable[C] == colorTable[D]:
        print("Town")
    else:
        print("Road")
