def solution(s):
    # 길이 구하기
    length = len(s)
    
    # 홀수면 아래 실행
    if length % 2 == 1 :
        answer = s[length//2]
        
    # 짝수면 아래 실행
    else :
        answer = s[length//2-1:length//2+1]
    return answer
