def solution(x):
  
    # ['1','2','3'] 형태로 반환
    new_num_list = list(str(x))
    adder = 0
    
    # 자릿수에 있는 것 다 더하기
    for i in new_num_list :
        adder+=int(i)
    
    # 원래 숫자에서 나누어 떨어지면 True
    if x % adder == 0 :
        return True
    
    # 아니면 False
    else :
        return False
