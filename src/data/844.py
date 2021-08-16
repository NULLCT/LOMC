def main():
    from collections import deque
    from sys import stdin
    input = stdin.readline
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in [0] * (N - 1):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        G[x].append(y)
        G[y].append(x)

    #各頂点の偶奇判定
    Q = deque()
    toured = [-1] * N
    Q.appendleft(0)
    toured[0] = 0
    dist = 0

    while len(Q) > 0:
        tmp = Q.popleft()
        for i in G[tmp]:
            if toured[i] == -1:
                toured[i] = (toured[tmp] + 1) % 2
                Q.append(i)

    for i in range(M):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        if (toured[x] + toured[y]) % 2 == 0:
            print("Town")
        else:
            print("Road")


main()
