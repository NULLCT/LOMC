from collections import deque
import sys

input = sys.stdin.readline


class Node(object):
    def __init__(self, index, nears):
        self.index = index
        self.nears = nears
        self.visit = -1


def main():
    n, q = map(int, input().split())
    g = [[] for _ in range(n)]

    for _ in range(n - 1):
        a, b = map(int, input().split())
        g[a - 1].append(b - 1)
        g[b - 1].append(a - 1)

    nodes = []
    for i in range(n):
        nodes.append(Node(i, g[i]))

    queue = deque()
    queue.append(nodes[0])
    nodes[0].visit = 0

    while queue:
        node = queue.popleft()
        nears = node.nears
        x = node.visit + 1
        for near in nears:
            if nodes[near].visit == -1:
                nodes[near].visit = x
                queue.append(nodes[near])

    for _ in range(q):
        c, d = map(int, input().split())

        if nodes[c - 1].visit % 2 == nodes[d - 1].visit % 2:
            print('Town')
        else:
            print('Road')


if __name__ == '__main__':
    main()
