from collections import defaultdict
import queue


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def even_or_odd_BFS(self, n):
        even_or_odd_list = [None] * (n + 1)
        e_or_o = "even"
        even_or_odd_list[1] = e_or_o
        que = queue.Queue()
        que.put(1)

        while not que.empty():
            e_or_o = "odd" if e_or_o == "even" else "even"
            qs = que.qsize()
            for _ in range(qs):
                r = que.get()
                for x in self.graph[r]:
                    if even_or_odd_list[x] == None:
                        even_or_odd_list[x] = e_or_o
                        que.put(x)
        return even_or_odd_list


n, q = map(int, input().split())
g = Graph()
for _ in range(n - 1):
    u, v = map(int, input().split())
    g.add_edge(u, v)
    g.add_edge(v, u)

even_or_odd_list = g.even_or_odd_BFS(n)

for _ in range(q):
    u, v = map(int, input().split())
    if even_or_odd_list[u] == even_or_odd_list[v]: print("Town")
    else: print("Road")
