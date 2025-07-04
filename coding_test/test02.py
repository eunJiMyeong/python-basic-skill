# 문제 설명
# 하루에 1초씩 느려지는 시계가 있다
# 시계를 12시에 맞춘뒤, N일 후 시계가 가르키는 시각을 출력하라
# 첫줄에 N이 입력된다
# (1 ≤ N ≤ 1,000)

# 예제 입력
# 51
# 예제 출력
# 11:59:09

import sys
N = int(sys.stdin.readline())
answer = '11:'
second = 60-(N%60)
minute = 60-(N//60+1)
answer += str(second)+":"
answer += str(minute)

print(answer)
