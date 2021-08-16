import sys

sys.setrecursionlimit(100000)

global city
global g


def search_d(c):
    global city
    global g
    for i in g[c]:
        if city[i] == -1:
            city[i] = 2 if city[c] == 1 else 1
            search_d(i)


def main():
    from sys import stdin
    readline = stdin.readline
    N, Q = map(int, input().split())
    list_graph = [[x - 1 for x in list(map(int,
                                           readline().split()))]
                  for _ in range(N - 1)]
    list_query = [[x - 1 for x in list(map(int,
                                           readline().split()))]
                  for _ in range(Q)]

    global city
    city = [-1] * N
    global g
    g = [[] * N for _ in range(N)]

    for e in list_graph:
        g[e[0]].append(e[1])
        g[e[1]].append(e[0])

    city[0] = 1
    search_d(0)

    for q in list_query:
        print("Town" if city[q[0]] == city[q[1]] else "Road")


if __name__ == '__main__':
    main()
