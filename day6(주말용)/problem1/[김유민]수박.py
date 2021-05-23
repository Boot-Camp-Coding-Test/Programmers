def solution(n):
    refer_str = '수박'
    answer = []
    
    for i in range(n) :
        answer.append(refer_str[i%len(refer_str)])
    
    return ''.join(answer)
