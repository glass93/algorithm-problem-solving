# 투 포인터 이용 (1. Two Sum)
import sys
sys.stdin = open('input.txt')

nums = list(map(int, input().split()))
target = int(input())

left, right = 0, len(nums) - 1

while not left == right:
    # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
    if nums[left] + nums[right] < target:
        left += 1
    # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
    elif nums[left] + nums[right] > target:
        right -= 1
    else:
        print(left, right)
        break