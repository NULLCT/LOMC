#D
N, Q = map(int, input().split())
#AB=[list(map(int,input().split())) for i in range(N-1)]
#CD=[list(map(int,input().split())) for i in range(Q)]
AB = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    AB[a].append(b)
    AB[b].append(a)

from collections import deque
#print(AB)


def tree_length(x, n, graph):
    #頂点xから全頂点への距離をはかる。0-indexed
    #木は[[1,2],[0,3],...]のような形で与える
    dist = [-1] * n
    dist[x] = 0
    check = [False] * n
    dq = deque([x])
    for i in range(n):
        while len(dq) > 0:
            s = dq.popleft()
            check[s] = True
            for j in range(len(graph[s])):
                if check[graph[s][j]] == False:
                    dq.append(graph[s][j])
                if dist[graph[s][j]] == -1:
                    dist[graph[s][j]] = dist[s] + 1
    return dist


TL = tree_length(0, N, AB)
for i in range(Q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    if (TL[l] + TL[r]) % 2 == 0:
        print('Town')
    else:
        print('Road')
