'''
URL: https://atcoder.jp/contests/abc290/tasks/abc290_b
Toyota Programming Contest 2023 Spring Qual B（AtCoder Beginner Contest 290）

A問題
'''

# TODO: 入力を受け取る
sanka, tuuka = map(int, input().split())
marubatu = input()

# TODO: 期待する出力になるようにコードを書く
kotae = ""
for i in marubatu:
    if i == "o" and tuuka >= 1:
        tuuka -= 1
        kotae += "o"
    else:
        kotae += "x"
print(kotae)
