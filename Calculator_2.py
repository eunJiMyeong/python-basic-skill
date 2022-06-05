#!/usr/bin/env python
# coding: utf-8

# In[2]:


# if문이 한가지 기능만 수행하도록 독립적으로 설계할 것

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
            first_num = int(input("첫번째 숫자를 입력해주세요"))
        
        if first_cal == '':
            first_cal = input("첫번째 사칙연산을 입력해주세요")
            if (first_cal != "+") or (first_cal != "-") or (first_cal != "*") or (first_cal != "/"):
                while((first_cal != "+") and (first_cal != "-") and (first_cal != "*") and (first_cal != "/")):
                    first_cal = input("사칙연산을 입력해주세요")
            
        if second_num == '':
            second_num = int(input("두번째 숫자를 입력해주세요"))
            
        calculator1 = cal(first_num,first_cal,second_num)
        
        if second_cal == '':
            second_cal = input("두번째 사칙연산을 입력해주세요")
            if (second_cal != "+") or (second_cal != "-") or (second_cal != "*") or (second_cal != "/"):
                while((second_cal != "+") and (second_cal != "-") and (second_cal != "*") and (second_cal != "/")):
                    second_cal = input("사칙연산을 입력해주세요")
            
        if third_num == '':
            third_num = int(input("세번째 숫자를 입력해주세요"))

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
            
    
    except:
        print("숫자를 입력하세요")


# In[ ]:




