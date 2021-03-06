# 일정 그래프 반복 (332. Reconstruct Itinerary)

import collections

tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]

graph = collections.defaultdict(list)
# 그래프 순서대로 구성
for a, b in sorted(tickets):
    graph[a].append(b)

route, stack = [], ['JFK']
while stack:
    # 반복으로 스택을 구성하되 막히는 부분에서 풀어내는 처리
    while graph[stack[-1]]:
        stack.append(graph[stack[-1]].pop(0))
    route.append(stack.pop())

# 다시 뒤집어 어휘 순 결과로
print(route[::-1])