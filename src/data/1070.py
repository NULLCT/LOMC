# Rishabh Rao (https://github.com/rishabhrao)

import sys

MOD = 1000000007


def inp():
    return sys.stdin.readline().strip()


def ii():
    return int(inp())


def iis():
    return [int(i) for i in inp().split()]


n, q = iis()

undir_nodes = [[] for _ in range(n + 1)]
node_depths = [0 for _ in range(n + 1)]
visited_nodes = [0 for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = iis()
    undir_nodes[u].append(v)
    undir_nodes[v].append(u)

stack_of_nodes = [1]
len_stack = 1
while len_stack:
    curr = stack_of_nodes.pop()
    len_stack -= 1
    visited_nodes[curr] = 1
    for child in undir_nodes[curr]:
        if not visited_nodes[child]:
            node_depths[child] = node_depths[curr] + 1
            stack_of_nodes.append(child)
            len_stack += 1

for _ in range(q):
    c, d = iis()
    print("Road" if abs(node_depths[c] - node_depths[d]) % 2 else "Town")
