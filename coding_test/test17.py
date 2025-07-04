# 문제입력 - 선풍기 (초급)
# 학생들이 일렬로 앉아있고 학생과 학생 사이에 빈칸이 존재합니다. 빈칸에 선풍기를 둘 수 있습니다
# 선풍기의 바람은 선풍기와 바로 이웃한 칸에만 닿습니다. 
# 하나의 선풍기는 최대 두명만 시원하게 할 수 있습니다.

# 첫째 줄에 교실의 길이 N이 주어집니다
# 둘째 줄에 학생을 의미하는 O, 빈칸을 의미하는 X 문자열이 주어집니다. 문자열은 O,X를 각각 하나 이상 포함합니다.
# 또한 모든 학생이 시원해질 수 있는 입력만 주어집니다
# 모든 학생들이 시원해지기 위해 구매해야 하는 선풍기의 최소 개수를 구해라

# 예제 입력
# 3
# XOX
# 예제출력
# 1

# 예제입력
# 5
# OXXOX
# 예제출력
# 2

import sys
N = int(sys.stdin.readline())
seat = list(sys.stdin.readline().rstrip())
check = [False] * N
cnt = 0

for i in range(1, N-1):
    # OXO의 경우일때 선풍기 가운데 1대 둠 (True)
    if seat[i-1]=="O" and seat[i] == "X" and seat[i+1]=="O":
        check[i]=True
    # O로 시작할경우 반드시다음엔 X가 오므로 (모든 학생이 시원해질 수 있는 입력만 주어집니다)
    # O 다음 자리에 선풍기가 없으면(False) 선풍기 놔주기
    if i ==1:
        if seat[0]=="O" and not check[i]:
            check[i]=True
    # XOX, OOX, XOO 경우에 알맞게 선풍기 두기
    if seat[i]=="O" and seat[i-1]=="X" and seat[i+1]=="X" and not check[i-1] and not check[i+1]:
        check[i+1]=True
    if seat[i]=="O" and (seat[i-1]=="X" or seat[i+1]=="X") and not check[i-1] and not check[i+1]:
        if seat[i-1]=="X":
            check[i-1]=True
        elif seat[i+1]=="X":
            check[i+1]=True

# 선풍기 수(True) 세기
print(check.count(True))
