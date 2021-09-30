# 파이썬다운 방식 (561. ArrayPartition 1)

import sys
sys.stdin = open('input.txt')

nums = list(map(int, input().split()))

print(sum(sorted(nums)[::2]))