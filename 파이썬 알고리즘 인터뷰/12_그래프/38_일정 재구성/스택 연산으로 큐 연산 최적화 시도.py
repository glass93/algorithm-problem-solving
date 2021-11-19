# 스택 연산으로 큐 연산 최적화 시도 (332. Reconstruct Itinerary)

import collections

tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]

graph = collections.defaultdict(list)
# 그래프를 뒤집어서 구성
for a, b in sorted(tickets, reverse=True):
    graph[a].append(b)

route = []
def dfs(a):
    # 마지막 값을 읽어 어휘 순 방문
    while graph[a]:
        dfs(graph[a].pop())
    route.append(a)

dfs('JFK')
# 다시 뒤집어 어휘 순 결과로
print(route[::-1])