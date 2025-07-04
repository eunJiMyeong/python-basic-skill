# 문제 입력
# N번 게임을 진행하며 결과는 승리 또는 패배 중 하나입니다. 
# 각 게임을 마쳤을 때 현재 연승 수, 현재 연패 수, 최장 연승 기록, 최장 연패 기록을 알려주세요
# 게임에서 승리하면 연패수가 0으로 초기화되고, 현재 연승수는 1 증가합니다.
# 반대로 게임에서 패배하면 현재 연승수가 0으로 초기화되고, 현재 연패수는 1 증가합니다.

# 입력값 설명
# 첫 번째 줄에 게임을 한 횟수 N이 주어집니다. (1 ≤ N ≤ 10)
# 다음 N개의 줄에 걸쳐 첫번째 게임부터 N번째 게임까지의 결과가 순서대로 주어집니다.

# 출력값 설명
# 총 N개의 줄을 출력합니다
# i(1 ≤ i ≤ N)번째 줄에는 i번째 게임을 마쳤을 때의 현재 연승 수, 현재 연패 수, 최장 연승 기록, 최장 연패 기록을 공백으로 구분하여 순서대로 출력합니다.

# 예제 입력
# 8
# WIN
# LOSE
# WIN
# WIN
# WIN
# LOSE
# LOSE
# WIN

# 예제 출력
# 1 0 1 0
# 0 1 1 1
# 1 0 1 1
# 2 0 2 1
# 3 0 3 1
# 0 1 3 1
# 0 2 3 2
# 1 0 3 2

import sys

N = int(sys.stdin.readline())
history = []
win = []
lose = []
for i in range(N):
    result = sys.stdin.readline().rstrip()
    history.append(result)    
    
    if history[0] != result:
        opposite = history[0]
        while(opposite in history):
            history.remove(opposite)
    
    win.append(history.count("WIN"))
    lose.append(history.count("LOSE"))
    
    # print(result)
    # print(history)

    print(history.count('WIN'), history.count('LOSE'), max(win), max(lose))
