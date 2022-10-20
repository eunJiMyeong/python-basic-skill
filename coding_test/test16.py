# 문제 설명 - 백준 1225 이상한곱셈 (DFS) 브론즈2
# A가 n 자리수, B가 m 자리수 라면 A에서 한 자리를 뽑고, B에서 한 자리를 뽑아 곱셈
# 총 가능한 조합은 n * m 개이고 모든 조합의 값을 더한 수를 출력하라
# 예를들어 121*34는 1*3+1*4+2*3+2*4+1*3+1*4=28 이다
# 첫째줄에 A,B가 주어진다. 모두 10,000자리를 넘지 않는 음이 아닌 정수이다
# 수가 0인 경우에는 0만 주어지며, 그외에 경우의 수는 0으로 시작하지 않는다

# 예제 입력
# 123 45
# 예제 출력 
# 54

# 시간 초과 오답
# import sys
# A, B = map(str, sys.stdin.readline().split())

# if A == "0" or B == "0":
#     print(0)

# nums = []
# for i in A:
#     for j in B:
#         num = int(i)*int(j)
#         nums.append(num)
# print(sum(nums))

import sys
A, B = map(str, sys.stdin.readline().split())
    
A = [int(i) for i in A]
B = [int(i) for i in B]

print(sum(A)*sum(B))
