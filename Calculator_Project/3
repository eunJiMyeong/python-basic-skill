#!/usr/bin/env python
# coding: utf-8

# In[1]:


# While문 안에 While문은 지양하는게 좋음 (for문 안에 for문은 OK)

first_num = '' # 숫자 변수
first_cal = '' # 사칙연산 변수
second_num = '' # 숫자 변수
second_cal = '' # 사칙연산 변수
third_num = '' # 숫자 변수


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
            first_num = input("첫번째 숫자를 입력해주세요")
            if first_num.isdigit() == False:
                first_num = ''
                raise Exception('숫자가 아닙니다')
        
        if first_cal == '':
            first_cal = input("첫번째 사칙연산을 입력해주세요")
            if (first_cal != "+") and (first_cal != "-") and (first_cal != "*") and (first_cal != "/"):
                first_cal = ''
                raise Exception('사칙연산이 아닙니다')
            
        if second_num == '':
            second_num = input("두번째 숫자를 입력해주세요")
            if second_num.isdigit() == False:
                second_num = ''
                raise Exception('숫자가 아닙니다')
            
        calculator1 = cal(first_num,first_cal,second_num)
        
        if second_cal == '':
            second_cal = input("두번째 사칙연산을 입력해주세요")
            if (second_cal != "+") and (second_cal != "-") and (second_cal != "*") and (second_cal != "/"):
                second_cal = ''
                raise Exception('사칙연산이 아닙니다')
            
        if third_num == '':
            third_num = input("세번째 숫자를 입력해주세요")
            if third_num.isdigit() == False:
                third_num = ''
                raise Exception('숫자가 아닙니다')

        calculator2 = cal(calculator1,second_cal,third_num)
        print(calculator2)

        start = input("계산기를 종료하려면 \"Q\"를 입력해주세요")
        if start == "Q":
            print("계산기를 종료합니다.")
        else:
            first_num = ''
            first_cal = ''
            second_num = ''
            second_cal= ''
            third_num = ''    
            
    
    except Exception as e:
        print("에러가 발생하였습니다", e)

