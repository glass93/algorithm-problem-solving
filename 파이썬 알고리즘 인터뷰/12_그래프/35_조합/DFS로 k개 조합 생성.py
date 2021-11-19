# DFS로 k개 조합 생성 (77. Combinations)

import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())

results = []

def dfs(elements, start, k):
    if k == 0:
        results.append(elements[:])

    # 자신 이전의 모든 값을 고정하여 재귀 호출
    for i in range(start, n + 1):
        elements.append(i)
        dfs(elements, i + 1, k - 1)
        elements.pop()

dfs([], 1, k)

print(results)