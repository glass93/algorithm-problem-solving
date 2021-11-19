# DFS를 활용한 순열 생성 (46. Permutations)

import sys
sys.stdin = open('input.txt')

nums = list(map(int, input().split()))

results = []
prev_elements = []

def dfs(elements):
    # 리프 노트일 때 결과 추가
    if len(elements) == 0:
        results.append(prev_elements[:])

    # 순열 생성 재귀 호출
    for e in elements:
        next_elements = elements[:]
        next_elements.remove(e)

        prev_elements.append(e)
        dfs(next_elements)
        prev_elements.pop()

dfs(nums)

print(results)