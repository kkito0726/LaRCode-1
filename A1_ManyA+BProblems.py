'''
URL: https://atcoder.jp/contests/abc288/tasks/abc288_a

Toyota Programming Contest 2023 Spring Qual A（AtCoder Beginner Contest 288）
A問題
'''

# TODO: 入力を受け取る

N = int(input())
num_list = [list(map(int, input().split())) for _ in range(N)]
# print(N)
# print(num_list)

# for i in range(N):
#      print(nums[i][0] + nums[i][1])
# for num in nums:
#   print(num[0] + num[1])

for i in range(N):
    print(num_list[i][0] + num_list[i][1])


# TODO: 期待する出力になるようにコードを書く
