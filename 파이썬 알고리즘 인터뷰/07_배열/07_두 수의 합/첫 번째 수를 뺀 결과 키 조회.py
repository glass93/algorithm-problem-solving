# 첫 번째 수를 뺀 결과 키 조회 (1. Two Sum)
import sys
sys.stdin = open('input.txt')

nums = list(map(int, input().split()))
target = int(input())

nums_map = {}
# 키와 값을 바꿔서 딕셔너리로 저장
for i, num in enumerate(nums):
    nums_map[num] = i

print(nums_map)

# 타켓에서 첫 번째 수를 뺀 결과를 키로 조회
for i, num in enumerate(nums):
    if target - num in nums_map and i != nums_map[target - num]:
        print([nums.index(num), nums_map[target - num]])
        break

## 조회 구조 개선
nums_map = {}
# 하나의 for 문으로 통합
for i, num in enumerate(nums):
    if target - num in nums_map:
        print([nums_map[target - num], i])
        break
    nums_map[num] = i