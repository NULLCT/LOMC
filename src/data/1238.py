from collections import deque


def main():
    N, Q = map(int, input().split())
    path_dat = [list(map(int, input().split())) for _ in range(N - 1)]
    queries = [list(map(int, input().split())) for _ in range(Q)]

    paths = [[] for _ in range(N)]
    for a, b in path_dat:
        a -= 1
        b -= 1
        paths[a].append(b)
        paths[b].append(a)

    dist = [-1] * N
    dist[0] = 0
    queue = deque([0])
    while queue:
        now = queue.popleft()
        for nxt in paths[now]:
            if dist[nxt] != -1:
                continue
            dist[nxt] = dist[now] + 1
            queue.append(nxt)

    for c, d in queries:
        c -= 1
        d -= 1
        tmp = dist[c] + dist[d]
        if tmp % 2 == 0:
            print('Town')
        else:
            print('Road')


main()
