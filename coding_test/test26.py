# 문제 입력 - 분리수거장(초급)

# 두정동에는 N개의 아파트 단지가 일직선상에 존재합니다. 각 아파트 단지에는 1번부터 N번까지 번호가 붙어있습니다.
# 두정동 동사무소에서는 아파트 단지 중 한 곳에 분리수거장을 지으려고 합니다. 분리수거장으로부터 각 주민들까지의 거리의 합이 최소가 되도록 하려면 어떤 아파트 단지에 분리수거장을 지어야 하는지 구하는 프로그램을 작성해주세요.
# 분리수거장으로부터 어떤 주민까지의 거리는 분리수거장이 있는 아파트 단지의 위치와 해당 주민이 거주하는 아파트 단지의 위치의 차로 계산됩니다.
# 단, 조건을 만족하는 아파트 단지가 여러개일 경우, 더 작은 번호의 아파트 단지에 분리수거장을 짓습니다.


# 예제 입력1
# 7
# 475 170
# 28 95
# 506 8361
# 51 3988
# 2 977
# 607 793
# 49 847

# 예제 출력1
# 3

# 506 아파트 위치를 분리수거장으로 했을때, 첫번째 아파트인 475 710 은 |506-475|의 거리만큼을 170명이 이동해야함

n = int(input())
apart = [[]*(n+1) for _ in range(n+1)]
distance = [0]*(n+1)
min = 1

for i in range(1,n+1):
    apart[i] = list(map(int,input().split()))

for i in range(1,n+1):
    for j in range(1,n+1):
        distance[i] += (abs(apart[i][0] - apart[j][0])*apart[j][1])
    if distance[min] > distance[i]:
        min = i
print(min)
        
# import sys

# N = int(sys.stdin.readline())
# apart = []
# for _ in range(N):
#     location, people = map(int, sys.stdin.readline().split())
#     apart.append([location, people])

# score = [0]*N # [0,0,0,0,0,0,]
# # [[0] for _ in range(N)] 은 [[0],[0],[0]] 이런식으로 나오는데 밑에서 score[i]+=로 계산이 불가능함

# for i in range(N):
#     for j in range(N):
#         score[i] += abs(apart[i][0]-apart[j][0])*apart[j][1]
#     if score[answer] > score[i]:
#         answer = i

# print(answer+1)