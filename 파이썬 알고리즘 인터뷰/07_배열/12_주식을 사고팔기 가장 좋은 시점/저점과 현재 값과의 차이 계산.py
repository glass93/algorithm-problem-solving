# 저점과 현재 값과의 차이 계산 (121. Best Time To Buy and Sell Stock)

import sys
sys.stdin = open('input.txt')

prices = list(map(int, input().split()))

profit = 0
min_price = max(prices)

# 최솟값과 최댓값을 계속 갱신
for price in prices:
    min_price = min(min_price, price)
    profit = max(profit, price - min_price)

print(profit)