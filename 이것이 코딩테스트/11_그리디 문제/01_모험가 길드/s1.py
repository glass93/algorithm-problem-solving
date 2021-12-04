# 틀림. 오름차순으로 정렬해야 함

import sys
sys.stdin = open('input.txt')
from collections import deque

# 모험가 수 N 입력
n = int(input())

data = list(map(int, input().split()))

ordered_data = deque(sorted(data, reverse=True))

count = 0

while ordered_data:
    x = ordered_data.popleft()
    group = [x]
    for _ in range(x - 1):
        group.append(ordered_data.popleft())
    if len(group) == x:
        count += 1

print(count)