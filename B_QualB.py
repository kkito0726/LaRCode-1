'''
URL: https://atcoder.jp/contests/abc290/tasks/abc290_b
Toyota Programming Contest 2023 Spring Qual B（AtCoder Beginner Contest 290）

A問題
'''

# TODO: 入力を受け取る
N, K = map(int, input().split())
S = input()

# TODO: 期待する出力になるようにコードを書く
count = 0
l = []

for i in range(N):
    if S[i] == "o" and count < K:
        count += 1
        l.append("o")

    else:
        count += 0
        l.append("x")
        
print("".join(l))