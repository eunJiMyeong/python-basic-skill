#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 두번째 숫자 입력할때 오류나면 두번째 숫자를 다시 입력하라고 뜨게끔
# 두번째 숫자를 정상적으로 입력하면 계산이 정상적으로 되게끔
# 딕셔너리나 리스트나 튜플을 활용할 수 있으면 활용하기

first_num = '' # 숫자 변수
first_cal = '' # 사칙연산 변수
second_num = '' # 숫자 변수

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
        if first_num == '':
            first_num = int(input("첫번째 숫자를 입력해주세요"))
            first_cal = input("사칙연산을 입력해주세요")
            if (first_cal != "+") or (first_cal != "-") or (first_cal != "*") or (first_cal != "/"):
                while((first_cal != "+") and (first_cal != "-") and (first_cal != "*") and (first_cal != "/")):
                    first_cal = input("사칙연산을 입력해주세요")
            second_num = int(input("두번째 숫자를 입력해주세요"))
            calculator1 = cal(first_num,first_cal,second_num)
            print(calculator1)
        else:
            second_num = int(input("두번째 숫자를 입력해주세요"))
            calculator1 = cal(first_num,first_cal,second_num)
            print(calculator1)
            
        start = input("계산기를 종료하려면 \"Q\"를 입력해주세요")
        if start == "Q":
            print("계산기를 종료합니다.")
        else:
            first_num = ''
            first_cal = ''
            second_num = ''

    except:
        print("숫자를 입력하세요")

