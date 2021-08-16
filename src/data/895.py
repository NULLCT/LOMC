class Node:
    def __init__(self, i):
        self.id = i
        self.adj_list = list()
        self.color = -1


class Graph:
    def __init__(self, size):
        self.node_num = size + 1
        self.node_list = [Node(i) for i in range(self.node_num)]

    def add_edge(self, a, b):
        a_node = self.node_list[a]
        b_node = self.node_list[b]
        a_node.adj_list.append(b_node)
        b_node.adj_list.append(a_node)

    def node(self, idx):
        return self.node_list[idx]

    def coloring(self):
        v_node = self.node_list[1]
        c = 0
        v_node.color = c
        queue = list()
        queue.append(v_node)
        while len(queue) > 0:
            c = (c + 1) % 2
            queue2 = list()
            for v_node in queue:
                for u_node in v_node.adj_list:
                    if u_node.color == -1:
                        u_node.color = c
                        queue2.append(u_node)
            queue = queue2

    def shortest_path(self, a, b):
        a_node = self.node_list[a]
        b_node = self.node_list[b]
        if a_node.color == b_node.color:
            return 0
        else:
            return 1


n, q = map(int, input().split())

G = Graph(n)
for _ in range(n - 1):
    a, b = map(int, input().split())
    G.add_edge(a, b)
G.coloring()
for _ in range(q):
    c, d = map(int, input().split())
    if G.shortest_path(c, d):
        print('Road')
    else:
        print('Town')
