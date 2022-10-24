# 문제 설명 - 전투력(초급)
# 용병들을 모으려고 합니다. 용병들은 각각의 전투력을 가지고 있습니다.
# 가장 전투력이 낮은 용병과 동일하게 나머지 용병들의 전투력이 조정됩니다
# 예를 들어 용병이 4명이고, 각 용병의 전투력이 (43, 50, 80, 23)이라면 최대 전투력의 합은 (43, 50, 80)을 선택한 것으로 43 * 3 = 129입니다.
# 23*4= 92로 129보다 낮기 때문에 3명을 선택해서 전투에 참전하는것이 유리하다

# 예제 입력1
# 4
# 43 50 80 23
# 예제 출력1
# 129

# 예제 입력2
# 2
# 12 16
# 예제 출력2
# 24

# 입력값 설명
# 첫째 줄에 용병의 수 N이 주어집니다. (1 ≤ N ≤ 10,000)
# 둘째 줄에는 각 용병들의 전투력 K가 공백을 기준으로 주어집니다. (1 ≤ K ≤ 10,000)
# 출력값 설명
# 첫째 줄에 문제에서 요구하는 정답을 출력하세요.

import sys

N = int(sys.stdin.readline())
fighters = list(map(int, sys.stdin.readline().split()))
fighters = sorted(fighters)
max_power= []
for i in range(len(fighters)):
    max_power.append(fighters.pop(0)*(len(fighters)+1))
print(max(max_power))