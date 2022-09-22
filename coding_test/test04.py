# 문제 설명

# 사격장에 있는 점수판은 세로 N칸, 가로 M칸으로 구성되어 있습니다. 각 칸에는 숫자가 쓰여있습니다.
# 점수판의 칸은 (a, b) 형태로 나타내고, 이는 위에서부터 a번째 칸, 왼쪽에서부터 b번째 칸을 의미합니다.
# (a, b)를 맞히면 다섯개의 칸 (a, b), (a-1, b), (a, b-1), (a, b+1), (a+1, b)에 쓰여있는 숫자들의 합만큼 점수를 획득합니다. 단, 점수판의 범위를 벗어나는 칸은 무시됩니다
# 철수가 한 번의 사격으로 얻을 수 있는 점수의 최댓값을 구하는 프로그램을 작성해주세요.
# 첫째 줄에 점수판의 크기를 의미하는 양의 정수 N과 M이 주어집니다. (1 ≤ N, M ≤ 100)
# 이어서 N개의 줄에 M개의 숫자가 공백으로 구분되어 주어집니다. 모든 숫자는 1 이상 100 이하의 양의 정수입니다

# 예제 입력
# 3 3
# 1 2 3
# 4 5 6
# 7 8 9

# 예제 출력
# 29

# 예제 입력
# 1 2
# 23 57

# 예제 출력
# 80

import sys

N, M = map(int, sys.stdin.readline().split())
arr = []
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))
# print(arr)

def get_score(x,y):
    score = arr[x][y]
    if x>=1:
        score += arr[x-1][y]
    if y>=1:
        score += arr[x][y-1]
    if x+1<N:
        score += arr[x+1][y]
    if y+1<M:
        score += arr[x][y+1]
    return score


max_score = -1e9
for i in range(N):
    for j in range(M):
        score = get_score(i,j)
        if max_score < score:
            max_score = score
print(max_score)
