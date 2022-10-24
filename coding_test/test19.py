# 문제 입력 - 직사각형 세기(초급)

# N × M 격자판이 흰색과 검은색 둘 중 하나로 색칠되어 있습니다.
# 격자판에서 검은색 직사각형의 개수를 출력하는 프로그램을 작성해주세요.
# ▢▢
# ■■
# 예를 들어 위와 같이 2x2 격자판이 색칠되어 있는 경우 검정색 직사각형의 개수는
# ■ : 2 개
# ■■ : 1 개
# 로 총 3개가 있습니다

# 예제 입력1
# 2 2
# 00
# 11
# 예제 출력1
# 3

# 예제 입력2
# 3 3
# 111
# 111
# 111
# 예제 출력2
# 36

# 입력값 설명
# 첫 번째 줄에 두 정수 N, M(1 ≤ N, M ≤ 10)가 공백으로 구분되어 주어집니다.
# 두 번째 줄부터 N개의 줄에 걸쳐 격자판의 각 상태를 나타내는 M개의 숫자가 공백 없이 주어집니다
# 0은 흰색을 1은 검은색을 의미합니다

# 출력값 설명
# 검정색 직사각형의 개수를 출력하세요.

import sys, itertools
N,M = map(int, sys.stdin.readline().split())
array = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
print(array)

rows = list(itertools.combinations_with_replacement(range(N), 2))
cols = list(itertools.combinations_with_replacement(range(M), 2))
print(rows)
print(cols)
answer = 0

# 모든 격자단위를 (0,0)~(N,M)단위까지 탐색함. 
# 탐색해서 모두 1인경우 answer +=1 
for start_1, end_1 in rows:
    for start_2, end_2 in cols:
        temp = 1
        for i in range(start_1, end_1 + 1):
            for j in range(start_2, end_2 + 1):
                print(i,j)
                temp *= array[i][j]
        # print(start_1, end_1, start_2, end_2, temp)
        if temp == 1:
            answer += 1
print(answer)