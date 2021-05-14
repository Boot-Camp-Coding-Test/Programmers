def solution(answers):
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]
    for i in range(1, len(answers)+1):
        if a[i%5-1]==answers[i-1]:
            score[0]+=1
        if b[i%8-1]==answers[i-1]:
            score[1]+=1
        if c[i%10-1]==answers[i-1]:
            score[2]+=1
    answer = []
    for idx, i in enumerate(score):
        if i == max(score):
            answer.append(idx+1)
    return answer
