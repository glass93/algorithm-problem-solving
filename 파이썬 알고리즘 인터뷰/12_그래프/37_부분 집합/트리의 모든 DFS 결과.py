# 트리의 모든 DFS 결과 (78. Subsets)

import sys
sys.stdin = open('input.txt')

nums = list(map(int, input().split()))

result = []

def dfs(index, path):
    # 매번 결과 추가
    result.append(path)
    print(result)

    # 경로를 만들면서 DFS
    for i in range(index, len(nums)):
        dfs(i + 1, path + [nums[i]])


dfs(0, [])
print(result)