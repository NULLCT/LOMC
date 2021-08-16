import sys

sys.setrecursionlimit(100000)

N, Q = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N - 1)]
CD = [list(map(int, input().split())) for _ in range(Q)]

# 各節点について、接続先節点のリストを作成
roads = [[] for _ in range(N)]
for a, b in AB:
    roads[a - 1].append(b - 1)
    roads[b - 1].append(a - 1)


class Dfs():
    def __init__(self, graphs, num):
        self.graphs = graphs
        self.times = [0] * num
        self.group = [[], []]
        self.time = 0
        self.queue = []
        self.gid = [0] * (num + 1)

    def __call__(self, start_pos):
        self.queue.append([start_pos, -1, 0])  #(current, previous, group)
        while self.queue:
            node_id, pre_node, group_id = self.queue.pop()
            self.group[group_id].append(node_id + 1)  #0index+1
            self.gid[node_id + 1] = group_id
            for next_id in self.graphs[node_id]:
                if not next_id == pre_node:
                    self.queue.append([next_id, node_id, group_id ^ 1])


dfs = Dfs(roads, N)

dfs(1)
for c, d in CD:
    if dfs.gid[c] == dfs.gid[d]:
        print("Town")
    else:
        print("Road")
