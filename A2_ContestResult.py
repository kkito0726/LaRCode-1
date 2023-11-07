'''
URL: https://atcoder.jp/contests/abc290/tasks/abc290_a
Toyota Programming Contest 2023 Spring Qual B（AtCoder Beginner Contest 290）

A問題
'''

# TODO: 入力を受け取る
N,M = map (int, input().split())
yeah = [list(map(int, input().split())) for _ in range(N)]
print(N,M)
print(yeah)
# TODO: 期待する出力になるようにコードを書く
Score = 0
for i in range(M):
    y = yeah[1][i]-1
    H = yeah[0][y]
    Score += H
print(Score)
    