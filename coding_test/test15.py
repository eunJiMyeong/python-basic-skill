# 문제 입력
# N명의 학생을 일렬로 세워 시험을 보게 했습니다.
# 시험에서 P점 이상을 받은 학생들은 상을 받습니다.
# P점 미만의 학생들 중에서도 좌우로 인접한 P점 이상의 학생이 한 명 이상이면 그 학생은 상을 받습니다
# 상을 줄 수 있는 최대 학생수는 K명 입니다.
# 가능한 많은 상을 받을 수 있는 P의 최댓값을 구하세요
# 상을 받는 학생이 없을 수도 있습니다.

# 입력값 첫째줄에는 N, K
# 둘째줄에는 학생들의 점수가 공백으로 구분되어 주어집니다.
# K명 이하에게 상을 주면서 가능한 많은 학생들이 상을 받을 수 있게 하는 커트라인 중 가장 큰 것을 출력하시오
# 상을 받을 수 있는 학생이 없을수도 있다는 점을 유의하세요

# 예제 입력 1
# 5 3
# 50 30 40 50 70
# 예제 출력
# 70

# 예제 입력 2
# 5 4
# 80 60 100 75 70
# 예제 출력
# 80

import sys
N, K = map(int, sys.stdin.readline().split())
score_list = list(map(int, sys.stdin.readline().split()))
score_set = set(score_list)
score_dict = {}

for i in score_set:
    cnt = 0
    for j in range(N):
        if score_list[j] >= i:
            cnt +=1
        else:
            if j!=0 and j!= (N-1):
                if score_list[j-1] >= i or score_list[j+1] >= i:
                    cnt += 1
            elif j == 0:
                if score_list[j+1] >= i:
                    cnt += 1
            elif j == (N-1):
                if score_list[j-1] >= i:
                    cnt += 1
    score_dict[i] = cnt

max_k = -1e9
for k,v in score_dict.items():
    if v <= K:
        if max_k < v:
            max_k = v
            max_score = k

if max_k == -1e9:
    print(0)
else:
    print(max_score)
    

print(score_dict)