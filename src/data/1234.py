class FastTree:
    def __init__(self, graph):
        self.n = len(graph)
        self.ancestor_table = [None] * self.n

        stack = [[0, -1, 0]]

        while stack:
            data = stack[-1]
            cur, parent, index = data
            children = graph[cur]
            if index >= len(children):
                stack.pop()
            else:
                if index == 0:
                    depth = len(stack)
                    table = []
                    i = 1
                    while i < depth:
                        table.append(stack[depth - i - 1][0])
                        i *= 2
                    self.ancestor_table[cur] = (depth - 1, table)

                child = children[index]
                if parent != child:
                    stack.append([child, cur, 0])
                data[2] += 1

    def get_depth(self, c):
        return self.ancestor_table[c][0]


N, Q = map(int, input().split())

graph = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

ft = FastTree(graph)

for _ in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    dc = ft.get_depth(c)
    dd = ft.get_depth(d)
    #	x = ft.get_common_ancestor(c, d)
    #	dx = ft.get_depth(x)
    #	l = (dc - dx) + (dd - dx)
    #	print(dx, dc, dd)
    l = dc + dd
    if l % 2 == 1:
        print("Road")
    else:
        print("Town")
