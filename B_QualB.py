'''
URL: https://atcoder.jp/contests/abc290/tasks/abc290_b
Toyota Programming Contest 2023 Spring Qual B（AtCoder Beginner Contest 290）

A問題
'''

# TODO: 入力を受け取る
N, K = map(int, input().split())
S = input()

# TODO: 期待する出力になるようにコードを書く
ans = ""
for i in range(N):
  if K==0 or S[i]=="x":
    ans += "x"
    continue
  
  if S[i] == "o":
    ans += "o"
    K -= 1
    
print(ans)
