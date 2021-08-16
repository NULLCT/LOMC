from collections import defaultdict, deque


def main():
    n, q = [int(x) for x in input().split()]
    graph = defaultdict(list)
    for i in range(n - 1):
        u, v = [int(x) for x in input().split()]
        graph[u].append(v)
        graph[v].append(u)
    color = [-1] * (n + 1)
    color[1] = 0
    queue = deque([1])
    while queue:
        node = queue.popleft()
        for v in graph[node]:
            if color[v] == -1:
                color[v] = 1 - color[node]
                queue.append(v)

    for i in range(q):
        a, b = [int(x) for x in input().split()]
        if color[a] == color[b]: print('Town')
        else: print('Road')


(main())
