import queue


def main():
    N, Q = [int(x) for x in input().split()]

    graph = [[] for i in range(N)]
    for i in range(N - 1):
        a, b = [int(x) for x in input().split()]
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    queries = []
    for i in range(Q):
        c, d = [int(x) for x in input().split()]
        queries.append([c - 1, d - 1])

    distances = bfs(graph, 0)

    for query in queries:
        if (distances[query[0]] - distances[query[1]]) % 2 == 0:
            print("Town")
        else:
            print("Road")


def bfs(graph, first_node):
    que = queue.Queue()
    que.put(first_node)
    distances = [-1 for x in range(len(graph))]
    distances[first_node] = 0

    while not que.empty():
        current_node = que.get()
        current_distance = distances[current_node]

        for next_node in graph[current_node]:
            if distances[next_node] < 0:
                que.put(next_node)
                distances[next_node] = current_distance + 1

    return distances


if __name__ == "__main__":
    main()
