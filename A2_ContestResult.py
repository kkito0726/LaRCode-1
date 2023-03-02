'''
URL: https://atcoder.jp/contests/abc290/tasks/abc290_a
Toyota Programming Contest 2023 Spring Qual B（AtCoder Beginner Contest 290）

A問題
'''

# TODO: 入力を受け取る

n, m = map(int, input().split())  
list = [list(map(int, input().split())) for _ in range(2)]

num_list = list[0]
index_list = list[1]

# TODO: 期待する出力になるようにコードを書く

answer = []

for i in index_list:
    for i2, n in enumerate(num_list):
        if i-1 == i2:
            answer.append(n)

print(sum(answer))




