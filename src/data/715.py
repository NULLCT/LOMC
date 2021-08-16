import sys


def read():
    return sys.stdin.readline().rstrip()


def main():
    n, q = map(int, read().split())
    al = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = [int(i) - 1 for i in read().split()]
        al[a].append(b)
        al[b].append(a)
    todo = [(0, 0)]
    seen = [False] * n
    color = [0] * n
    while todo:
        v, p = todo.pop()
        if seen[v]:
            continue
        seen[v] = True
        color[v] = p
        for u in al[v]:
            todo.append((u, 1 - p))
    for _ in range(q):
        c, d = [int(i) - 1 for i in read().split()]
        print("Town" if color[c] == color[d] else "Road")


if __name__ == '__main__':
    main()
