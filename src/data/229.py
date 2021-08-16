import sys
from random import randint

sys.setrecursionlimit(10**7)
input = sys.stdin.readline


def getlist(type):
    return list(map(type, input().rstrip().split()))


def calc(G, crr, pre, arr):
    for nxt in G[crr]:
        if nxt == pre:
            continue
        arr[nxt] = (arr[crr] + 1) % 2
        calc(G, nxt, crr, arr)
    return


def main():
    n, q = getlist(int)
    G = [set() for _ in range(n)]
    for _ in range(n - 1):
        a, b = getlist(int)
        a, b = a - 1, b - 1
        G[a].add(b)
        G[b].add(a)
    arr = [0 for _ in range(n)]
    calc(G, randint(0, n - 1), -1, arr)
    ans = []
    for _ in range(q):
        a, b = getlist(int)
        a, b = a - 1, b - 1
        ans.append((arr[a] ^ arr[b]) == 0)
    for f in ans:
        if f:
            print("Town")
        else:
            print("Road")


if __name__ == "__main__":
    main()
