import sys


def main():
    sys.setrecursionlimit(1000000)

    N, Q = [int(x) for x in input().split()]

    # 隣接リスト形式でグラフをつくる
    # 重み付きの場合は、[行き先, weight]をそれぞれの行に持たせれば良い。
    graph = [[] for i in range(N)]
    for i in range(N - 1):
        a, b = [int(x) for x in input().split()]
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    queries = []
    for i in range(Q):
        c, d = [int(x) for x in input().split()]
        queries.append([c - 1, d - 1])

    distances = [-1 for x in range(N)]
    distances[0] = 0
    dfs(graph, distances, 0)

    for query in queries:
        if (distances[query[0]] - distances[query[1]]) % 2 == 0:
            print("Town")
        else:
            print("Road")


def dfs(graph, distances, current_node):
    next_nodes = graph[current_node]
    for next_node in next_nodes:
        if distances[next_node] < 0:
            distances[next_node] = distances[current_node] + 1
            dfs(graph, distances, next_node)


if __name__ == "__main__":
    main()
