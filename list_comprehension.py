#!/usr/bin/env python
# coding: utf-8

# In[5]:


r1 = [1,2,[3,4]]   # 리스트 안에 리스트 생성 방법
r2 = list('Hello')  # 문자열을 리스트로 전달

r3 = list((5,6,7))  # 튜플을 리스트로 전달

r4 = list(range(0,7))  # range를 리스트로 전달


# Q1. [1,2,3,4,5] 를 두 배씩 증가시킨 리스트를 만들어라
r5 = [1,2,3,4,5]
r6 = []    # 일단 빈 리스트를 생성하고
for a in r5:
    r6.append(a * 2)



# Q1을 '리스트 컴프리헨션'을 이용해서 풀면 아래와 같다
r5 = [1,2,3,4,5]
r7 = [ x * 2 for x in r5 ] 



# Q2. 조건 값을 추가 - 홀수인 경우에만 두배씩 증가
r5 = [1,2,3,4,5]
r8 = []
for i in r5:
    if i % 2:    # i가 홀수인 경우에만 문장 실행
        r8.append(i * 2)



# Q2를 '리스트 컴프리헨션'을 이용해서 풀면 아래와 같다
r5 = [1,2,3,4,5]
r9 = [ x * 2 for x in r5 if x % 2]


# Q3. 다음 데이터의 조합으로 나올 수 있는 모든 조합을 구해라 - for문 활용
color = ['Black', 'White']
item = ['Ring', 'Ball', 'Pin']
r10 = []
for x in color:
    for y in item:
        r10.append(x + y)



# Q3를 '리스트 컴프리헨션'을 이용해서 풀면 아래와 같다
color = ['Black', 'White']
item = ['Ring', 'Ball', 'Pin']
r11 = [x + y for x in color for y in item]



# Q4. '리스트 컴프리헨션'을 이용하여 2*1,2*2..부터 9*9까지 구구단의 값을 리스트에 넣어라
r12 = [x * y for x in range(2,10) for y in range(1,10)]


# Q4에서 2의 배수는 제외하는 조건을 건다면?
r13 = [x * y for x in range(2,10) for y in range(1,10) if (x*y) % 2]


# In[ ]:




