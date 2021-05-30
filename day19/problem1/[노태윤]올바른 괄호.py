# 통과는 했지만 del 안 쓰고 다시 해보자

from collections import deque

def solution(s):
    queue = deque(s)
    stack_list = []
    n = 0
    while n < len(s) : 
        popped = queue.popleft() # s 맨 앞 문자 pop
        stack_list.append(popped) # stack 리스트에 append

        if len(stack_list) == 1 : # stack 리스트에 element 가 하나라면 n+=1 해주고 continue
            n+=1
            continue
        
        if stack_list[-1] == ')' and stack_list[-2] == '(' : # 만약 stack 리스트 마지막 전 & 마지막 element 가 '(' , ')' 이면 stack 리스트에서 delete
            del stack_list[-2:]
        
        n+=1

    if not stack_list : # stack 리스트에 element 가 없으면 True
        return True
    else : # stack 리스트에 element 가 있으면 False
        return False
