'''
URL: https://atcoder.jp/contests/abc290/tasks/abc290_b
Toyota Programming Contest 2023 Spring Qual B（AtCoder Beginner Contest 290）

A問題
'''

# TODO: 入力を受け取る
N,K = map(int, input().split())
S = input()

# print(N,K)
# print(S)


# TODO: 期待する出力になるようにコードを書  


T = []

for i in range(N):
    if K > 0 and S[i] == 'o':
        K -= 1
        T.append('o')

    else:
        T.append('x')

print(''.join(T))


    


