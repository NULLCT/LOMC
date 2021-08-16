from collections import deque

n = 0
m = 0


# input:Graph G and start vertex s
def bfs(G, s) -> list:
    # initialize
    que = deque()
    dist = [-1] * n
    dist[s] = 0
    que.append(s)

    while len(que) != 0:
        v = que.popleft()

        for x in G[v]:
            if dist[x] != -1:
                continue

            dist[x] = dist[v] + 1
            que.append(x)

    return dist


if __name__ == "__main__":
    n, q = map(int, input().split())
    ans_lis = []
    m = n - 1
    Graph = [[] for _ in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        # 1-start
        a -= 1
        b -= 1
        Graph[a].append(b)
        Graph[b].append(a)
    dis = bfs(Graph, 0)
    for j in range(q):
        fm, to = map(int, input().split())
        fm -= 1
        to -= 1
        dis_fm = dis[fm]
        dis_to = dis[to]
        if dis_fm % 2 == dis_to % 2:
            ans_lis.append("Town")
        else:
            ans_lis.append("Road")
    for j in ans_lis:
        print(j)
