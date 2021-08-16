import sys
from collections import defaultdict, deque


def main(f):
    N, Q = list(map(int, f.readline().split()))
    children = [[] for _ in range(N + 1)]
    for i in range(1, N):
        a, b = list(map(int, f.readline().split()))
        children[a].append(b)
        children[b].append(a)

    parity = [None] * (N + 1)

    q = deque()
    q.append((1, -1))
    while q:
        i, parent = q.popleft()
        if parent == -1:
            parity[i] = 1
        else:
            parity[i] = -parity[parent]
        for j in children[i]:
            if j == parent:
                continue
            q.append((j, i))

    for i in range(1, Q + 1):
        c, d = list(map(int, f.readline().split()))
        if parity[c] == parity[d]:
            print('Town')
        else:
            print('Road')


main(sys.stdin)
