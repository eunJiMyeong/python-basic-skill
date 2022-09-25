# 문제 설명
# 현재 텍스트 에디터에 입력된 전체 내용을 S, 현재 커서 위치를 cur (0 ≤ cur ≤ |S|), 
# 찾고 싶은 내용을 s, 바꾸고 싶은 내용을 t라고 했을 때
# S[i .. i+|s|-1] = s를 만족하는 최소의 i (i ≥ cur)를 찾아서 t로 바꾸면 됩니다.
# i는 커서 뒤에 있는 index 여야 한다.
# 만약 해당하는 i가 존재하지 않는 경우, 아무 동작도 하지 않습니다.

# 첫째 줄에 알파벳 소문자로만 이루어진 문자열 S가 입력됩니다. (1 ≤ |S| ≤ 50)
# 둘째 줄에 찾아바꾸기를 사용한 횟수 N이 입력됩니다. (1 ≤ N ≤ 10)
# 셋째 줄부터 N개의 줄에 걸쳐서 문제에서 설명한 s, t, cur이 공백으로 구분되어 입력됩니다. 
# (1 ≤ |s|, |t| ≤ 50, 0 ≤ cur ≤ |S|)

# 입력 예제
# qwertyuiop
# 3
# wer ab 1
# tyu ccccc 2
# qab ii 5

# 출력 예제
# qabtyuiop
# qabccccciop
# qabccccciop

import sys

S = sys.stdin.readline()
N = int(sys.stdin.readline())

for i in range(N):
    s,t,cur = sys.stdin.readline().split()
    S = S[:int(cur)] + S[int(cur):].replace(s,t)
    print(S)

print(S)