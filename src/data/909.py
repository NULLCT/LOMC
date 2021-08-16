#####################################
import atexit, io, sys, collections, math, heapq, fractions, copy, os, functools
import sys
import random
import collections

from io import BytesIO, IOBase

#####################################  python 3 START
BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
#####################################  python 3 END

n, qq = map(int, input().split())
adj = collections.defaultdict(list)
for _ in range(n - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
q = collections.deque([(1, 0, None)])
nadj = collections.defaultdict(list)
depth = [0 for _ in range(n + 1)]
while (q):
    u, d, parent = q.popleft()
    depth[u] = d
    for v in adj[u]:
        if v != parent:
            nadj[u].append(v)
            q.append((v, d + 1, u))

adj = nadj
t = []
first = {}


def euler(root, adj, t):
    if root not in first: first[root] = len(t)
    t.append((depth[root], root))
    for v in adj[root]:
        if v not in first: first[v] = len(t)
        t.append((depth[v], v))
        euler(v, adj, t)
        t.append((depth[v], v))


#euler(1, adj, t)
def tlca(u, v, root, adj):
    fi = min(first[u], first[v])
    li = max(first[u], first[v])
    return min(t[fi:li + 1])[1]


def lca(u, v, root, adj):
    if u == root:
        return u
    if v == root:
        return v
    if len(adj[root]) == 0:
        return 0
    temp = [lca(u, v, desc, adj) for desc in adj[root]]
    if sum(temp) == 0:
        return 0
    count = 0
    for val in temp:
        if val:
            count += 1
    if count == 1:
        for val in temp:
            if val:
                return val
    elif count == 2:
        return root
    return 0


def f(u, v, adj, depth):
    #l = lca(u,v,1,adj)

    #print (tlca(u,v,1,adj) == l)
    quantity = depth[u] + depth[v]
    #quantity += abs(depth[l] - depth[u])
    #quantity += abs(depth[l] - depth[v])
    return 'Road' if quantity % 2 else 'Town'


for _ in range(qq):
    u, v = map(int, input().split())
    print(f(u, v, adj, depth))
