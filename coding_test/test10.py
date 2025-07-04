# 문제 입력 - 이코테 그리디 02 큰수의 법칙

# N개의 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만들어라
# 단 특정한 인덱스에 있는 수가 연속해서 K번을 초과하여 더해질 수 없다
# 같은 수라도 다른 인덱스에 있다면 다른 수로 본다

# 첫째줄에 N, M, K가 주어진다
# 둘째줄에 N개의 자연수가 주어진다
# 입력으로 주어지는 K는 항상 M보다 작거나 같다
# 더해진 답을 출력한다

# 예제 입력
# 5 8 3
# 2 4 5 4 6
# 예제 출력
# 46

N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
sums = 0
first = data[-1]
second = data[-2]

while(M>0):
    for i in range(K):
        sums += first
        M -= 1
        if M == 0:
            break # for문에서 M=0이 되어도 while문이 바로 끝나지 않는다.
    if M >0:
        sums += second
        M -=1 # if문에서 M=0이 되면 while문이 끝남
print(sums)


# 입력받는 숫자가 무한대로 늘어나 시간 초과가 될 경우

N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[-1]
second = data[-2]

cnt = (M//(K+1))*K # 가장큰수를 K번+두번째큰수를 1번 반복해서 더할때 가장큰수를 더하는 횟수
cnt += M%(K+1) # 위 패턴을 모두 돈 후에도 남는 수가 있으면 가장 큰수로 채운다.

result = 0
result += cnt * first
result += (M-cnt) * second
print(result)