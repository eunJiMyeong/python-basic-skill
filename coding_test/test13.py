#문제입력 - 이코테 05.DFS/BFS 03. 음료수 얼려먹기(DFS)

# N*M크기 얼음틀이 있다.구멍이 뚫린 부분은 0, 칸막이가 있는 부분은 1
# 구멍이 뚫린 부분끼리 상,하,좌,우로 연결된 경우 연결된 부분에 1개의 아이스크림을 얼릴 수 있다.
# 다음 4*5 얼음틀에서는 3개의 아이스크림을 얻을 수 있다.
# 00110
# 00011
# 11111
# 00000

# 입력조건
# 첫번째줄에 얼음틀의 N*M 크기 N,M이 주어진다
# 두번째줄부터 N+1번째 줄까지 얼음틀의 형태가 주어진다

# 출력조건
# 한번에 만들 수 있는 아이스크림 갯수를 출력하라


N,M = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input()))) 
    # list(map(int,sys.stdin.readline().split())) 은 011, 010 입력시 [[11],[10]] 이런식으로 나옴
print(N,M,graph)

def dfs(x,y):
    # 좌표 범위 (0,0)~(N-1,M-1) 를 벗어나면 함수 종료
    if x<=-1 or x >= N or y <= -1 or y >= M :
        return False
    # graph[x][y] 방문 안했을 시
    if graph[x][y] == 0:
        graph[x][y] = 1 # 
        # 상하좌우 좌표값 1로 만들어주기
        # 재귀적으로 반복하여 상좌표로 갔을때 상좌표 자리에서 상하좌우를 또 탐색하게 됨
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    # graph[x][y] == 1일때
    return False

result = 0
for i in range(N):
    for j in range(M):
        # 0,0부터 시작해서 연속적으로 붙어있는 모든칸에 대해 값을 0->1로 바꾼 후 True 뱉는 횟수 count
        if dfs(i,j) == True:
            result +=1
            print("넘어감")
            
print(result)
# print(graph)