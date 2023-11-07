'''
URL: https://atcoder.jp/contests/abc290/tasks/abc290_b
Toyota Programming Contest 2023 Spring Qual B（AtCoder Beginner Contest 290）

A問題
'''

# TODO: 入力を受け取る
N, K = map(int, input().split())
S = input()
# TODO: 期待する出力になるようにコードを書く
join = ''
l = 0
for i in range(N):
    if l < K:
        if S[i] == 'o':
            l += 1
            join += 'o'
        if S[i] == 'x':
            join += 'x'
    else:
        join += 'x'
print(join)

    