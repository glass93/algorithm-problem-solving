# DFS로 일정 그래프 구성 (332. Reconstruct Itinerary)

import collections

tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
graph = collections.defaultdict(list)
# 그래프 순서대로 구성
for a, b in sorted(tickets):
    graph[a].append(b)

route = []


def dfs(a):
    # 첫 번째 값을 읽어 어휘 순 방문
    while graph[a]:
        dfs(graph[a].pop(0))
    route.append(a)


dfs('JFK')
# 다시 뒤집어 어휘 순 결과로
print(route[::-1])