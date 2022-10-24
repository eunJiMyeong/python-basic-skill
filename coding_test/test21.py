# 문제설명 - 무료급식(초급)
# 나이가 많은 사람부터 배식을 진행합니다.
# 나이가 같다면 먼저 온 사람 순서대로 진행합니다

# 예제 입력1
# 4
# 23 Seungkwan
# 23 Dongbin
# 22 Minkyu
# 24 Geonhyuk
# 예제 출력1
# Geonhyuk
# Seungkwan
# Dongbin
# Minkyu

import sys

N = int(sys.stdin.readline())
dict = {}
for i in range(N):
    age, name = input().split()
    age = int(age)
    if age in dict:
        dict[age].append(name)
    else:
        dict[age] = [name]
    
dict = sorted(dict.items(), reverse=True)

for k,v in dict:
    check = False
    if len(v)>1:
        for j in range(len(v)):
            print(v[j])
            check = True
    if check==True:
        pass
    else:
        print(v[0])