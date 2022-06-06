#!/usr/bin/env python
# coding: utf-8

# In[14]:


# 슬라이스 구성 [시작위치:종료위치(:증가값)]
# 'abc defg' 의 정방향 순서는 띄어쓰기 포함해서 0,1,2,3,4,5,6,7 (0부터 시작)
# 역방향순서는 띄어쓰기 포함해서 -8,-7,-6,-5,-4,-3,-2,-1 (-1부터 시작)

a = '0123456789'

print(a[0:0]) # 아무것도 출력되지 않음
print(a[:]) # 전체 출력
print(a[0:7]) # 시작->종료 순서가 정방향이면 '종료순서-1' 까지 출력됨
print(a[7:1:-1]) #시작->종료 순서가 역방향이면 증가값에 '-'숫자 들어가야 작동됨 / 역방향인경우 '종료순서+1'까지 출력됨
print(a[-8:-3]) # 시작->종료 순서가 정방향이므로 '종료순서-1'해서 -4자리인 6까지 출력됨. 
print(a[-1:-7:-3]) # 역방향진행에(종료순서+1) 2칸씩 건너뜀
print(a[1:-1:2]) # 정방향진행에(종료순서-1) 1칸씩 건너뜀


# In[ ]:




