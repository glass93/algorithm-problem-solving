# 짝수 번째 값 계산 (561. ArrayPartition 1)

import sys
sys.stdin = open('input.txt')

nums = list(map(int, input().split()))

nums.sort()
sum = 0

for i, n in enumerate(nums):
    # 짝수 번째 값의 합 계산
    if i % 2 == 0:
        sum += n

print(sum)