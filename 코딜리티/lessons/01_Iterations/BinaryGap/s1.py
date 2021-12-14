# input
# 561892
# 74901729
# 1376796946
# output
# 3
# 4
# 5

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    binary_N = bin(N)

    count = 0
    maximum_count = 0

    for i in range(2, len(binary_N)):
        if binary_N[i] == "0":
            count += 1
        elif binary_N[i] == "1":
            if count > maximum_count:
                maximum_count = count
                count = 0
            else:
                count = 0

    print(maximum_count)