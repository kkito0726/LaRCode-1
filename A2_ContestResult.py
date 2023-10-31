'''
URL: https://atcoder.jp/contests/abc290/tasks/abc290_a
Toyota Programming Contest 2023 Spring Qual B（AtCoder Beginner Contest 290）

A問題
'''

# TODO: 入力を受け取る
N, M = map(int, input().split())
score = list(map(int, input().split()))
answer = list(map(int, input().split()))

# TODO: 期待する出力になるようにコードを書く
ans = 0
for a in answer:
    ans += score[a-1]
print(ans)