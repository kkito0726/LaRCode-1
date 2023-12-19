'''
URL: https://atcoder.jp/contests/abc290/tasks/abc290_b
Toyota Programming Contest 2023 Spring Qual B（AtCoder Beginner Contest 290）

A問題
'''

# TODO: 入力を受け取る
a,b= map(int, input().split())  # 3個の数字の入力を受け取る
c = input()  # sはstr型


S = ""
for i in range(a) :
    if c[i] == "o" and b>=0 :
       b -= 1
       S += "o"
    else :
       S += "x"
print(S)