'''
URL: https://atcoder.jp/contests/abc290/tasks/abc290_a
Toyota Programming Contest 2023 Spring Qual B（AtCoder Beginner Contest 290）

A問題
'''

# TODO: 入力を受け取る
a,b = map(int, input().split())
#print(a,b)
num_list = []
for i in range(2):
    num_list.append(list(map(int,input().split())))
#print(num_list)
# TODO: 期待する出力になるようにコードを書く
a = 0
for i in range(b):
    a += num_list[0][num_list[1][i]-1]
print(a)

