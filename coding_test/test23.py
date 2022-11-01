# 문제 입력 - 성적이 낮은 순서대로 학생 출력하기(초급)

# 첫줄에 학생 수가 주어집니다
# 둘째줄부터 학생 수만큼 이름, 성적이 주어집니다
# 성적이 낮은 순으로 이름을 출력하세요
# 동차인 경우 알파벳 순서로 이름을 출력하세요

# 예제 입력2
# 5
# John 50
# Henry 80
# Hena 30
# Kan 98
# Suji 58

# 예제 출력2
# Hena John Suji Henry Kan

import sys, operator

N = int(sys.stdin.readline())
student = []
for i in range(N):
    name, score = input().split()
    score = int(score)
    student.append([name, score])
# print(student)
# 리스트로 정렬하면 알파벳 오름차순으로 디폴트 정렬됨
student.sort()
student = sorted(student, key=lambda x:(x[1]))

cnt = 0
for i,j in student:
    print(i, end=' ')