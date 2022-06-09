#!/usr/bin/env python
# coding: utf-8

# In[10]:


# 1.딕셔너리 변수를 선언하세요
# 2. 딕셔너리 변수안에는 commnd 라는 변수가 존재해야합니다
# 3. while 문을 이용하여 작업하세요
# 4. input 함수를 사용해서 commond 변수에 저장하세요
# 5. print 함수를 사용하여 input 으로 입력받은 명령어를 출력하세요

#######################################
# 딕셔너리를 선언하세요

#while 1 :
  ######## 프로그램을 완성하세요
Start = ''
dict = {'command':''}
while(Start != 'Q'):
    dict['command'] = input("변수를 입력하세요")
    Start = input("종료하려면 Q를 입력하세요")
    if Start == 'Q':
        break
print(dict)

