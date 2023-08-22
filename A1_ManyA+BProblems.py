'''
URL: https://atcoder.jp/contests/abc288/tasks/abc288_a

Toyota Programming Contest 2023 Spring Qual A（AtCoder Beginner Contest 288）
A問題
'''

# TODO: 入力を受け取る
N = int(input())
numbers = [list(map(int, input().split())) for i in range(N)]
# TODO: 期待する出力になるようにコードを書く
for i in range(N):
    print(numbers[i][0] + numbers[i][1])
