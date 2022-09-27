# 문제 설명
# 입력의 첫 줄에는 민겸이가 가지고 있는 막대기의 개수 N이 주어집니다. (1 ≤ N ≤ 10)
# 입력의 두 번째 줄에는 민겸이가 가지고 있는 N개의 막대기의 길이가 공백으로 구분되어 정수로 주어집니다. 막대기의 길이는 1 이상 10 이하입니다.
# 민겸이가 만들 수 있는 직사각형 중 가장 넓이가 큰 직사각형의 넓이를 구하세요.
# 만약 민겸이가 가지고 있는 막대기들을 이용해서 직사각형을 만들 수 없으면 0을 출력하세요.

# 예제 입력1
# 5
# 5 3 9 3 5

# 예제 출력1
# 15

# 예제 입력2
# 4
# 5 1 9 7

# 예제 출력2
# 0

import sys

N = int(sys.stdin.readline())
sticks = list(map(int,sys.stdin.readline().split()))
answer = []
while(len(sticks)!=0):
    max_length = max(sticks)
    if sticks.count(max_length) >= 2:
        answer.append(max_length)
    while(max_length in sticks):
        sticks.remove(max_length)

answer.sort(reverse=True)

if len(answer)>=2:
    print(answer[0]*answer[1])
else:
    print(0)