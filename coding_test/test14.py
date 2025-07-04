#문제입력 - 이코테 05.DFS/BFS 04. 미로 탈출(BFS)

# 미로 크기 (N,M) 에 괴물이 있는 부분은 0, 없는 부분은 1로 표시
# 현재 위치는 항상 (1,1) 이고 미로의 출구는 (N,M)에 존재
# 탈출하기 위해 필요한 최소 칸의 갯수를 구해라

# 입력 조건
# 첫째줄에 N,M 이 주어진다.
# 두번재줄부터 N개의 줄만큼 맵의 정보가 주어진다

# 출력 조건
# 탈출을 위해 필요한 최소 칸의 갯수를 출력

# 입력 예시
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111

# 출력 예시
# 10

from collections import deque
n,m= map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int,input())))

# 상하좌우 좌표 이동    
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    que = deque()
    que.append((x,y))
    while que:
        x,y = que.popleft()
        # 상하좌우 탐색 반복해서 1인곳 좌표를 한번에 모두 append하고 +1로 만듦
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >=n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny]= graph[x][y]+1
                print(graph)
                que.append((nx,ny))
                
    return graph[n-1][m-1]

print(bfs(0,0))
print(graph)