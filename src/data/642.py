import sys

sys.setrecursionlimit(10**6)

n, q = map(int, input().split())

edges = [[] for _ in range(n)]

for a, b in (map(int, input().split()) for _ in range(n - 1)):
    a, b = a - 1, b - 1
    edges[a].append(b)
    edges[b].append(a)

flags = [False for _ in range(n)]
marked = [False for _ in range(n)]


def mark(i, flag):
    if marked[i]:
        return
    else:
        flags[i] = flag
        marked[i] = True
        for next in edges[i]:
            mark(next, not flag)


mark(0, False)
for c, d in (map(int, input().split()) for _ in range(q)):
    c, d = c - 1, d - 1
    if flags[c] == flags[d]:
        print("Town", flush=False)
    else:
        print("Road", flush=False)
