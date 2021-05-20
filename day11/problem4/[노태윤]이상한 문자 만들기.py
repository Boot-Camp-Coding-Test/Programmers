def solution(s):
    answer = ''
    index = 0
    for i in s :
        if i == ' ' :
            index = 0
            answer+=' '
            continue
        if index % 2 == 0 :
            answer+= i.upper()
        else :
            answer+= i.lower()
        index+=1
    return answer

# Key points
  # 문자 간의 공백이 하나 이상!
  # 단어 별로 짝/홀수 인덱스
