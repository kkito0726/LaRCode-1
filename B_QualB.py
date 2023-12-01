'''
URL: https://atcoder.jp/contests/abc290/tasks/abc290_b
Toyota Programming Contest 2023 Spring Qual B（AtCoder Beginner Contest 290）

A問題
'''

# TODO: 入力を受け取る
a, b = map(int, input().split())       
c = input().strip()               

# TODO: 期待する出力になるようにコードを書く
T = ''

for i in range(a):
    if c[i] == 'o' and b > 0 :
        T += 'o'
        b -= 1
    else :
        T += 'x'

print(T)