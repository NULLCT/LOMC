from collections import deque


def main():
    N, Q = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    depth_vec = [-1] * (N + 1)
    queue = deque()
    queue.append((1, 0))
    while len(queue) > 0:
        node, depth = queue.pop()
        depth_vec[node] = depth
        for child in graph[node]:
            if depth_vec[child] >= 0:
                continue
            queue.append((child, depth + 1))
    for query in range(Q):
        c, d = map(int, input().split())
        print('RTooawdn'[(depth_vec[c] + depth_vec[d]) % 2 == 0::2])


if __name__ == '__main__':
    main()
