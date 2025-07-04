# 문제 설명
# 좀비 게임 : 술래를 먼저 한명 정한 뒤, 술래가 아이들을 쫓아다니며 몸을 터치하면 터치된 아이도 같이 술래가 됩니다
# 술래끼리 혹은 술래가 아닌 아이끼리도 터치는 할 수 있지만 이 경우 아무일도 일어나지 않는다는 점에 주의해주세요

# 입력값 설명
# 첫 번째 줄에 좀비 게임을 하는 아이들의 수를 나타내는 정수 N과 좀비 게임의 첫 술래를 나타내는 정수 A가 주어집니다. (2 ≤ A ≤ N ≤ 1,000)
# 두 번째 줄에 좀비 게임을 하는 동안 아이들끼리 터치가 일어난 횟수 M이 주어집니다. (1 ≤ M ≤ 1,000)
# 세 번째 줄부터 M개의 줄에 걸쳐서 서로 터치가 일어난 아이들의 번호가 X, Y로 주어집니다. (1 ≤ X, Y ≤ N, X ≠ Y)

# 예제 입력1
# 5 1
# 3
# 1 2
# 2 3
# 4 5

# 예제 출력1
# 3

# 예제 입력2
# 5 1
# 5
# 1 5
# 2 3
# 5 4
# 2 4
# 2 1

# 예제 출력2
# 4

import sys

N, A = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline())
answer = []
answer.append(A)
for i in range(M):
    touch = list(map(int,sys.stdin.readline().split()))
    for j in answer:
        if j in touch:
            answer.append(touch[0])
            answer.append(touch[1])
            break
            
# print(answer)
# print(set(answer))
print(len(set(answer)))