# 문제입력 - 소수판별(초급)
# 입력된 숫자가 소수이면 1, 소수가 아니면 0을 출력하라

import sys
A = int(sys.stdin.readline())
check = True
if A < 2:
    check = False
else:
    for x in range(2,int(A**0.5)+1):
        if A % x == 0:
            check = False

if check:
    print(1)
else:
    print(0)