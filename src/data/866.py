from collections import deque


def func():
    N, Q = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        G[a - 1].append(b - 1)
        G[b - 1].append(a - 1)

    que = deque()
    que.append((0, 0, -1))
    tmp = -1
    dist = [0] * N
    while que:
        v = que.popleft()
        for x in G[v[0]]:
            if x == v[2]:
                continue
            dist[x] = v[1] + 1
            que.append((x, v[1] + 1, v[0]))
    # print(dist)
    for _ in range(Q):
        c, d = map(int, input().split())
        if abs(dist[c - 1] - dist[d - 1]) % 2 == 0:
            print("Town")
        else:
            print("Road")


if __name__ == '__main__':
    func()
