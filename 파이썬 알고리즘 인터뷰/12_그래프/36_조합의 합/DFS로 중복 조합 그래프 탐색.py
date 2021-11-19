# DFS로 중복 조합 그래프 탐색 (39. Combination Sum)

import sys
sys.stdin = open('input.txt')

candidates = list(map(int, input().split()))
target = int(input())

result = []

def dfs(csum, index, path):
    # 종료 조건
    if csum < 0:
        return
    if csum == 0:
        result.append(path)
        return

    # 자신 부터 하위 원소 까지의 나열 재귀 호출
    for i in range(index, len(candidates)):
        dfs(csum - candidates[i], i, path + [candidates[i]])

dfs(target, 0, [])
print(result)