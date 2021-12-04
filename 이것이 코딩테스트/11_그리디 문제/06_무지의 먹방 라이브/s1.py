# 시간 초과나는 내 풀이

import sys
sys.stdin = open('input.txt')

food_times = list(map(int, input().split()))
k = int(input())

idx = 0
count = 0
result = 0
while count <= k:
    if idx == len(food_times):
        idx = 0
    if food_times[idx] == 0:
        idx += 1
        continue
    else:
        food_times[idx] -= 1
        idx += 1
        count += 1

print(idx)