'''
URL: https://atcoder.jp/contests/abc288/tasks/abc288_a

Toyota Programming Contest 2023 Spring Qual A（AtCoder Beginner Contest 288）
A問題
'''

# TODO: 入力を受け取る


# TODO: 期待する出力になるようにコードを



# nums = map(int, input().split())
# print(nums)
# num_list = list(map(int, imput().split()))

n = int(input())
num_list = [list(map(int, input().split())) for _ in range(n)]
# print(num_list)

for i in range(n):
    print(num_list[i][0] + num_list[i][1])