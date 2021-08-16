from collections import deque


class Graph:
    def __init__(self):
        self.edges = {}

    def append_edge(self, sv, ev, weight=1):
        if sv in self.edges:
            self.edges[sv].append((ev, weight))
        else:
            self.edges[sv] = [(ev, weight)]

    def bfs(self, sv, N):
        dist = [-1] * N
        q = deque([])  # キュー
        q.append(sv)
        dist[sv] = 0
        connect_vtxs = []
        while len(q) > 0:
            p = q.popleft()  # キュー取りだし（先頭）
            connect_vtxs.append(p)
            if p not in self.edges:
                return [-1] * N, connect_vtxs
            for (ev, w) in self.edges[p]:
                if dist[ev] != -1:
                    continue
                q.append(ev)  # キュー追加
                dist[ev] = dist[p] + 1
        return dist, connect_vtxs


def main():
    N, Q = map(int, input().split())
    ab = [list(map(int, input().split())) for i in range(N - 1)]
    g = Graph()
    for i in range(len(ab)):
        a, b = ab[i]
        g.append_edge(a - 1, b - 1)
        g.append_edge(b - 1, a - 1)
    dist, connect_vtxs = g.bfs(0, N)

    for i in range(Q):
        c, d = map(int, input().split())
        if (dist[c - 1] + dist[d - 1]) % 2 == 0:
            print("Town")
        else:
            print("Road")


if __name__ == '__main__':
    main()
