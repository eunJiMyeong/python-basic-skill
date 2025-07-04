# 학생들의 성적이 정렬되지 않은 형태로 나열되어 있습니다.
# 이때 성적에 따라 학생들의 등수를 계산해주는 프로그램을 작성해주세요.
# 두 명 이상의 학생이 같은 점수를 받을 수 있으며, 같은 점수를 받은 학생들은 모두 같은 석차로 처리합니다. 
# 예를 들어 학생 5명의 성적이 30, 47, 47, 52, 70이면, 47점을 받은 학생 두 명은 모두 3등이고, 4등은 존재하지 않습니다.

# 예제 입력1
# 5
# 30 47 47 52 70

# 예제 출력1
# 30 5
# 47 3
# 47 3
# 52 2
# 70 1

import sys
input = sys.stdin.readline

N = int(input())
scores = list(map(int, input().split()))
result = []


for i in range(N):
    rank = 1
    for j in range(N):
        if scores[i] < scores[j]:
            rank += 1
    result.append(rank)
print(result)
for i in range(N):
    print(scores[i], result[i])
