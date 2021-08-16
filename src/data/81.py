from collections import defaultdict, deque
# input: a_1 a_2がそれぞれ無向につがなっている
# 1 2
# 1 4
# 2 3
# 3 4
# このinputでは、1と２のノードが繋がっていて、1と４のノードが繋がっているetc..


def solve():
    N, Q = map(int, input().split())
    G = defaultdict(list)
    for i in range(N - 1):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
    # print(G)
    # print(c, d)
    dist = [-1] * (N + 1)
    que = deque()

    dist[1] = 0
    que.append(1)
    while not len(que) == 0:
        v = que.popleft()

        for nv in G[v]:
            if not dist[nv] == -1: continue
            dist[nv] = dist[v] + 1
            que.append(nv)

    for _ in range(Q):
        c, d = map(int, input().split())
        result = "Town" if (dist[d] - dist[c]) % 2 == 0 else "Road"
        print(result)


if __name__ == '__main__':
    solve()
