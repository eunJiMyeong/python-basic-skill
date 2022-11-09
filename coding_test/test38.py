# 문제설명 - 약수가 소수인지 판별 (초급)

# 입력값 설명
# 첫째 줄에 정수 A가 주어집니다. (1 ≤ A ≤ 10,000,000)

# 출력값 설명
# 정수 A를 두 소수의 곱으로 나타낼 수 있으면 두 숫자를 오름차순으로 출력합니다. 가능한 소수의 쌍이 많은 경우 가장 작은 소수와의 곱을 출력합니다.
# 만약 정수 A를 두 소수의 곱으로 나타낼 수 없다면 IMPOSSIBLE을 출력합니다.

# 예제 입력1
# 15
# 예제 출력1
# 3 5

# 예제 입력2
# 20
# 예제 출력2
# IMPOSSIBLE

import sys
input = sys.stdin.readline

N = int(input())

# 소수 판별 함수
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

prime_set = set()
answer = [0,0]

for i in range(2, (N//2)+1):
    # N이 i로 나누어지고(약수가 있고), 약수가 소수인경우
    if N % i == 0 and is_prime(i):
        mod, remain = divmod(N,i) # 처음 약수가 나온경우 prime_set에 집어넣음
        # 두번째 약수 나온경우부터 첫번째약수랑 비교 (어차피 가장 작은 값부터 오름차순으로 출력이니까)
        if remain == 0 and mod in prime_set:
            answer[0], answer[1] = min(mod, i), max(mod, i)
            break
        prime_set.add(i)

print(f'{answer[0]} {answer[1]}' if answer[0] != 0 else 'IMPOSSIBLE')