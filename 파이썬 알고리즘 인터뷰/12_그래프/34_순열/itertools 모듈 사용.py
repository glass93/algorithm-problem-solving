# itertools 모듈 사용 (46. Permutations)

import sys
import itertools
sys.stdin = open('input.txt')

nums = list(map(int, input().split()))

print(list(map(list, (itertools.permutations(nums)))))