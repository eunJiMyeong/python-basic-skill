# 문제입력 - 반품(초급)
# 첫 번째 줄에 호준이가 반품하려고 하는 물건의 수 N과, 회사에서 정한 금액 M이 각각 자연수로 주어집니다. (1 ≤ N ≤ 500) (1 ≤ M ≤ 1,000,000)
# 둘째 줄부터 N개의 줄에 걸쳐 물건들의 가격 P(i)가 자연수로 주어집니다.(1 ≤ P(i) ≤ 10,000)

# 가장 비싼 가격의 물품부터 반품할때 반품할 수 있는 물건의 최대 갯수를 구해라

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
P = [int(input()) for _ in range(N)]
P.sort(reverse=True)

cnt = 0
for i in P:
    if M>=i:
        M -= i
        cnt += 1
    
print(cnt)