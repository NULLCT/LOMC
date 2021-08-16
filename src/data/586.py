from collections import deque


def main():
    # input
    N, Q = map(int, input().split())
    abs = [[*map(int, input().split())] for _ in range(N - 1)]
    cds = [[*map(int, input().split())] for _ in range(Q)]

    # compute
    adjss = [[] for _ in range(N)]
    for a, b in abs:
        a -= 1
        b -= 1
        adjss[a].append(b)
        adjss[b].append(a)

    ## BFS
    deq = deque([0])
    dist = [-1] * N
    dist[0] = 0
    while deq:
        v = deq.popleft()
        for i in adjss[v]:
            if dist[i] == -1:
                dist[i] = 1 - dist[v]
                deq.append(i)

    # output
    for c, d in cds:
        c -= 1
        d -= 1
        if dist[c] == dist[d]:
            print('Town')
        else:
            print('Road')


if __name__ == '__main__':
    main()
