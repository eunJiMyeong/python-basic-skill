# 문제입력 - 데이트 자본주의(초급)

# 첫째 줄에 동빈이가 현재 갖고 있는 돈의 액수 N과 매칭가능한 상대의 수 M이 입력됩니다. (1 ≤ N, M ≤ 1000)
# 둘째 줄에 상대들의 매칭 가격 P(i)가 공백을 기준으로 입력됩니다. (1 ≤ P(i) ≤ 1,000)

# 동빈이가 최대로 만날 수 있는 상대의 수를 출력합니다.
#  (단, 동빈이는 최대한 매칭 비용이 비싼 상대부터 만나보고 싶어 합니다. )
# 예를 들어 동빈이가 1000의 돈을 가지고 있고 매칭 가능한 상대의 수가 5명으로 각각 300, 200, 500, 400, 100의 매칭 가격을 가진다면,
# 동빈이는 (500, 400, 100)으로 세 번의 매칭을 하게 됩니다.

# 예제입력
# 1000 5
# 300 200 500 400 100
# 예제출력
# 3

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
price = list(map(int, sys.stdin.readline().split()))
price.sort(reverse=True)
que = deque(price)
cnt = 0

while que:    # que에 원소가 있는동안 while문 동작
    max_cost = que.popleft()
    if N >= max_cost:
        N -= max_cost
        cnt += 1
        continue
    else:
        if que: # que의 원소가 하나인경우 max_cost값 취하면서 que=([])가 되므로 해당 조건없으면 에러뜸
            min_cost = que.pop()
            if N>= min_cost:
                N -= min_cost
                cnt+=1
        else:
            break
print(cnt)
    