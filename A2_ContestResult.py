'''
URL: https://atcoder.jp/contests/abc290/tasks/abc290_a
Toyota Programming Contest 2023 Spring Qual B（AtCoder Beginner Contest 290）

A問題
'''

# TODO: 入力を受け取る


# TODO: 期待する出力になるようにコードを書く

N,M = map(int, input().split())
tensu = list(map(int, input().split()))
mondaisu = list(map(int, input().split()))

# print(N,M)
# print(tensu)
# print(mondaisu)

score = 0

for i in mondaisu:
    score += tensu[i-1]
print(score)


