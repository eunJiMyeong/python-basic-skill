#!/usr/bin/env python
# coding: utf-8

# In[13]:


# q0103 에서 완성한 프로그램을 그대로 복사 후 개선합니다
# 개선 작업
# 1. 입력받은 명령어가 '@w' 일 경우 '위로 이동합니다' 를 출력하세요
# 2. 입력받은 명령어가 '@a' 일 경우 '왼쪽으로 이동합니다' 를 출력하세요
# 3. 입력받은 명령어가 '@s' 일 경우 '아래로 이동합니다' 를 출력하세요
# 4. 입력받은 명령어가 '@d' 일 경우 '오른쪽으로 이동합니다' 를 출력하세요

dict = {'command':''}
while(dict['command'] == ''):
    try:
        dict['command'] = input("위로이동: @w / 왼쪽이동: @a / 아래이동: @s / 오른쪽이동: @d / 종료: Q")
        if dict['command'] == '@w':
            print("위로 이동합니다.")
        elif dict['command'] == '@a':
            print("왼쪽으로 이동합니다.")
        elif dict['command'] == '@s':
            print("아래로 이동합니다.")
        elif dict['command'] == '@d':
            print("아래로 이동합니다.")
        elif dict['command'] == 'Q':
            dict['command'] == ''
            print("종료합니다")
        else:
            dict['command'] = ''
            print("잘못된 입력입니다")
    except:
        print("오류입니다")
        dict['command'] = ''

