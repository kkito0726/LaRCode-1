'''
URL: https://atcoder.jp/contests/abc290/tasks/abc290_a
Toyota Programming Contest 2023 Spring Qual B（AtCoder Beginner Contest 290）

A問題
'''

# TODO: 入力を受け取る
a,b = map(int, input().split())  # 3個の数字の入力を受け取る                      # 出力を確認
num_list = list(map(int, input().split()))  # n個の数字がリストに格納される
num_list2 = list(map(int, input().split()))  # n個の数字がリストに格納される


score = 0
for i in range(b) :
    score += num_list[num_list2[i]-1]
print(score)