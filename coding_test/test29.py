# 2차원 리스트 dfs 응용
# 방향성과 가중치가 없는 그래프가 주어졌을때 정점 1에서부터 DFS 수행하는 프로그램을 작성하시오
# 예제입력
# 3 0
# 예제출력
# 1
# 예제입력
# 5 3
# 1 4
# 2 3
# 4 5
# 예제출력
# 1 4 5

# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 입력됩니다. (1≤N, 0≤M≤1,000)
# 둘째 줄부터 M + 1번째 줄까지 정수 A와 B가 입력됩니다. (1 ≤ A, B ≤ 1,000) 이 때 각 줄은 A와 B가 서로 연결되었음을 의미합니다.

N, M = map(int, input().split())

visited = [False] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int, input().split())
    # 무향그래프이므로 양쪽에 모두 삽입
    graph[a].append(b)
    graph[b].append(a)

# print(graph)

def dfs(graph, v, visited):
    visited[v] = True
    # 리스트 속 원소가 작은숫자부터 들어가게 정렬
    graph[v].sort() 
    print(v, end=' ')
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i , visited)
dfs(graph,1,visited)