# input
# 3 8 9 7 6
# 3
# 0 0 0
# 1
# 1 2 3 4
# output
# [9, 7, 6, 3, 8]
# [0, 0, 0]
# [1, 2, 3, 4]

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    a = list(map(int, input().split()))
    k = int(input())

    result = [0] * len(a)
    if k == 0 or k == len(a) or len(a) == 1:
        print(a)
    else:
        for i in range(len(a)):
            if k >= len(a):
                result[int((i+k)%len(a))] = a[i]
            elif i + k > len(a)-1:
                result[i+k-len(a)] = a[i]
            else:
                result[i+k] = a[i]
        print(result)