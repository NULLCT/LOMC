from heapq import heappush, heappop


class Graph():
    def __init__(self, n, INF=10**18):
        self.n = n
        self.INF = INF
        self.edges = [[] for _ in range(n)]

    def add_edge(self, u, v, w, directed=True):
        self.edges[u].append([v, w])
        if not directed:
            self.edges[v].append([u, w])

    def dijkstra(self, s):
        dist = [self.INF] * self.n
        hq = [(0, s)]
        dist[s] = 0

        while hq:
            cur = heappop(hq)[1]
            for nxt, cost in self.edges[cur]:
                if dist[nxt] > dist[cur] + cost:
                    dist[nxt] = dist[cur] + cost
                    heappush(hq, (dist[nxt], nxt))
        return dist

    def bfs(self, s):
        dist = [self.INF] * self.n
        que = [s]
        dist[s] = 0

        for cur in que:
            for nxt, w in self.edges[cur]:
                assert w == 1
                if dist[nxt] != self.INF:
                    continue
                dist[nxt] = dist[cur] + 1
                que.append(nxt)
        return dist


N, Q = map(int, input().split())
AB = [[*map(int, input().split())] for _ in range(N - 1)]
CD = [[*map(int, input().split())] for _ in range(Q)]
G = Graph(N)

for a, b in AB:
    G.add_edge(a - 1, b - 1, 1, directed=False)

dist = G.bfs(0)

for c, d in CD:
    c, d = c - 1, d - 1
    print('Road' if (dist[c] + dist[d]) & 1 else 'Town')
