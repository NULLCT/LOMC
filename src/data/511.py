# モジュールのインポート
import sys

sys.setrecursionlimit(10**6)

readline = sys.stdin.readline


def get_input() -> tuple:
    """
    標準入力を取得する.

    Returns:
        tuple: 標準入力
    """
    # 標準入力を取得
    N, Q = map(int, input().split())
    g = {i: [] for i in range(1, N + 1)}
    for _ in range(N - 1):
        a, b = map(int, readline().split())
        g[a].append(b)
        g[b].append(a)
    q = []
    for _ in range(Q):
        c, d = map(int, readline().split())
        q.append((c, d))

    return N, Q, g, q


def dfs(g: dict, city_depth: dict, depth: int, city: int) -> None:
    """
    街の深さを設定する.

    Args:
        g (dict): 道路
        city_depth (dict): 街の深さ(city_depth[i]: 街iの深さ)
        depth (int): 深さ
        city (int): 街
    """
    if city_depth[city] != -1:
        return
    city_depth[city] = depth
    for nbhd_city in g[city]:
        dfs(g, city_depth, depth + 1, nbhd_city)


def solve(N: int, Q: int, g: dict, q: list) -> None:
    """
    求解処理.

    Args:
        N (int): 街の数(2 <= N <= 10^5)
        Q (int): クエリの数(1 <= Q <= 10^5)
        g (dict): 道路(g[i]: 街iと結ばれている街のリスト)
        q (list): クエリ
    """
    # 求解処理
    city_depth = {i: -1 for i in range(1, N + 1)}
    dfs(g, city_depth, 0, 1)  # 街1をroot nodeとして各街の深さを設定
    for i in range(Q):
        c, d = q[i]
        if abs(city_depth[c] - city_depth[d]) % 2 == 0:
            print("Town")
        else:
            print("Road")


if __name__ == "__main__":
    # 標準入力を取得
    N, Q, g, q = get_input()

    # 求解処理
    solve(N, Q, g, q)
