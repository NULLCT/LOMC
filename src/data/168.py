def main():
    import sys
    input = sys.stdin.readline
    sys.setrecursionlimit(10**7)
    from collections import Counter, deque, defaultdict
    from itertools import combinations, permutations, accumulate, groupby, product
    from bisect import bisect_left, bisect_right
    from heapq import heapify, heappop, heappush
    from math import floor, ceil, pi, factorial, gcd, sqrt

    def I():
        return int(input())

    def MI():
        return map(int, input().split())

    def LI():
        return list(map(int, input().split()))

    def SI():
        return input().rstrip()

    inf = 10**17
    mod = 10**9 + 7
    #mod =998244353
    n, q = MI()
    adj = [[] for i in range(n)]
    for i in range(n - 1):
        a, b = MI()
        a -= 1
        b -= 1
        adj[a].append(b)
        adj[b].append(a)
    dist = [0] * n
    Q = deque([0])
    visited = [0] * n
    visited[0] = 1
    while Q:
        x = Q.popleft()
        for nex in adj[x]:
            if visited[nex]:
                continue
            dist[nex] = dist[x] + 1
            Q.append(nex)
            visited[nex] = 1
    #print(dist)
    for i in range(q):
        c, d = MI()
        c -= 1
        d -= 1
        if (dist[c] - dist[d]) % 2 == 0:
            print("Town")
        else:
            print("Road")


if __name__ == "__main__":
    main()
