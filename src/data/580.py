n, q = map(int, input().split())

from collections import deque

graph = []
visited = []

for i in range(n):
    tmp = []
    graph.append(tmp)

for i in range(n - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append(v)
    graph[v].append(u)

#print(graph)


def BFS(s, g):
    dist = [-1] * n

    Q = deque()
    Q.append(s)
    dist[s] = 0

    while len(Q) > 0:
        #キューの先頭の頂点を取り出してiとする
        i = Q.popleft()
        #頂点iに隣接する頂点を順番に見る
        #見ている頂点をiとする
        for j in graph[i]:
            #jが未訪問だったとき、jへの最短距離を更新して、キューの末尾に追加する
            if dist[j] == -1:
                dist[j] = dist[i] + 1
                Q.append(j)
            #print(dist,Q)

    #print(dist)
    return dist


x = BFS(0, n)

#print(x)

for i in range(q):
    s, g = map(int, input().split())
    s -= 1
    g -= 1
    if (x[s] + x[g]) % 2 == 0:
        print('Town')
    else:
        print('Road')
