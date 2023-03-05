'''
URL: https://atcoder.jp/contests/abc290/tasks/abc290_b
Toyota Programming Contest 2023 Spring Qual B（AtCoder Beginner Contest 290）

A問題
'''

# TODO: 入力を受け取る





# TODO: 期待する出力になるようにコードを書く
N, K = map(int, input().split()) #Nは参加者、Kは予選通過者
S = [s for s in input()] #Sは文字列
answer = []
for p in S:
    if p == "o" and answer.count("o") < K:
        answer.append("o")
    else:
        answer.append("x")
answer2 = "".join(answer)
print(answer2)