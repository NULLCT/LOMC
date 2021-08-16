import sys
from collections import defaultdict, deque


def main(f):
    global children, parity
    mod = 10**9 + 7
    N, Q = list(map(int, f.readline().split()))
    children = [[] for _ in range(N + 1)]
    parity = [None] * (N + 1)
    for i in range(1, N):
        a, b = list(map(int, f.readline().split()))
        children[a].append(b)
        children[b].append(a)

    q = deque()

    parity[1] = 1
    q.append(1)
    while q:
        i = q.popleft()
        for j in children[i]:
            if parity[j] == None:
                parity[j] = -parity[i]
                q.append(j)

    for i in range(1, Q + 1):
        c, d = list(map(int, f.readline().split()))
        if parity[c] == parity[d]:
            print('Town')
        else:
            print('Road')


main(sys.stdin)
