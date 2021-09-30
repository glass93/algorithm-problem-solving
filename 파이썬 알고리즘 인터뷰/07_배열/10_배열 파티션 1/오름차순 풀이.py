# 오름차순 풀이 (561. ArrayPartition 1)

import sys
sys.stdin = open('input.txt')

nums = list(map(int, input().split()))

sum = 0
pair = []
nums.sort()

for n in nums:
    # 앞에서부터 오름차순으로 페어를 만들어서 합 계산
    pair.append(n)
    if len(pair) == 2:
        sum += min(pair)
        pair = []

print(sum)