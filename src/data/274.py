import queue


def main():
    global N, distances

    N, Q = map(int, (input().split()))
    AB = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        AB[a - 1].append(b - 1)
        AB[b - 1].append(a - 1)

    colors = [-1] * N
    colors[0] = 0
    q = queue.Queue()
    q.put(0)

    while not q.empty():
        town_from = q.get()
        for town_to in AB[town_from]:
            if colors[town_to] == -1:
                colors[town_to] = 1 - colors[town_from]
                q.put(town_to)

    for _ in range(Q):
        c, d = map(int, input().split())
        if colors[c - 1] == colors[d - 1]:
            print('Town')
        else:
            print('Road')


if __name__ == '__main__':
    main()
