from collections import deque


def D():
    N, Q = map(int, input().split())
    dist = [[] for i in range(N + 1)]
    for i in range(N - 1):
        a, b = map(int, input().split())
        dist[b].append(a)
        dist[a].append(b)
    #スタートsとして、ゴールを1にしたときの、距離（偶数=0,奇数=1)
    que = deque()
    que.append(1)
    vivited = [False] * (N + 1)
    vivited[1] = True
    counter = [0] * (N + 1)
    n = 0

    while que:
        now = que.popleft()
        for to in dist[now]:
            if vivited[to] == False:
                counter[to] = counter[now] + 1
                vivited[to] = True
                que.append(to)
    for i in range(Q):
        c, d = map(int, input().split())
        if (counter[c] + counter[d]) % 2 == 0:
            print('Town')
        else:
            print('Road')


D()
