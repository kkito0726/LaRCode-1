'''
URL: https://atcoder.jp/contests/abc290/tasks/abc290_a
Toyota Programming Contest 2023 Spring Qual B（AtCoder Beginner Contest 290）

A問題
'''

# TODO: 入力を受け取る
M,N = map(int, input().split())
tensu = list(map(int, input().split()))
monndaisu = list(map(int, input().split()))
# print(M,N)
# print(tensu)
# print(monndaisu)


# TODO: 期待する出力になるようにコードを書く
score = 0 
for i in monndaisu:
    score += tensu[i-1]
print(score)