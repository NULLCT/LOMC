import sys
import math
import heapq


def input():
    return sys.stdin.readline().rstrip()


def RL():
    return map(int, input().split())


def main():
    N, Q = RL()
    ROOT = [[] for _ in range(N)]
    for i in range(N - 1):
        a, b = RL()
        a -= 1
        b -= 1
        ROOT[a].append(b)
        ROOT[b].append(a)

    q = [0]
    GRID = [3] * N
    GRID[0] = 0
    while q:
        p = q.pop()

        for j in ROOT[p]:
            if GRID[j] == 3:
                GRID[j] = 1 - GRID[p]
                q.append(j)

    for i in range(Q):
        a, b = RL()
        a -= 1
        b -= 1
        if GRID[a] == GRID[b]:
            print("Town")
        else:
            print("Road")


if __name__ == "__main__":
    main()
