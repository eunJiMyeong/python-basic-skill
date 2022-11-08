# 문제입력 - 배열돌리기(초급)
# 배열을 몹시 좋아하는 또리는 배열로 다음과 같은 연산을 할 수 있습니다.
# 배열의 가장 왼쪽 원소를 제거한 뒤, 그 원소를 배열의 가장 오른쪽에 넣는다.
# 길이가 N인 배열이 주어졌을 때, 초기 상태 배열을 출력하고 해당 연산을 N-1번 수행하고 각 연산이 수행될 때마다 배열을 출력하는 프로그램을 작성해주세요.
# 예를 들어, 배열의 길이가 5이고 들어있는 수가 순서대로 5, 7, 8, 2, 6라면 다음과 같이 5번 출력해야 합니다.

# 5 7 8 2 6
# 7 8 2 6 5
# 8 2 6 5 7
# 2 6 5 7 8
# 6 5 7 8 2

# 예제 입력1
# 5
# 1 2 3 4 5

# 예제 출력1
# 1 2 3 4 5
# 2 3 4 5 1
# 3 4 5 1 2
# 4 5 1 2 3
# 5 1 2 3 4

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))
queue = deque(array)
print(*queue)
for i in range(N-1):
    queue.rotate(-1)
    print(*queue)