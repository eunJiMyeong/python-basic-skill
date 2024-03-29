# 문제입력 - 1로 만들기(초급)

# 정수 X가 주어질 때 정수 X에 사용할 수 있는 연산은 다음과 같이 4가지입니다.
# 1. X가 5로 나누어 떨어지면, 5로 나눕니다.
# 2. X가 3으로 나누어 떨어지면, 3으로 나눕니다.
# 3. X가 2로 나누어 떨어지면, 2로 나눕니다.
# 4. X에서 1을 뺍니다.

# 정수 X가 주어졌을 때, 위와 같은 연산 4개를 적절히 사용해서 1을 만들려고 합니다. 
# 연산을 사용하는 횟수의 최솟값을 출력하는 프로그램을 작성해주세요.
# 예를 들어 정수가 26인 경우 26 -> 25 -> 5 -> 1로 3번의 연산이 최솟값입니다.

# 예제 입력1
# 26
# 예제 출력1
# 3

# 예제 입력2
# 99
# 예제 출력2
# 5

# 입력값 설명
# 첫째 줄에 정수 X가 주어집니다. (1 ≤ X ≤ 30,000)

# 출력값 설명
# 첫째 줄에 연산을 하는 횟수의 최솟값을 출력합니다.

import sys
input = sys.stdin.readline

X = int(input())
# 메모이제이션
d = [0] * 30001

for i in range(2, X+1):
    d[i] = d[i-1] + 1
    print(d)
    if i % 2 == 0:
        print(i,2)
        d[i] = min(d[i],d[i//2]+1)
    if i % 3 == 0:
        print(i,3)
        d[i] = min(d[i],d[i//3]+1)
    if i % 5 == 0:
        print(i,5)
        d[i] = min(d[i],d[i//5]+1)
    print(d)
print(d[X])