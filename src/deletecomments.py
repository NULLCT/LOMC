#!/usr/bin/env python3

from typing import List
from copy import copy
import numpy as np


def count_quote_marks(x: str) -> List[int]:
    """各種引用符の数を数える"""
    n_tquotes = x.count('\'\'\'')
    n_tdquotes = x.count('\"\"\"')
    n_quotes = x.count('\'') - 3 * n_tquotes
    n_dquotes = x.count('\"') - 3 * n_tdquotes
    return [n_quotes, n_dquotes, n_tquotes, n_tdquotes]


def get_comment_ids(cmd: str) -> List[int]:
    """「コメントを示す」ハッシュのインデックスを取得"""
    # quotes, double quotes, triple quotes, triple double quotesの数を保持するリスト
    quotes_counts = np.zeros(4, dtype=int)

    # ハッシュ (#) の位置を返すジェネレーター
    hash_ids = (i for i, elem in enumerate(cmd) if '#' in elem)

    # hash_idsのうち，引用符内に無いハッシュのインデックスをcomment_idsとする
    prev_i = 0
    comment_ids = []
    for i in hash_ids:
        sliced = cmd[prev_i: i]
        quotes_counts += np.array(count_quote_marks(sliced))

        # 全quotes_countsが偶数 <=> 引用符外にあるハッシュ
        if np.sum((quotes_counts) % 2) == 0:
            comment_ids.append(i)

        prev_i = i

    return comment_ids


def get_return_ids(cmd: str) -> List[int]:
    """改行記号\nを取得"""
    return [i for i in range(len(cmd)) if cmd[i: i + 1] == '\n']


def delete_useless_comments(cmd: str) -> str:
    """不要なコメントを削除する"""
    cmd = copy(cmd)

    comment_ids = get_comment_ids(cmd)

    return_ids = get_return_ids(cmd + '\n')

    next_return_ids = []  # ハッシュ直後の改行コードを取得
    for index in comment_ids:
        next_return_ids.append([i for i in return_ids if i > index][0])


    # 後ろからcmdを削っていかないとインデックス指定が面倒なので
    for i, j in zip(reversed(comment_ids), reversed(next_return_ids)):
        cmd = cmd[:i] + cmd[j:]
    return cmd

cmd = """
import queue

N, Q = map(int, input().split())
G = [[] for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
que = queue.Queue()
color = [-1] * N
color[0] = 0
que.put(0)
while not que.empty():
    t = que.get()
    for i in G[t]:
        if color[i] == -1:
            color[i] = 1 - color[t]
            que.put(i)
for i in range(Q):
    a, b = map(int, input().split())
    if color[a - 1] == color[b - 1]:
        print("Town")
    else:
        print("Road")
"""

print(delete_useless_comments(cmd))
