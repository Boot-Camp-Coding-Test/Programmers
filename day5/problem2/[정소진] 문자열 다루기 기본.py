def solution(str):
  
    if len(str) == 4 or len(str) == 6:
        try : 
            str = int(str)
            return True
        except :
            return False
        
    return False
