# itertools 모듈 사용 (77. Combinations)

import sys
import itertools
sys.stdin = open('input.txt')

n, k = map(int, input().split())

print(list(itertools.combinations(range(1, n+1), k)))