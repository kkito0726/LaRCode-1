'''
URL: https://atcoder.jp/contests/abc290/tasks/abc290_a
Toyota Programming Contest 2023 Spring Qual B（AtCoder Beginner Contest 290）

A問題
'''

# TODO: 入力を受け取る
N, M = map(int, input().split())
tests = list(map(int, input().split()))
id_list = list(map(int, input().split()))

# TODO: 期待する出力になるようにコードを書く
point = 0
for i in range(M):
  point += tests[id_list[i] - 1]
  
print(point)
