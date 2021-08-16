import sys

input = sys.stdin.readline


def main():
    def is_bipartite(graph):
        n = len(graph)
        color = [-1] * n

        for start in range(n):
            if color[start] == -1:
                color[start] = 0
                stack = [start]

                while stack:
                    parent = stack.pop()

                    for child in graph[parent]:
                        if color[child] == -1:
                            color[child] = 1 - color[parent]
                            stack.append(child)
                        elif color[parent] == color[child]:
                            return False, color

        return color

    n, q = map(int, input().split())

    g = [[] for _ in range(n)]

    for _ in range(n - 1):
        a, b = map(int, input().split())
        g[a - 1].append(b - 1)
        g[b - 1].append(a - 1)

    c = is_bipartite(g)

    for _ in range(q):
        a, b = map(int, input().split())
        if c[a - 1] == c[b - 1]:
            print("Town")
        else:
            print("Road")


main()
