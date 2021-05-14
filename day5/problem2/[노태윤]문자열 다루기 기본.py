def solution(s):
    # int(s) 가 되면 아래 실행 
    try :
        y = int(s)
        
        # 문자열 length 가 4 또는 6 이면 True
        if (len(s) == 6) or (len(s) == 4) :
            return True
        
        # 문자열 length 가 4 또는 6 이 아니면 False
        else :
            return False
          
    # int(s) 했을 때 오류가 난다면 아래 실행
    except :
        return False

# Keypoint

# len(문자열) 가능
# len(숫자열) 불가능
