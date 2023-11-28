'''
URL: https://atcoder.jp/contests/abc290/tasks/abc290_a
Toyota Programming Contest 2023 Spring Qual B（AtCoder Beginner Contest 290）

A問題
'''

# TODO: 入力を受け取る
N, M = map(int, input().split())
score_list = list(map(int, input().split()))
index = list(map(int, input().split()))
# TODO: 期待する出力になるようにコードを書く
ans = 0
for id in index:
    ans += score_list[id - 1]
print(ans)