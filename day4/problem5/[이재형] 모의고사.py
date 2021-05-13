def solution(answers):
    answer = []
    a = [1, 2, 3, 4, 5] * 2000
    b = [2, 1, 2, 3 ,2, 4, 2, 5] * 1250
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    
    if len(a) >= len(answers) : ##이게 없어도 될듯 함..
        for i in range(len(answers)) :
            if a[i] != answers[i]:
                a[i] = 0
            else :
                a[i] = 1

            if b[i] != answers[i]:
                b[i] = 0
            else :
                b[i] = 1

            if c[i] != answers[i]:
                c[i] = 0
            else :
                c[i] =1

    a = sum(a[:len(answers)])
    b = sum(b[:len(answers)])
    c = sum(c[:len(answers)])
    d = [a, b, c]
    for i in range(1, 4):
        if d[i-1] == max(d):
            answer.append(i)
        
        
    return answer




