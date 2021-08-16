import heapq
from collections import defaultdict


def dijkstra(start, N, branches):
    """
    :param start:
    :param N: The number of nodes
    :param branches: dictionary, branches[src_node] = [(next_node, cost)]
    :return:
    """
    distance_heap = [(float('inf'), i) for i in range(N)]
    distance_heap[start] = (0, start)
    heapq.heapify(distance_heap)

    ways = {}

    dv = [-1] * N
    heap_is_empty = False
    most_close_node_id = most_close_node_distance = -1
    while True:
        while True:
            if len(distance_heap) == 0:
                heap_is_empty = True
                break
            most_close_node_distance, most_close_node_id = heapq.heappop(
                distance_heap)
            if dv[most_close_node_id] < 0:
                break
        if heap_is_empty:
            break

        dv[most_close_node_id] = most_close_node_distance
        # update heap (just add new distances)
        for branch in branches[most_close_node_id]:
            next_node, cost = branch
            # skip already processed nodes
            if dv[next_node] >= 0:
                continue
            distance = cost + most_close_node_distance
            heapq.heappush(distance_heap, (distance, next_node))

    return dv


def resolve():
    N, Q = [int(v) for v in input().split()]

    branches = defaultdict(list)
    for _ in range(N - 1):
        a, b = [int(v) - 1 for v in input().split()]
        branches[a].append((b, 1))
        branches[b].append((a, 1))

    dv = dijkstra(0, N, branches)
    for _ in range(Q):
        c, d = [int(v) - 1 for v in input().split()]
        if (dv[c] + dv[d]) % 2 == 0:
            print('Town')
        else:
            print('Road')


if __name__ == '__main__':
    resolve()
