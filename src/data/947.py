from collections import defaultdict


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}'
                         for r, m in self.all_group_members().items())


n, q = map(int, input().split())
elist = [[] for i in range(n)]

for i in range(n - 1):
    a, b = map(int, input().split())
    elist[a - 1].append(b - 1)
    elist[b - 1].append(a - 1)
haji = 0
for i in range(n):
    if len(elist[i]) == 1:
        haji = i
        break
fukasa = [0 for i in range(n)]
import heapq

node_heap = []
heapq.heappush(node_heap, [haji])
done = [True] * n
while node_heap:
    tmp = heapq.heappop(node_heap)
    cur_node = tmp[0]

    for e in elist[cur_node]:
        if done[e]:
            fukasa[e] = fukasa[cur_node] + 1
            heapq.heappush(node_heap, [e])
    done[cur_node] = False
#print(fukasa)

for i in range(q):
    c, d = map(int, input().split())
    if (fukasa[c - 1] - fukasa[d - 1]) % 2 == 0:
        print("Town")
    else:
        print("Road")
