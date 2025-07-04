# 문제입력- 성적이 높은 순서대로 출력하기(초급)

# 학생 정보는 학생의 이름과 학생의 성적으로 구분됩니다.
# N개의 학생 정보가 주어졌을 때, 성적이 높은 순서대로 학생의 이름을 출력하는 프로그램을 작성해주세요.
# 단, 이름이 같은 학생이 존재할 수 있고, 점수가 같은 학생이 있으면 사전순으로 뒤에 오는 학생을 먼저 출력합니다.

# 예제입력
# 5
# John 50
# Henry 80
# Hena 30
# Kan 98
# Suji 58

# 예제 출력
# Kan Henry Suji John Hena

import sys, operator

N = int(sys.stdin.readline())
student = []
for i in range(N):
    name, score = input().split()
    score = int(score)
    student.append([name, score])

# 리스트로 정렬하면 알파벳 오름차순으로 디폴트 정렬됨
student.sort(reverse=True)
student = sorted(student, key=lambda x:(-x[1]))

for i,j in student:
    print(i, end=' ')
    
    

# 아래처럼 그냥 리스트로 정렬해도 됨
# n = int(input())
# student = []

# for i in range(n):
#     student.append(input().split())
#     print(student)
#     student[i][1] = int(student[i][1])
#     print(student)

# student = sorted(student, key=lambda x:x[1], reverse=True)
# print(student)

# for x in student:
#     print(x[0],end=" ")
