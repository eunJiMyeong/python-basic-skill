#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 변수를 리스트화
# While문 안에 While문은 지양하는게 좋음 (for문 안에 for문은 OK)

num_list = [] # 숫자 리스트
cal_list = [] # 사칙연산 리스트

def cal(num1,cal1,num2):
    if cal1 == '+':
        return int(num1)+int(num2)
    elif cal1 == '-':
        return int(num1)-int(num2)
    elif cal1 == '*':
        return int(num1)*int(num2)
    elif cal1 == '/':
        return int(num1)/int(num2)

start = ''
while(start != 'Q'):
    try:    
        if len(num_list) == 0:
            num_list.append(input("첫번째 숫자를 입력해주세요"))
            if num_list[0].isdigit() == False:
                num_list.pop(0)
                raise Exception('숫자가 아닙니다')
        
        if len(cal_list) == 0:
            cal_list.append(input("첫번째 사칙연산을 입력해주세요"))
            if (cal_list[0] != "+") and (cal_list[0] != "-") and (cal_list[0] != "*") and (cal_list[0] != "/"):
                cal_list.pop(0)
                raise Exception('사칙연산이 아닙니다')
            
        if len(num_list) == 1:
            num_list.append(input("두번째 숫자를 입력해주세요"))
            if num_list[1].isdigit() == False:
                num_list.pop(1)
                raise Exception('숫자가 아닙니다')
            
        calculator1 = cal(num_list[0],cal_list[0],num_list[1])
        
        if len(cal_list) == 1:
            cal_list.append(input("두번째 사칙연산을 입력해주세요"))
            if (cal_list[1] != "+") and (cal_list[1] != "-") and (cal_list[1] != "*") and (cal_list[1] != "/"):
                cal_list.pop(1)
                raise Exception('사칙연산이 아닙니다')
            
        if len(num_list) == 2:
            num_list.append(input("세번째 숫자를 입력해주세요"))
            if num_list[2].isdigit() == False:
                num_list.pop(2)
                raise Exception('숫자가 아닙니다')

        calculator2 = cal(calculator1,cal_list[1],num_list[2])
        print(calculator2)

        start = input("계산기를 종료하려면 \"Q\"를 입력해주세요")
        if start == "Q":
            print("계산기를 종료합니다.")
        else:
            num_list = []
            cal_list = []
            
    
    except Exception as e:
        print("에러가 발생하였습니다", e)


# In[ ]:




