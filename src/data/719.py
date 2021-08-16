from collections import deque


def bfs(e, n):
    path = deque()
    cost = [0] * n
    path.append(0)
    while path:
        now = path.popleft()
        for next in e[now]:
            if cost[next] == 0:
                cost[next] = cost[now] + 1
                path.append(next)
    return cost


def main():
    N, Q = map(int, input().split())
    e = [[] for _ in range(N)]
    for i in range(N - 1):
        a, b = map(int, input().split())
        e[a - 1].append(b - 1)
        e[b - 1].append(a - 1)
    #前処理なし??
    cost = bfs(e, N)
    for k in range(Q):
        c, d = map(int, input().split())
        print("Road") if cost[c - 1] % 2 != cost[d - 1] % 2 else print("Town")


main()
