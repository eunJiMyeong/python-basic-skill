#!/usr/bin/env python
# coding: utf-8

# In[1]:


# q0012 문제 
# 아래 프로그램을 수정하여 똑같은 출력내용을 완성하세요
# 출력문
###########################
# 전체 7개 값중 첫번째 값 0
# 전체 7개 값중 두번째 값 1
# 전체 7개 값중 세번째 값 2
# .... 등등
###########################
# intList 의 길이를 구하는 함수를 인터넷으로 검색해서 사용하세요
# 변수를 추가하거나 아래 로직을 마음대로 수정하세요

#intList = list(range(0,7))

#for x in intList :


#-----------------------
#답안

intList = list(range(0,7))
stringList = ['첫번째', '두번째', '세번째', '네번째', '다섯번째', '여섯번째', '일곱번째']
temp = stringList

for x in intList:
    print("전체 {}개 중".format(len(intList)),temp[x],"값")


# In[15]:


# q0013 문제 

# for문 을 활용할세요
# 물자열 찾기 함수를 활용하세요
# 아래와 같은 출력문을 완성하세요

# python 에는 o 가 존재합니다
# WELCOME 에는 해당문자가 존재하지 않습니다
# Tutorial 에는 o 가 존재합니다
# tistory 에는 o 가 존재합니다
# github 에는 해당문자가 존재하지 않습니다


#stringArr = ['python','WELCOME','Tutorial','tistory','github']

#for x in stringArr :
    #코드를 완성하세요


#-----------------------
#답안

stringArr = ['python','WELCOME','Tutorial','tistory','github']

for x in stringArr:
    if "o" in x:
        print(x,"에는 o가 존재합니다")
    else:
        print(x, "에는 해당문자가 존재하지 않습니다")


# In[1]:


# q0014 문제
# 이중 for 문을 활용하세요
# 구구단을 출력하세요
# 출력 예시
# 1 * 1 = 1
# 1 * 2 = 2
# 1 * 3 = 3
# ...
# 2 * 1 = 2
# 2 * 2 = 4
# ...
# 3 * 1 = 3
# ...9까지

#-----------------------
#답안

intList = [1,2,3,4,5,6,7,8,9]
one = [1,2,3,4,5,6,7,8,9]
for x in intList:
    for y in one:
        print(f'{x}*{y}={y*x}')

