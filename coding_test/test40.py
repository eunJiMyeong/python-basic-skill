# 백준 1202 보석도둑 (초급)

# 세계적인 도둑 상덕이는 보석점을 털기로 결심했다.
# 상덕이가 털 보석점에는 보석이 총 N개 있다. 각 보석은 무게 Mi와 가격 Vi를 가지고 있다. 상덕이는 가방을 K개 가지고 있고, 각 가방에 담을 수 있는 최대 무게는 Ci이다. 가방에는 최대 한 개의 보석만 넣을 수 있다.
# 상덕이가 훔칠 수 있는 보석의 최대 가격을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N과 K가 주어진다. (1 ≤ N, K ≤ 300,000)
# 다음 N개 줄에는 각 보석의 정보 Mi와 Vi가 주어진다. (0 ≤ Mi, Vi ≤ 1,000,000)
# 다음 K개 줄에는 가방에 담을 수 있는 최대 무게 Ci가 주어진다. (1 ≤ Ci ≤ 100,000,000)
# 모든 숫자는 양의 정수이다.

# 출력
# 첫째 줄에 상덕이가 훔칠 수 있는 보석 가격의 합의 최댓값을 출력한다.

# 예제입력
# 3 2
# 1 65
# 5 23
# 2 99
# 10
# 2
# 예제출력
# 164

import sys, heapq
input = sys.stdin.readline

N, K = map(int, input().split())
mv = []
# 보석 리스트를 애초에 힙큐 리스트로 만듦
for _ in range(N):
    heapq.heappush(mv, list(map(int, input().split())))

# 가방의 가용성을 오름차순으로 정렬(작은것부터 비교해서 담자!)
C = [int(input()) for _ in range(K)]
C.sort()

answer = 0
tmp_mv = []

for i in C:
    # 보석이 남아있고, 보석의 무게가 가방 가용성과 같거나 작을때(가방에 담을 수 있을때), 
    # 보석 리스트는 힙큐리스트라 보석 무게가 작은것부터 비교
    while mv and i>= mv[0][0]:
        # 담을 수 있는 보석은 모조리 꺼내서 tmp_mv에 담는다
        # 보석 가격은 큰 순으로 담아야 하니까 - 처리 (2 5 중 젤 작은건 2지만 -2 -5중 젤 작은건 -5다. 이런식으로 max힙로직으로 바꿔줘야함)
        heapq.heappush(tmp_mv, -heapq.heappop(mv)[1])
        print(i, tmp_mv, mv)    
    if tmp_mv:
        # tmp_mv에 원소가 있을때 젤 큰가격을 answer에 추가 (위에서 -로 map힙으로 바꿨으니)
        answer += heapq.heappop(tmp_mv)
        print(answer)
print(-answer)