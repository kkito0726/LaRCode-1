'''
URL: https://atcoder.jp/contests/abc290/tasks/abc290_b
Toyota Programming Contest 2023 Spring Qual B（AtCoder Beginner Contest 290）

A問題
'''

# TODO: 入力を受け取る
N, K = map(int, input().split())
request = input()

# TODO: 期待する出力になるようにコードを書く
advance = []
for i in range(len(request)):
    if K > 0:
       if request[i] == 'o':
           K -= 1
           advance.append('o')
       elif request[i] == 'x':
           advance.append('x')
    else:
        advance.append('x')
print(''.join(advance))