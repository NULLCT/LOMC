import sys

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

from collections import deque


def main():  # for speed up
    # ノード数, エッジ数, 始点ノード
    n, q = map(int, input().split())
    # adj[s]: ノード s に隣接する(ノード, 重み)をリストで持つ
    adj = [[] for _ in range(n)]
    for _ in range(n - 1):
        s, t = map(int, input().split())
        adj[s - 1].append(t - 1)
        adj[t - 1].append(s - 1)

    dp = [-1] * n
    dqn = deque()
    dqn.append((0, 0))
    while dqn:
        (ii, depth) = dqn.popleft()
        dp[ii] = depth
        for jj in adj[ii]:
            if dp[jj] < 0:
                dqn.append((jj, depth + 1))

    for _ in range(q):
        s, t = map(int, input().split())
        if (dp[s - 1] + dp[t - 1]) % 2 == 0:
            print("Town")
        else:
            print("Road")


main()
