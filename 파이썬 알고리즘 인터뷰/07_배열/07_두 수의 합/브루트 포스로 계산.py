# 브루트 포스로 계산 (1. Two Sum)

import sys
sys.stdin = open('input.txt')

nums = list(map(int, input().split())) # 2, 7, 11, 15
target = int(input()) # 9

for i in range(len(nums)):
    for j in range(1, len(nums)):
        if nums[i] + nums[j] == target:
            print([i, j])