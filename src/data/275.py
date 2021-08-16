from collections import deque


def bfs(routes, n, a, b):
    visited = [False for _ in range(n + 1)]

    deq = deque([(a, 0)])
    while deq:
        v = deq.popleft()
        for u in routes[v[0]]:
            if u == b:
                return v[1]
            if visited[u] == False:
                visited[u] = True
                deq.append((u, v[1] + 1))


def main():
    n, q = map(int, input().split())
    routes = [[] for _ in range(n + 1)]
    costs = [0 for _ in range(n + 1)]

    for _ in range(n - 1):
        a, b = map(int, input().split())
        routes[a].append(b)
        routes[b].append(a)

    # for i in range(n):
    #     for j in range(n):
    #         res = bfs(routes, n, i+1, j+1)
    #         costs[i+1] = res % 2
    #         costs[j+1] = res % 2
    deq = deque([(1, 0)])
    visited = [False for _ in range(n + 1)]
    while deq:
        v = deq.popleft()
        for u in routes[v[0]]:
            if visited[u] == False:
                visited[u] = True
                costs[u] = v[1] % 2
                deq.append((u, v[1] + 1))

    for _ in range(q):
        a, b = map(int, input().split())
        if costs[a] != costs[b]:
            print("Road")
        else:
            print("Town")


main()
