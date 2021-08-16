import sys
import math
import collections

sys.setrecursionlimit(500 * 500)


def main():

    input = sys.stdin.readline

    N, Q = map(int, input().split())

    global town_road
    global town

    town_road = [[] for _ in range(N)]
    town = [-1] * N

    for _ in range(N - 1):
        a, b = map(int, input().split())
        a = a - 1
        b = b - 1

        town_road[a].append(b)
        town_road[b].append(a)

    query = []
    for _ in range(Q):
        c, d = map(int, input().split())

        c = c - 1
        d = d - 1

        query.append([c, d])

    dfs(0, 0)

    for c, d in query:
        if town[c] == town[d]:
            print("Town")
        else:
            print("Road")


def dfs(check_town, before_town):
    if town[check_town] == -1:
        if before_town == 0:
            town[check_town] = 1
        else:
            town[check_town] = 0
        for check in town_road[check_town]:
            dfs(check, town[check_town])
    return


if __name__ == "__main__":
    main()
