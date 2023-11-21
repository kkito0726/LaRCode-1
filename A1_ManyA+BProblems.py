'''
URL: https://atcoder.jp/contests/abc288/tasks/abc288_a

Toyota Programming Contest 2023 Spring Qual A（AtCoder Beginner Contest 288）
A問題
'''

# TODO: 入力を受け取る
n = int(input())
num_list = [list(map(int, input().split())) for _ in range(n)]

# TODO: 期待する出力になるようにコードを書く

for num in num_list :
    print(num[0]+num[1])
