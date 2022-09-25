# 문제 설명
# 첫줄에 HH:MM:SS 형태로 시간이 주어짐
# 두번째엔 몇 초(t)마다 카운트 할지가 주어짐
# (1 ≤ t ≤ 60)
# 세번째엔 t초마다 몇 번 카운트(n)할지가 주어짐
# (1 ≤ n ≤ 120)
# 첫줄에 주어진 시간에서 t초마다 n-1번 카운트 했을때 최종 시간을 출력하라

# 예제 입력
# 23:59:30
# 31
# 2
# 예제 출력
# 00:00:01

import sys

# 0n으로 된 경우 n만 저장
hour, minute, second = map(int, sys.stdin.readline().split(':'))
t = int(sys.stdin.readline())
n = int(sys.stdin.readline())

plus = t * (n - 1)

second += plus

minute += second//60
second %= 60
hour += minute//60
minute %= 60
hour %= 24

answer = ''
if hour <10:
    answer += '0'+str(hour)
answer += ":"
if minute <10:
    answer += '0'+str(minute)
answer += ":"
if second<10:
    answer += '0'+str(second)

print(answer)
