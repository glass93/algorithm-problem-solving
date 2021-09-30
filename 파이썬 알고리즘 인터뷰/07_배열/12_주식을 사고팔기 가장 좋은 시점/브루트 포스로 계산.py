# 브루트 포스로 계산 (121. Best Time To Buy and Sell Stock)

import sys
sys.stdin = open('input.txt')

prices = list(map(int, input().split()))

max_price = 0

for i, price in enumerate(prices):
    for j in range(i, len(prices)):
        max_price = max(prices[j] - price, max_price)

print(max_price)