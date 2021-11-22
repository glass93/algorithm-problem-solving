# 내 코드

import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())

result = 0
while True:
    if (n % k) == 0:
        if (n // k) == 1:
            result += 1
            break
        else:
            n = n // k
            result += 1
    else:
        n -= 1
        result += 1

print(result)