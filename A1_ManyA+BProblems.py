'''
URL: https://atcoder.jp/contests/abc288/tasks/abc288_a

Toyota Programming Contest 2023 Spring Qual A（AtCoder Beginner Contest 288）
A問題
'''

# TODO: 入力を受け取る
N = int(input())
nums = [list(map(int, input().split())) for _ in range(N)]

# TODO: 期待する出力になるようにコードを書く
for num in nums:
  print(num[0] + num[1])
