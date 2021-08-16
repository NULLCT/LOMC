from collections import defaultdict
import sys


def input():
    return sys.stdin.readline()[:-1]


class MyGraph:
    def __init__(self):

        # ノードの集合
        self.nodes = set()
        # 各ノードに隣接している(そこからたどり着ける)ノードの集合をまとめた辞書
        self.connections = defaultdict(set)

        # 0:未到達
        # 1:白
        # 2:黒
        self.color = defaultdict(int)

    def add_nodes(self, nodes):
        # 頂点の集合(またはリストなど)を加えます。
        for node in nodes:
            if node not in self.nodes:
                self.nodes.add(node)

    def add_edges(self, edges):
        # 辺を加えます。辺は(from , to )の形のタプルにすること。
        # 例：graph.add_edges([ (1,2) , (1,3) , (2,4) ])
        for f, t in edges:
            # f : from     t : to
            self.connections[f].add(t)
            self.connections[t].add(f)

    def nuriwake(self):
        start_node = 1

        job_stack = [start_node]
        self.color[start_node] = 1

        while job_stack:
            node = job_stack.pop()
            node_c = self.color[node]
            if node_c == 1:
                next_color = 2
            else:
                next_color = 1

            for next_node in self.connections[node]:
                if self.color[next_node] == 0:
                    self.color[next_node] = next_color
                    job_stack.append(next_node)


def main():
    n, q = tuple(map(int, input().split()))
    nodes = list(range(1, n + 1))
    edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

    g = MyGraph()
    g.add_nodes(nodes)
    g.add_edges(edges)
    g.nuriwake()

    ans = []
    for _ in range(q):
        c, d = tuple(map(int, input().split()))
        if g.color[c] == g.color[d]:
            ans.append('Town')
        else:
            ans.append('Road')

    print('\n'.join(ans))


if __name__ == '__main__':
    main()
