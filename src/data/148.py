import queue


def main():
    N, Q = map(int, input().split())
    town = [[] for _ in range(N)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        town[a - 1].append(b - 1)
        town[b - 1].append(a - 1)

    que = queue.Queue()
    que.put(0)
    # print(que.get())
    color = [-1] * N
    color[0] = 0
    while not que.empty():
        t = que.get()
        for i in town[t]:
            if color[i] == -1:
                color[i] = 1 - color[t]
                que.put(i)

    for _ in range(Q):
        c, d = map(int, input().split())
        if color[c - 1] == color[d - 1]:
            print('Town')
        else:
            print("Road")


if __name__ == '__main__':
    main()
