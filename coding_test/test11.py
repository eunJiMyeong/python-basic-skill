# 문제 입력 - 이코테 그리디 03. 숫자 카드 게임

# 여러개의 숫자 카드 중 가장 높은 숫자 카드 한장을 뽑는 게임이다
# N개의 행, M개의 열로 이루어진 숫자 카드가 있다
# 먼저 뽑고자 하는 행을 고른 후 그 행에서 가장 낮은 숫자 카드를 선택한다
# 따라서 처음에 카드를 고르는 행을 선택할때 최종적으로 가장 높은 숫자카드를 고를 수 있도록 전략을 짜야 한다

# 첫째줄에 N M 이 주어진다
# 둘째줄부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다
# 선택한 카드에 적힌 숫자를 출력한다.

# 예제 입력1
# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

# 예제 출력1
# 2

N,M = map(int, input().split())

min_list = []
for i in range(N):
    row = list(map(int, input().split()))
    min_list.append(min(row))

print(max(min_list))


# 이코테 답안
result = 0
N,M = map(int, input().split())
result = 0
for i in range(N):
    row = list(map(int, input().split()))
    
    # 현재 row에서 가장 작은 수 찾기
    min_value = 1e9
    for a in row:
        min_value = min(a, min_value)
    # 가장 작은수들 중 가장 큰 수 찾기
    result = max(result, min_value)
    
print(result)