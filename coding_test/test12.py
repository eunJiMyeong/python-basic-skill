# 문제 입력 - 이코테 그리디 04. 1이 될 때까지

# 어떤 수 N이 1이 될때까지 다음 두 과정 중 하나를 반복적으로 선택하여 수행
# 단 두번째 연산은 N이 K로 나누어떨어질때만 선택할 수 있다
# 1. N에서 1을 뺀다
# 2. N을 K로 나눈다

# N이 1이 될때까지 1번 혹은 2번의 과정을 수행해야 하는 최소 횟수를 구해라

# 첫째줄에 N K가 공백으로 주어진다
# N이 1이 될때까지 1번 혹은 2번의 과정을 수행하는 횟수의 최솟값 입력

# 입력 예시
# 25 5

# 출력 예시
# 2

N, K = map(int, input().split())
cnt = 0
while True:
    if N%K!=0:
        N -= 1
        cnt += 1
    else:
        N //= K
        cnt += 1
    
    if N ==1:
        break
print(cnt)


# 이코테 답안
N, K = map(int, input().split())
result = 0
while True:
    target = (N//K)*K # K로 나누어떨어지는 수를 구함
    result += (N-target) # 나누어떨어지는 수 외의 수 -1 연산처리 횟수
    N = target
    if N < K:
        break
    result += 1
    N //= K

result += (N-1) # 위 while문이 다 돌아가면 정상카운팅 +1 이라 -1 해주는것
print(result)