# 문제 설명
# 입력값 설명
# 첫 번째 줄에 구간의 길이가 meter 단위로 주어집니다. (1 ≤ 구간의 길이 ≤ 1,000)
# 두 번째 줄에 두 카메라가 제공한 로그의 개수 N이 주어집니다. (1 ≤ N ≤ 3)
# 다음 N줄에 거쳐 출발점의 카메라가 제공한 로그가 주어집니다.
# 다음 N줄에 거쳐 도착점의 카메라가 제공한 로그가 주어집니다.
# 로그는 (차량번호 숫자 4자리) (촬영된 시각) 형식으로 제공되며, 시각은 HH:MM:SS 형식입니다. (00 ≤ HH < 24, 00 ≤ MM, SS < 60)
# 모든 로그의 촬영일은 같으며, 같은 차량에 대해 출발점에서 촬영된 시각은 항상 도착점에서 촬영된 시각보다 앞섭니다. 한 카메라에 같은 차량번호가 두번 이상 주어지지 않습니다. 
# 출발점의 카메라에 등장하는 차량은 반드시 도착점의 카메라에도 등장합니다.

# 출력값 설명
# N개의 줄에 걸쳐 각 차량의 번호와 소수점을 버린 meter / hour 단위의 속력을 공백으로 구분하여 출력합니다.
# 차량 번호가 작은 것부터 출력해야 합니다.

# 예제 입력
# 1000
# 3
# 0000 00:00:00
# 1111 00:00:00
# 2222 00:00:00
# 0000 00:00:01
# 1111 00:01:00
# 2222 10:00:00

# 예제 출력
# 0000 3600000
# 1111 60000
# 2222 100

import sys
import math

meter = int(sys.stdin.readline())
N = int(sys.stdin.readline())

car_time = {}
for i in range(N*2):
    if i <N:
        car_num, time = sys.stdin.readline().split()
        time_info = list(map(int, time.split(":")))
        total = time_info[0]*3600 + time_info[1]*60 + time_info[2]
        car_time[car_num] = [total]
    else:
        car_num, time = sys.stdin.readline().split()
        time_info = list(map(int, time.split(":")))
        total = time_info[0]*3600 + time_info[1]*60 + time_info[2]
        car_time[car_num] += [total]

print(car_time)

for k,v in car_time.items():
    car_time[k] = math.floor((3600*meter)/(v[1]-v[0]))

car_time = sorted(car_time.items())
# car_time.sort()

for i in car_time:
    print(i[0], i[1])