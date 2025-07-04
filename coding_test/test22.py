# 문제입력 - 재고정리(초급)

# 서로 다른 신발에는 서로 다른 번호가 붙어있습니다. 
# 매장안의 신발을 모두 모아 재고가 가장 많은 신발을 알아내려고 합니다
# 재고 수가 동일한 경우 신발 번호가 가장 큰 번호를 출력하세요

# 예제 입력1
# 8
# 5
# 2
# 2
# 5
# 1
# 5
# 3
# 3

# 예제 출력1
# 5

import sys, operator

N = int(sys.stdin.readline())
dict = {}
for _ in range(N):
    cloth = int(sys.stdin.readline())
    if cloth in dict:
        dict[cloth] += 1
    else:
        dict[cloth] = 1

dict = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)
max_cnt = -1e9
answer = []
for k,v in dict:
    if max_cnt <= v:
        max_cnt = v
        answer.append(k)
print(max(answer))